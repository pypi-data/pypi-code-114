from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tdelay:
	"""Tdelay commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tdelay", core, parent)

	def set(self, tdelay: int, cell=repcap.Cell.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:TDELay \n
		Snippet: driver.source.bb.tdscdma.down.cell.tdelay.set(tdelay = 1, cell = repcap.Cell.Default) \n
		Sets the time shift of the selected cell compared to cell 1; the time delay of cell 1 is 0. \n
			:param tdelay: integer Range: 0 to 19200, Unit: chip
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
		"""
		param = Conversions.decimal_value_to_str(tdelay)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:TDELay {param}')

	def get(self, cell=repcap.Cell.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:TDELay \n
		Snippet: value: int = driver.source.bb.tdscdma.down.cell.tdelay.get(cell = repcap.Cell.Default) \n
		Sets the time shift of the selected cell compared to cell 1; the time delay of cell 1 is 0. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:return: tdelay: integer Range: 0 to 19200, Unit: chip"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:TDELay?')
		return Conversions.str_to_int(response)
