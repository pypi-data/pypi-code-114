from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Time:
	"""Time commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("time", core, parent)

	def set(self, ap_time: float, channel=repcap.Channel.Default) -> None:
		"""SCPI: SENSe<CH>:[POWer]:APERture:TIMe \n
		Snippet: driver.sense.power.aperture.time.set(ap_time = 1.0, channel = repcap.Channel.Default) \n
		Defines the aperture time (size of the acquisition interval) for the corresponding sensor. \n
			:param ap_time: float Range: depends on connected power sensor
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sense')
		"""
		param = Conversions.decimal_value_to_str(ap_time)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		self._core.io.write(f'SENSe{channel_cmd_val}:POWer:APERture:TIMe {param}')

	def get(self, channel=repcap.Channel.Default) -> float:
		"""SCPI: SENSe<CH>:[POWer]:APERture:TIMe \n
		Snippet: value: float = driver.sense.power.aperture.time.get(channel = repcap.Channel.Default) \n
		Defines the aperture time (size of the acquisition interval) for the corresponding sensor. \n
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sense')
			:return: ap_time: float Range: depends on connected power sensor"""
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		response = self._core.io.query_str(f'SENSe{channel_cmd_val}:POWer:APERture:TIMe?')
		return Conversions.str_to_float(response)
