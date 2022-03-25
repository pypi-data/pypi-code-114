import json
from abc import abstractmethod
from typing import Optional

from confluent_kafka import TIMESTAMP_NOT_AVAILABLE

from .logger import init_logger
from .config import KAFKA_SERVER_URL
from .machine_topics import MACHINE_INPUT_TOPIC
from .service import Service
from .event_utls.consumer_decorator import consume
from .message import Headers
from .simple_service_message import SimpleServiceMessage
from .topics import AGENT_EVENTS, RECONFIG_TOPIC, SERVICE_INPUT_TOPIC
from .machine_topics import MACHINE_EVENTS
from .simulation.update_message_types import *
from .agent_result_message import AgentResultMessage
from .adapter.MsgBusWriter import MessageBusWriter

_logger = init_logger(__name__)


class CallbackList():
    def __init__(self):
        self.callbacks = {}
        self.released_id_pool = []
        self.count = 0

    @staticmethod
    def is_callback_id(p_id):
        return len(p_id.split('/')) > 1

    def add(self, func, p_id) -> str:
        _logger.debug("register new callback function")
        if len(self.released_id_pool) > 0:
            gen_p_id = self.released_id_pool.pop()
        else:
            gen_p_id = str(self.count)
            self.count += 1
        new_p_id = p_id + "/" + str(gen_p_id)
        self.callbacks[new_p_id] = func
        return new_p_id

    def pop(self, p_id):
        callback = self.callbacks.get(p_id)
        if callback is not None:
            self.released_id_pool.append(int(p_id.split('/')[-1]))
            return self.callbacks.pop(p_id)

    def is_empty(self):
        return len(self.callbacks) == 0


class SimpleService(Service):
    def __init__(self, name, read, write=None):
        super().__init__(name)
        self.write_hook = MessageBusWriter() if write is None else write
        self.read_hook = read
        self.current_package_id = None
        self.callback_list = CallbackList()

    @abstractmethod
    def proposal(self, params: Optional[dict]):
        """[summary]
        Function that will be called when the Agent is triggered.
        :param params: Optional parameter for configuration or setting internal parameter 
        :type params: Optional[dict]
        :return: A tuple consisting of a dictionary which is containing the result of the Agent that will be stored, 
        an error code and and error message. All parameter are optional and can be set to None if not needed.
        :rtype: Optional[Tuple[dict, int, str]]
        """
        pass

    def write(self, channel, device, _property, **kwargs):
        if self.write_hook is None:
            raise KeyError("write hook isn't set.")
        # pass message internal parameter
        callback = kwargs.get('callback')
        if callback is not None:
            kwargs['package_id'] = self.callback_list.add(callback, self.current_package_id)
            kwargs.pop('callback')  # functions are not serializable
        else:
            kwargs['package_id'] = self.current_package_id
        kwargs['service_type'] = self.type
        return self.write_hook(channel, device, _property, **kwargs)

    def read(self, channel, device, _property, **kwargs):
        if self.read_hook is None:
            raise KeyError("read_hook isn't set.")
        return self.read_hook(channel, device, _property, **kwargs)

    def publish_results(self, res: AgentResultMessage):
        self.producer.async_produce(AGENT_EVENTS, res.serialize(),
                                    Headers(package_id=self.current_package_id, source=self.type, msg_type=self.type))

    def reconfig_event(self, msg):
        """[summary]
        Function that can be overloaded by the concret service to reconfig without restarting
        :param msg: [description]
        :type msg: [type]
        """
        pass

    def _does_local_storage_exists(self):
        # ToDo: Not implemented yet
        return False

    @consume([SERVICE_INPUT_TOPIC, MACHINE_EVENTS, RECONFIG_TOPIC], KAFKA_SERVER_URL)
    def service_input_handler(self, msg, **kwargs):
        timestamp_type, timestamp = msg.timestamp()
        if timestamp_type == TIMESTAMP_NOT_AVAILABLE:
            _logger.debug(f"[{self.name}] receive a message without a timestamp")
            return
        headers = Headers.from_kafka_headers(msg.headers())
        self.current_package_id = headers.package_id
        #self.machine_adapter.active_package_id = headers.package_id
        _logger.debug(f'[{self.name}] call service_input_handler receive headers: {str(headers)} group_id: {",".join([t.group_id for t in self.thread_pool])}')
        _logger.debug(f"Received message from topic '{msg.topic()}'")
        if msg.topic() == MACHINE_EVENTS:
            _logger.debug(f"machine event topic called... p_id: {self.current_package_id}")
            _logger.debug(f"{self.callback_list.callbacks}")
            callback = self.callback_list.pop(self.current_package_id)
            if callback is not None:
                callback()
                _logger.debug(f"callback finished. p_id: {self.current_package_id}")
                if self.callback_list.is_empty():
                    data = SetMachineMessage(is_last_message=True, write_commands=[])
                    self.producer.sync_produce(MACHINE_INPUT_TOPIC, data.serialize(), Headers(package_id=self.current_package_id.split('/')[0], source=self.type, msg_type=self.type))
                    _logger.debug("send last message.")

        if headers.is_message_for(self.type) or headers.is_message_for(self.name):
            if msg.topic() == SERVICE_INPUT_TOPIC:
                data = SimpleServiceMessage.deserialize([msg])
                result = self.proposal(data.params)
                # store message
                if result != None:
                    agent_result, error_code, error_message = result
                    if self._does_local_storage_exists():
                        # TODO: store the agent_result in local db and set agent_result to db url
                        pass
                    self.producer.async_produce(AGENT_EVENTS, AgentResultMessage(agent_result, error_message, error_code).serialize(),
                                                Headers(package_id=self.current_package_id, source=self.type, msg_type=self.type))
                    _logger.debug(f"send result message to topic '{AGENT_EVENTS}'")
                if self.callback_list.is_empty():
                    data = SetMachineMessage(is_last_message=True, write_commands=[])
                    self.producer.sync_produce(MACHINE_INPUT_TOPIC, data.serialize(), Headers(package_id=self.current_package_id, source=self.type, msg_type=self.type))
                    _logger.debug("send last message.")

            elif msg.topic() == RECONFIG_TOPIC:
                _logger.debug(f"reconfig message received")
                self.reconfig_event(json.loads(msg.value().decode('utf-8')))
                return
            _logger.debug(f"Is it empty: {self.callback_list.is_empty()} {self.callback_list.callbacks}")

        _logger.debug(f'[{self.name}] end service_input_handler')
