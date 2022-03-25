from ..simulation.update_message_types import WriteCommand, SetMachineMessage
from ..machine_topics import MACHINE_INPUT_TOPIC
from ..message import Headers
from ..logger import init_logger
from ..event_utls.producer import Producer

_logger = init_logger(__name__)


class MessageBusWriter:
    def __init__(self, producer=None):
        self.producer = Producer() if producer is None else producer

    def __call__(self, channel, device, _property, **kwargs):
        p_id = kwargs.get("package_id")
        s_type = kwargs.get("service_type")
        if p_id is None:
            _logger.error("package_id isn't set.")
            return
        if s_type is None:
            _logger.error("service_type isn't set.")
            return
        data = SetMachineMessage(is_last_message=False, write_commands=[WriteCommand(channel=channel, device_name=device, property=_property, params=kwargs)])
        self.producer.sync_produce(MACHINE_INPUT_TOPIC, data.serialize(), Headers(package_id=p_id, source=s_type, msg_type=s_type))
