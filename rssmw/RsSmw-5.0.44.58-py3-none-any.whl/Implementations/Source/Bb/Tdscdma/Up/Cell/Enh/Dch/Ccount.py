from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ccount:
	"""Ccount commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ccount", core, parent)

	def set(self, ccount: int, cell=repcap.Cell.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:ENH:DCH:CCOunt \n
		Snippet: driver.source.bb.tdscdma.up.cell.enh.dch.ccount.set(ccount = 1, cell = repcap.Cell.Default) \n
		Sets the number of channels to be used.
		The number of timeslots is set with the command BB:TDSC:DOWN|UP:CELL1:ENH:DCH:TSCount. \n
			:param ccount: integer Range: 1 to 16
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
		"""
		param = Conversions.decimal_value_to_str(ccount)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:ENH:DCH:CCOunt {param}')

	def get(self, cell=repcap.Cell.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:ENH:DCH:CCOunt \n
		Snippet: value: int = driver.source.bb.tdscdma.up.cell.enh.dch.ccount.get(cell = repcap.Cell.Default) \n
		Sets the number of channels to be used.
		The number of timeslots is set with the command BB:TDSC:DOWN|UP:CELL1:ENH:DCH:TSCount. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:return: ccount: integer Range: 1 to 16"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:ENH:DCH:CCOunt?')
		return Conversions.str_to_int(response)
