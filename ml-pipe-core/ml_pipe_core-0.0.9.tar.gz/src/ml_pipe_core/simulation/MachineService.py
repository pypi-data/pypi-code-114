from typing import List, Dict

from confluent_kafka import TIMESTAMP_NOT_AVAILABLE

from ..service import Service
from ..logger import init_logger
from ..adapter.PetraAdapter import PetraAdapter
from ..machine_topics import MACHINE_EVENTS, MACHINE_INPUT_TOPIC
from ..message import Headers
from ..config import KAFKA_SERVER_URL
from ..simulation.update_message_types import SetMachineMessage, UpdateMessage
from ..event_utls.consumer_decorator import consume
from ..simple_service import CallbackList

_logger = init_logger(__name__)


class MachineService(Service):
    def __init__(self, name, write, read):
        super().__init__(name)
        self.category = 'Simulation'
        self.write = write
        self.read = read
        self.updated_devices: Dict[int, List[List[str]]] = {}

    def _are_keys_in_dict(self, keys: List[str], dict):
        for key in keys:
            if key not in dict:
                return False
        return True

    def simulate(self):
        pass

    @consume([MACHINE_INPUT_TOPIC], KAFKA_SERVER_URL)
    def machine_input_handler(self, msg, **kwargs):
        timestamp_type, timestamp = msg.timestamp()
        if timestamp_type == TIMESTAMP_NOT_AVAILABLE:
            _logger.debug(f"[{self.name}] receive a message without a timestamp")
            return
        headers = Headers.from_kafka_headers(msg.headers())
        received_package_id = headers.package_id
        _logger.debug(f'[{self.name}] call machine_input_handler receive headers: {str(headers)} group_id: {",".join([t.group_id for t in self.thread_pool])}')
        # if headers.is_message_for(self.type) or headers.is_message_for(self.name):

        message = SetMachineMessage.deserialize([msg])
        if message.is_last_message or CallbackList.is_callback_id(received_package_id):
            updated_device_lists = self.updated_devices.get(received_package_id, [])
            _logger.debug(f"publish a event id: {received_package_id}.")
            self.updated_event(package_id=received_package_id,
                               msg=UpdateMessage(source=headers.msg_type, updated=updated_device_lists))
            if len(updated_device_lists) > 0:
                self.updated_devices.pop(received_package_id)
        else:
            _updated_devices = []
            for write_command in message.write_commands:
                self.write(write_command.channel, write_command.device_name, write_command.property, **write_command.params)
                _updated_devices.append(f"{write_command.channel}/{write_command.device_name}")
            self.simulate()
            if self.updated_devices.get(received_package_id) is None:
                self.updated_devices[received_package_id] = [_updated_devices]
            else:
                self.updated_devices[received_package_id].append(_updated_devices)
            # updated event
            # self.updated_event(package_id=received_package_id,
            #                    msg=UpdateMessage(source=headers.msg_type, updated=updated_devices))
        _logger.debug(f"[{self.name}] end machine_input_handler")

    def updated_event(self, package_id, msg):
        self.producer.sync_produce(MACHINE_EVENTS, msg.serialize(), Headers(package_id=package_id, source=self.type))
