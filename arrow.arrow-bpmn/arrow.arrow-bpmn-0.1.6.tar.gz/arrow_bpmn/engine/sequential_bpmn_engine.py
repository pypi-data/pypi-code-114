import logging
import uuid
from typing import List

from arrow_bpmn.__spi__ import CompleteAction, IncidentAction
from arrow_bpmn.__spi__ import NodeRef
from arrow_bpmn.__spi__.action import Action, EventAction
from arrow_bpmn.__spi__.action import ContinueAction
from arrow_bpmn.__spi__.action.cascade_action import CascadeAction
from arrow_bpmn.__spi__.action.dequeue_action import DequeueAction
from arrow_bpmn.__spi__.action.queue_action import QueueAction
from arrow_bpmn.__spi__.action.resume_action import ResumeAction
from arrow_bpmn.__spi__.execution import Environment
from arrow_bpmn.__spi__.execution import State
from arrow_bpmn.__spi__.registry.event import Event
from arrow_bpmn.__spi__.types import OptDict
from arrow_bpmn.engine.abstract_engine import BpmnEngine, ProcessRef
from arrow_bpmn.engine.registry.abstract_event_registry import NoneEvent


def flatten(iterable):
    return [item for sublist in iterable for item in sublist]


def first(iterable):
    return iterable[0]


class SequentialBpmnEngine(BpmnEngine):

    def invoke_by_event(self, event: Event, init_state: OptDict = None, header: OptDict = None) -> List[State]:
        def invoke(subscription: NodeRef):
            process = self.process_store.read_process(ProcessRef(event.group, subscription.process_id))
            environment = Environment(event.group, process, self.factories)

            is_reentry = not environment.is_start_event(subscription.node_id)
            state = State(init_state or {}, subscription, is_reentry, header=header)

            result = self._handle_action(ContinueAction(subscription.node_id), state, environment)
            return result[0]

        subscriptions = self.event_registry.get_subscriptions(event)
        assert len(subscriptions) > 0, "no subscriptions found"
        return list(map(invoke, subscriptions))

    def resume_by_event(self, event: Event, init_state: OptDict = None) -> List[State]:
        def resume_process(node_ref: NodeRef) -> List[State]:
            state = self.process_store.read_state(node_ref)
            state.properties.update(init_state or {})

            process = self.process_store.read_process(ProcessRef(event.group, node_ref.process_id))
            environment = Environment(event.group, process, self.factories)

            action = ContinueAction(node_ref.node_id)
            return self._handle_action(action, state, environment)

        node_refs = self.event_registry.get_subscriptions(event)
        return flatten([resume_process(node_ref) for node_ref in node_refs])

    def invoke_by_id(self, ref: ProcessRef, init_state: OptDict = None, header: OptDict = None) -> State:
        return self.invoke_by_event(NoneEvent(ref.group, ref.process_id), init_state, header)[0]

    def _handle_action(self, action: Action, state: State, env: Environment) -> List[State]:
        logging.info(action)

        # Continue Action
        # ***************
        if isinstance(action, ContinueAction):
            node = self.interceptor(env.get_node(action.id))
            assert node is not None, f"no node found with id {action.id}"

            node_ref = NodeRef(env.group, state.reference.process_id, action.id, str(uuid.uuid4()), str(uuid.uuid4()))
            new_state = state.with_reference(node_ref)

            # execute all present boundary events in order to register their events
            [self._handle_action(ContinueAction(e.id), state, env) for e in env.get_boundary_events(node.id)]

            [x.before_node_execution(node) for x in self.listeners]
            new_state, next_actions = node.execute(new_state, env)
            [x.after_node_execution(node) for x in self.listeners]

            return flatten([self._handle_action(action, new_state, env) for action in next_actions])

        # Complete Action
        # ***************
        elif isinstance(action, CompleteAction):
            # remove all registered boundary events from the completed node
            for event in env.get_boundary_events(action.id):
                self._handle_action(DequeueAction(event.attached_to_ref), state, env)

            if action.save_state:
                self.process_store.write_state(state)

            if action.consume_token:
                return [state]

            return []

        # Queue Action
        # ************
        elif isinstance(action, QueueAction):
            if action.save_state:
                self.process_store.write_state(state)

            if action.event is not None:
                # register an event subscription to get ready for an ResumeAction
                self.event_registry.create_subscription(action.event, state.reference, action.consumable)
                # return the state as the intermediate result of the process
                return [state]

            return []

        # Dequeue Action
        # ************
        elif isinstance(action, DequeueAction):
            self.event_registry.delete_subscription(action.event, state.reference)

            return []

        # Cascade Action
        # **************
        elif isinstance(action, CascadeAction):
            event = NoneEvent(env.group, action.process_id)
            subscription = first(self.event_registry.get_subscriptions(event))

            process = self.process_store.read_process(ProcessRef(event.group, subscription.process_id))
            new_state = State(action.init_state, subscription, False, action.parent_reference)
            new_environment = Environment(event.group, process, self.factories)

            new_state = first(self._handle_action(ContinueAction(subscription.node_id), new_state, new_environment))
            return self._handle_action(ResumeAction(new_state.parent_reference), new_state, env)

        # Resume Action
        # *************
        elif isinstance(action, ResumeAction):
            _env = env
            if action.reference.process_id != env.process_id:
                parent_process = self.process_store.read_process(ProcessRef(env.group, action.reference.process_id))
                _env = Environment(env.group, parent_process, self.factories)

            node = _env.get_node(action.reference.node_id)
            assert node is not None, f"no node found with id {action.reference.node_id}"

            [x.before_node_execution(node) for x in self.listeners]
            new_state, next_actions = node.execute(state.with_is_reentry(True), _env)
            [x.after_node_execution(node) for x in self.listeners]

            return flatten([self._handle_action(action, new_state, env) for action in next_actions])

        # Incident Action
        # ***************
        elif isinstance(action, IncidentAction):
            self.incident_handler.handle(action)
            return []

        # Event Action
        # ************
        elif isinstance(action, EventAction):
            next_actions = self.event_emitter.emit(action.event, self.event_registry)
            return flatten([self._handle_action(action, state, env) for action in next_actions])

        else:
            raise ValueError("cannot handle action " + str(action))
