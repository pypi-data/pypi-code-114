from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SpareUse:
	"""SpareUse commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Index, default value after init: Index.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spareUse", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_index_get', 'repcap_index_set', repcap.Index.Nr1)

	def repcap_index_set(self, index: repcap.Index) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Index.Default
		Default value after init: Index.Nr1"""
		self._cmd_group.set_repcap_enum_value(index)

	def repcap_index_get(self) -> repcap.Index:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, spatial_reuse: int, frameBlock=repcap.FrameBlock.Default, index=repcap.Index.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:SPAReuse<ST> \n
		Snippet: driver.source.bb.wlnn.fblock.spareUse.set(spatial_reuse = 1, frameBlock = repcap.FrameBlock.Default, index = repcap.Index.Default) \n
		Indicates if the spatial reuse is allowed (value is ≠0) or not (value is 0) . \n
			:param spatial_reuse: integer Range: 0 to 15
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'SpareUse')
		"""
		param = Conversions.decimal_value_to_str(spatial_reuse)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:SPAReuse{index_cmd_val} {param}')

	def get(self, frameBlock=repcap.FrameBlock.Default, index=repcap.Index.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:SPAReuse<ST> \n
		Snippet: value: int = driver.source.bb.wlnn.fblock.spareUse.get(frameBlock = repcap.FrameBlock.Default, index = repcap.Index.Default) \n
		Indicates if the spatial reuse is allowed (value is ≠0) or not (value is 0) . \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'SpareUse')
			:return: spatial_reuse: integer Range: 0 to 15"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:SPAReuse{index_cmd_val}?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'SpareUse':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SpareUse(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
