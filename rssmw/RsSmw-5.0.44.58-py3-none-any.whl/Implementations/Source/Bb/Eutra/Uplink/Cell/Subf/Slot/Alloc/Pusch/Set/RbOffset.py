from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RbOffset:
	"""RbOffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rbOffset", core, parent)

	def get(self, cellNull=repcap.CellNull.Default, subframeNull=repcap.SubframeNull.Default, slotNull=repcap.SlotNull.Default, allocationNull=repcap.AllocationNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:[CELL<CCIDX>]:[SUBF<ST0>]:SLOT<USER0>:ALLoc<CH0>:PUSCh:SET:RBOFfset \n
		Snippet: value: int = driver.source.bb.eutra.uplink.cell.subf.slot.alloc.pusch.set.rbOffset.get(cellNull = repcap.CellNull.Default, subframeNull = repcap.SubframeNull.Default, slotNull = repcap.SlotNull.Default, allocationNull = repcap.AllocationNull.Default) \n
		Queries the start resource block of the selected allocation in slot n of the subframe. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param slotNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: rb_offset: integer Range: 0 to 49"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		slotNull_cmd_val = self._cmd_group.get_repcap_cmd_value(slotNull, repcap.SlotNull)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:CELL{cellNull_cmd_val}:SUBF{subframeNull_cmd_val}:SLOT{slotNull_cmd_val}:ALLoc{allocationNull_cmd_val}:PUSCh:SET:RBOFfset?')
		return Conversions.str_to_int(response)
