from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RbCount:
	"""RbCount commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rbCount", core, parent)

	def set(self, number_of_rbs: int, cellNull=repcap.CellNull.Default, subframeNull=repcap.SubframeNull.Default, allocationNull=repcap.AllocationNull.Default, setItem=repcap.SetItem.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:[CELL<CCIDX>]:[SUBF<ST0>]:ALLoc<CH0>:PUACh:SET<USER>:RBCount \n
		Snippet: driver.source.bb.oneweb.uplink.cell.subf.alloc.puach.set.rbCount.set(number_of_rbs = 1, cellNull = repcap.CellNull.Default, subframeNull = repcap.SubframeNull.Default, allocationNull = repcap.AllocationNull.Default, setItem = repcap.SetItem.Default) \n
		Sets the size of the selected allocation in resource blocks (per subframe) . \n
			:param number_of_rbs: integer Range: 0 to 110
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:param setItem: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Set')
		"""
		param = Conversions.decimal_value_to_str(number_of_rbs)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		setItem_cmd_val = self._cmd_group.get_repcap_cmd_value(setItem, repcap.SetItem)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:UL:CELL{cellNull_cmd_val}:SUBF{subframeNull_cmd_val}:ALLoc{allocationNull_cmd_val}:PUACh:SET{setItem_cmd_val}:RBCount {param}')

	def get(self, cellNull=repcap.CellNull.Default, subframeNull=repcap.SubframeNull.Default, allocationNull=repcap.AllocationNull.Default, setItem=repcap.SetItem.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:[CELL<CCIDX>]:[SUBF<ST0>]:ALLoc<CH0>:PUACh:SET<USER>:RBCount \n
		Snippet: value: int = driver.source.bb.oneweb.uplink.cell.subf.alloc.puach.set.rbCount.get(cellNull = repcap.CellNull.Default, subframeNull = repcap.SubframeNull.Default, allocationNull = repcap.AllocationNull.Default, setItem = repcap.SetItem.Default) \n
		Sets the size of the selected allocation in resource blocks (per subframe) . \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:param setItem: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Set')
			:return: number_of_rbs: integer Range: 0 to 110"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		setItem_cmd_val = self._cmd_group.get_repcap_cmd_value(setItem, repcap.SetItem)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ONEWeb:UL:CELL{cellNull_cmd_val}:SUBF{subframeNull_cmd_val}:ALLoc{allocationNull_cmd_val}:PUACh:SET{setItem_cmd_val}:RBCount?')
		return Conversions.str_to_int(response)
