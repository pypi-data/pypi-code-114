from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, puac_state: bool, cellNull=repcap.CellNull.Default, subframeNull=repcap.SubframeNull.Default, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:[CELL<CCIDX>]:[SUBF<ST0>]:ALLoc<CH0>:PUACh:STATe \n
		Snippet: driver.source.bb.oneweb.uplink.cell.subf.alloc.puach.state.set(puac_state = False, cellNull = repcap.CellNull.Default, subframeNull = repcap.SubframeNull.Default, allocationNull = repcap.AllocationNull.Default) \n
		Sets the allocation state to active or inactive. Note: Disabling an allocation deactivate the PUACH/PUSCH/PUCCH and the
		corresponding demodulation reference signal, but does not affect other allocations of the UE or the sounding reference
		signal. \n
			:param puac_state: 0| 1| OFF| ON
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.bool_to_str(puac_state)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:UL:CELL{cellNull_cmd_val}:SUBF{subframeNull_cmd_val}:ALLoc{allocationNull_cmd_val}:PUACh:STATe {param}')

	def get(self, cellNull=repcap.CellNull.Default, subframeNull=repcap.SubframeNull.Default, allocationNull=repcap.AllocationNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:[CELL<CCIDX>]:[SUBF<ST0>]:ALLoc<CH0>:PUACh:STATe \n
		Snippet: value: bool = driver.source.bb.oneweb.uplink.cell.subf.alloc.puach.state.get(cellNull = repcap.CellNull.Default, subframeNull = repcap.SubframeNull.Default, allocationNull = repcap.AllocationNull.Default) \n
		Sets the allocation state to active or inactive. Note: Disabling an allocation deactivate the PUACH/PUSCH/PUCCH and the
		corresponding demodulation reference signal, but does not affect other allocations of the UE or the sounding reference
		signal. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: puac_state: No help available"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ONEWeb:UL:CELL{cellNull_cmd_val}:SUBF{subframeNull_cmd_val}:ALLoc{allocationNull_cmd_val}:PUACh:STATe?')
		return Conversions.str_to_bool(response)
