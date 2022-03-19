from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RuAllocation:
	"""RuAllocation commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Index, default value after init: Index.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ruAllocation", core, parent)
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

	def set(self, ru_allocation: enums.WlannFbPpduRuAlloc, frameBlock=repcap.FrameBlock.Default, index=repcap.Index.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:CCH1:RUALlocation<ST> \n
		Snippet: driver.source.bb.wlnn.fblock.cch1.ruAllocation.set(ru_allocation = enums.WlannFbPpduRuAlloc.RU0, frameBlock = repcap.FrameBlock.Default, index = repcap.Index.Default) \n
		For EHT frames. Sets the resource unit allocation of the first content channel for the respective channel and station. \n
			:param ru_allocation: RU0| RU1| RU2| RU3| RU4| RU5| RU6| RU7| RU8| RU9| RU10| RU11| RU12| RU13| RU14| RU15| RU16| RU17| RU18| RU19| RU20| RU21| RU22| RU23| RU24| RU25| RU26| RU27| RU28| RU29| RU30| RU31| RU32| RU33| RU34| RU35| RU36| RU37| RU38| RU39| RU40| RU41| RU42| RU43| RU44| RU45| RU46| RU47| RU48| RU49| RU50| RU51| RU52| RU53| RU54| RU55| RU56| RU57| RU58| RU59| RU60| RU61| RU62| RU63| RU64| RU65| RU66| RU67| RU68| RU69| RU70| RU71| RU72| RU73| RU74| RU75| RU76| RU77| RU78| RU79| RU80| RU81| RU82| RU83| RU84| RU85| RU86
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'RuAllocation')
		"""
		param = Conversions.enum_scalar_to_str(ru_allocation, enums.WlannFbPpduRuAlloc)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:CCH1:RUALlocation{index_cmd_val} {param}')

	# noinspection PyTypeChecker
	def get(self, frameBlock=repcap.FrameBlock.Default, index=repcap.Index.Default) -> enums.WlannFbPpduRuAlloc:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:CCH1:RUALlocation<ST> \n
		Snippet: value: enums.WlannFbPpduRuAlloc = driver.source.bb.wlnn.fblock.cch1.ruAllocation.get(frameBlock = repcap.FrameBlock.Default, index = repcap.Index.Default) \n
		For EHT frames. Sets the resource unit allocation of the first content channel for the respective channel and station. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'RuAllocation')
			:return: ru_allocation: RU0| RU1| RU2| RU3| RU4| RU5| RU6| RU7| RU8| RU9| RU10| RU11| RU12| RU13| RU14| RU15| RU16| RU17| RU18| RU19| RU20| RU21| RU22| RU23| RU24| RU25| RU26| RU27| RU28| RU29| RU30| RU31| RU32| RU33| RU34| RU35| RU36| RU37| RU38| RU39| RU40| RU41| RU42| RU43| RU44| RU45| RU46| RU47| RU48| RU49| RU50| RU51| RU52| RU53| RU54| RU55| RU56| RU57| RU58| RU59| RU60| RU61| RU62| RU63| RU64| RU65| RU66| RU67| RU68| RU69| RU70| RU71| RU72| RU73| RU74| RU75| RU76| RU77| RU78| RU79| RU80| RU81| RU82| RU83| RU84| RU85| RU86"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:CCH1:RUALlocation{index_cmd_val}?')
		return Conversions.str_to_scalar_enum(response, enums.WlannFbPpduRuAlloc)

	def clone(self) -> 'RuAllocation':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RuAllocation(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
