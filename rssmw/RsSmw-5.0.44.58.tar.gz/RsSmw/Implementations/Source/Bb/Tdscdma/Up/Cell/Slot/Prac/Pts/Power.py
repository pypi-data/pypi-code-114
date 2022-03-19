from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	def set(self, power: float, cell=repcap.Cell.Default, slotNull=repcap.SlotNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:SLOT<CH0>:PRAC:PTS:POWer \n
		Snippet: driver.source.bb.tdscdma.up.cell.slot.prac.pts.power.set(power = 1.0, cell = repcap.Cell.Default, slotNull = repcap.SlotNull.Default) \n
		Sets the power of the UpPTS. \n
			:param power: float Range: -80 to 0
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:param slotNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
		"""
		param = Conversions.decimal_value_to_str(power)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		slotNull_cmd_val = self._cmd_group.get_repcap_cmd_value(slotNull, repcap.SlotNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:SLOT{slotNull_cmd_val}:PRAC:PTS:POWer {param}')

	def get(self, cell=repcap.Cell.Default, slotNull=repcap.SlotNull.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:SLOT<CH0>:PRAC:PTS:POWer \n
		Snippet: value: float = driver.source.bb.tdscdma.up.cell.slot.prac.pts.power.get(cell = repcap.Cell.Default, slotNull = repcap.SlotNull.Default) \n
		Sets the power of the UpPTS. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:param slotNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:return: power: float Range: -80 to 0"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		slotNull_cmd_val = self._cmd_group.get_repcap_cmd_value(slotNull, repcap.SlotNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:SLOT{slotNull_cmd_val}:PRAC:PTS:POWer?')
		return Conversions.str_to_float(response)
