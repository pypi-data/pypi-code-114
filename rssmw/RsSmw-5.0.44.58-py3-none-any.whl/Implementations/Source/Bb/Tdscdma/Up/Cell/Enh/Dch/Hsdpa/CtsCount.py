from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CtsCount:
	"""CtsCount commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ctsCount", core, parent)

	def set(self, cts_count: int, cell=repcap.Cell.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:ENH:DCH:HSDPA:CTSCount \n
		Snippet: driver.source.bb.tdscdma.up.cell.enh.dch.hsdpa.ctsCount.set(cts_count = 1, cell = repcap.Cell.Default) \n
		Sets the number of physical channels per timeslot. \n
			:param cts_count: integer Range: 1 to 14
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
		"""
		param = Conversions.decimal_value_to_str(cts_count)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:ENH:DCH:HSDPA:CTSCount {param}')

	def get(self, cell=repcap.Cell.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:ENH:DCH:HSDPA:CTSCount \n
		Snippet: value: int = driver.source.bb.tdscdma.up.cell.enh.dch.hsdpa.ctsCount.get(cell = repcap.Cell.Default) \n
		Sets the number of physical channels per timeslot. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:return: cts_count: integer Range: 1 to 14"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:ENH:DCH:HSDPA:CTSCount?')
		return Conversions.str_to_int(response)
