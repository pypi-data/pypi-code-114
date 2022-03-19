from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Priority:
	"""Priority commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("priority", core, parent)

	def set(self, priority: enums.PowSensDisplayPriority, channel=repcap.Channel.Default) -> None:
		"""SCPI: SENSe<CH>:[POWer]:DISPlay:PERManent:PRIority \n
		Snippet: driver.sense.power.display.permanent.priority.set(priority = enums.PowSensDisplayPriority.AVERage, channel = repcap.Channel.Default) \n
		Selects average or peak power for permanent display. \n
			:param priority: AVERage| PEAK
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sense')
		"""
		param = Conversions.enum_scalar_to_str(priority, enums.PowSensDisplayPriority)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		self._core.io.write(f'SENSe{channel_cmd_val}:POWer:DISPlay:PERManent:PRIority {param}')

	# noinspection PyTypeChecker
	def get(self, channel=repcap.Channel.Default) -> enums.PowSensDisplayPriority:
		"""SCPI: SENSe<CH>:[POWer]:DISPlay:PERManent:PRIority \n
		Snippet: value: enums.PowSensDisplayPriority = driver.sense.power.display.permanent.priority.get(channel = repcap.Channel.Default) \n
		Selects average or peak power for permanent display. \n
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sense')
			:return: priority: AVERage| PEAK"""
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		response = self._core.io.query_str(f'SENSe{channel_cmd_val}:POWer:DISPlay:PERManent:PRIority?')
		return Conversions.str_to_scalar_enum(response, enums.PowSensDisplayPriority)
