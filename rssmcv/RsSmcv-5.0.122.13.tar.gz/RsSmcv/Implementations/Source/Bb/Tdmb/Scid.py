from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scid:
	"""Scid commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: SubChannel, default value after init: SubChannel.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scid", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_subChannel_get', 'repcap_subChannel_set', repcap.SubChannel.Nr1)

	def repcap_subChannel_set(self, subChannel: repcap.SubChannel) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to SubChannel.Default
		Default value after init: SubChannel.Nr1"""
		self._cmd_group.set_repcap_enum_value(subChannel)

	def repcap_subChannel_get(self) -> repcap.SubChannel:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def get(self, subChannel=repcap.SubChannel.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:TDMB:SCID<CH> \n
		Snippet: value: int = driver.source.bb.tdmb.scid.get(subChannel = repcap.SubChannel.Default) \n
		Queries the subchannel identifiers per subchannel. \n
			:param subChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Scid')
			:return: sub_channel_id: integer Range: 0 to 63"""
		subChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(subChannel, repcap.SubChannel)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDMB:SCID{subChannel_cmd_val}?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'Scid':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Scid(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
