from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TsCount:
	"""TsCount commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tsCount", core, parent)

	def set(self, ts_count: int, cell=repcap.Cell.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:ENH:DCH:HSUPA:TSCount \n
		Snippet: driver.source.bb.tdscdma.down.cell.enh.dch.hsupa.tsCount.set(ts_count = 1, cell = repcap.Cell.Default) \n
		Sets the number of timeslots. \n
			:param ts_count: integer Range: 2 to 5
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
		"""
		param = Conversions.decimal_value_to_str(ts_count)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:ENH:DCH:HSUPA:TSCount {param}')

	def get(self, cell=repcap.Cell.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:ENH:DCH:HSUPA:TSCount \n
		Snippet: value: int = driver.source.bb.tdscdma.down.cell.enh.dch.hsupa.tsCount.get(cell = repcap.Cell.Default) \n
		Sets the number of timeslots. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:return: ts_count: integer Range: 2 to 5"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:ENH:DCH:HSUPA:TSCount?')
		return Conversions.str_to_int(response)
