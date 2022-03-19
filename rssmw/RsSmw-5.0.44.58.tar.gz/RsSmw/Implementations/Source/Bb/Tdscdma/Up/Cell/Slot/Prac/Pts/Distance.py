from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Distance:
	"""Distance commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("distance", core, parent)

	def set(self, distance: int, cell=repcap.Cell.Default, slotNull=repcap.SlotNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:SLOT<CH0>:PRAC:PTS:DISTance \n
		Snippet: driver.source.bb.tdscdma.up.cell.slot.prac.pts.distance.set(distance = 1, cell = repcap.Cell.Default, slotNull = repcap.SlotNull.Default) \n
		Sets the value to vary the timing between UpPTS and RACH. \n
			:param distance: integer Range: 1 to 4
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:param slotNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
		"""
		param = Conversions.decimal_value_to_str(distance)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		slotNull_cmd_val = self._cmd_group.get_repcap_cmd_value(slotNull, repcap.SlotNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:SLOT{slotNull_cmd_val}:PRAC:PTS:DISTance {param}')

	def get(self, cell=repcap.Cell.Default, slotNull=repcap.SlotNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:SLOT<CH0>:PRAC:PTS:DISTance \n
		Snippet: value: int = driver.source.bb.tdscdma.up.cell.slot.prac.pts.distance.get(cell = repcap.Cell.Default, slotNull = repcap.SlotNull.Default) \n
		Sets the value to vary the timing between UpPTS and RACH. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:param slotNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:return: distance: integer Range: 1 to 4"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		slotNull_cmd_val = self._cmd_group.get_repcap_cmd_value(slotNull, repcap.SlotNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:SLOT{slotNull_cmd_val}:PRAC:PTS:DISTance?')
		return Conversions.str_to_int(response)
