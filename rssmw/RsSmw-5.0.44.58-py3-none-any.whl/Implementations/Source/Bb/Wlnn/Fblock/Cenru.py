from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cenru:
	"""Cenru commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Index, default value after init: Index.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cenru", core, parent)
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

	def set(self, center_26_tone_ru: bool, frameBlock=repcap.FrameBlock.Default, index=repcap.Index.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:CENRu<ST> \n
		Snippet: driver.source.bb.wlnn.fblock.cenru.set(center_26_tone_ru = False, frameBlock = repcap.FrameBlock.Default, index = repcap.Index.Default) \n
		For full bandwidth 80 MHz: if enabled, indicates that center 26 -tone RU is allocated in the common block fields of both
		SIGB content channels with same value. For full bandwidth 160/80+80 MHz: if enabled, indicates that center 26 -tone RU is
		allocated for one individual 80 MHz in Common Block fields of both SIGB content channels. \n
			:param center_26_tone_ru: OFF| ON| 1| 0
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cenru')
		"""
		param = Conversions.bool_to_str(center_26_tone_ru)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:CENRu{index_cmd_val} {param}')

	def get(self, frameBlock=repcap.FrameBlock.Default, index=repcap.Index.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:CENRu<ST> \n
		Snippet: value: bool = driver.source.bb.wlnn.fblock.cenru.get(frameBlock = repcap.FrameBlock.Default, index = repcap.Index.Default) \n
		For full bandwidth 80 MHz: if enabled, indicates that center 26 -tone RU is allocated in the common block fields of both
		SIGB content channels with same value. For full bandwidth 160/80+80 MHz: if enabled, indicates that center 26 -tone RU is
		allocated for one individual 80 MHz in Common Block fields of both SIGB content channels. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cenru')
			:return: center_26_tone_ru: OFF| ON| 1| 0"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:CENRu{index_cmd_val}?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'Cenru':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cenru(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
