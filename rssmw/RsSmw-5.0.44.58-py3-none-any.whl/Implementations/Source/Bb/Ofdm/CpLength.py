from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CpLength:
	"""CpLength commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Channel, default value after init: Channel.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cpLength", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_channel_get', 'repcap_channel_set', repcap.Channel.Nr1)

	def repcap_channel_set(self, channel: repcap.Channel) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Channel.Default
		Default value after init: Channel.Nr1"""
		self._cmd_group.set_repcap_enum_value(channel)

	def repcap_channel_get(self) -> repcap.Channel:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, cp_length: int, channel=repcap.Channel.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:CPLength<CH> \n
		Snippet: driver.source.bb.ofdm.cpLength.set(cp_length = 1, channel = repcap.Channel.Default) \n
		Sets the cyclic prefix length as number of samples. \n
			:param cp_length: integer Range: 0 to 8192
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'CpLength')
		"""
		param = Conversions.decimal_value_to_str(cp_length)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:CPLength{channel_cmd_val} {param}')

	def get(self, channel=repcap.Channel.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:OFDM:CPLength<CH> \n
		Snippet: value: int = driver.source.bb.ofdm.cpLength.get(channel = repcap.Channel.Default) \n
		Sets the cyclic prefix length as number of samples. \n
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'CpLength')
			:return: cp_length: integer Range: 0 to 8192"""
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:OFDM:CPLength{channel_cmd_val}?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'CpLength':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CpLength(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
