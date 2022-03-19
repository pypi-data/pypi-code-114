from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mshift:
	"""Mshift commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mshift", core, parent)

	def get(self, cell=repcap.Cell.Default, slotNull=repcap.SlotNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:SLOT<CH0>:PRAC:MSG:MSHift \n
		Snippet: value: int = driver.source.bb.tdscdma.up.cell.slot.prac.msg.mshift.get(cell = repcap.Cell.Default, slotNull = repcap.SlotNull.Default) \n
		Queries the value of the midamble shift. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:param slotNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:return: mshift: integer Range: 0 to 128"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		slotNull_cmd_val = self._cmd_group.get_repcap_cmd_value(slotNull, repcap.SlotNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:SLOT{slotNull_cmd_val}:PRAC:MSG:MSHift?')
		return Conversions.str_to_int(response)
