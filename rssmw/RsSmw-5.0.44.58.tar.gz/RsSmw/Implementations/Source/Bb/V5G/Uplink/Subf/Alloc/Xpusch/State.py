from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, pusc_state: bool, subframeNull=repcap.SubframeNull.Default, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:SUBF<ST0>:ALLoc<CH0>:XPUSch:STATe \n
		Snippet: driver.source.bb.v5G.uplink.subf.alloc.xpusch.state.set(pusc_state = False, subframeNull = repcap.SubframeNull.Default, allocationNull = repcap.AllocationNull.Default) \n
		Sets the allocation state to active or inactive for the corresponding, including xPUSCH/xPUCCH and the corresponding
		reference signals. Note: Disabling an allocation does not affect other allocations of the UE. \n
			:param pusc_state: 1| ON| 0| OFF
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.bool_to_str(pusc_state)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:UL:SUBF{subframeNull_cmd_val}:ALLoc{allocationNull_cmd_val}:XPUSch:STATe {param}')

	def get(self, subframeNull=repcap.SubframeNull.Default, allocationNull=repcap.AllocationNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:SUBF<ST0>:ALLoc<CH0>:XPUSch:STATe \n
		Snippet: value: bool = driver.source.bb.v5G.uplink.subf.alloc.xpusch.state.get(subframeNull = repcap.SubframeNull.Default, allocationNull = repcap.AllocationNull.Default) \n
		Sets the allocation state to active or inactive for the corresponding, including xPUSCH/xPUCCH and the corresponding
		reference signals. Note: Disabling an allocation does not affect other allocations of the UE. \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: pusc_state: 1| ON| 0| OFF"""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:V5G:UL:SUBF{subframeNull_cmd_val}:ALLoc{allocationNull_cmd_val}:XPUSch:STATe?')
		return Conversions.str_to_bool(response)
