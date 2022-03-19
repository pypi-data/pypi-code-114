from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NcbTti:
	"""NcbTti commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ncbTti", core, parent)

	def get(self, cell=repcap.Cell.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:ENH:DCH:HSUPA:NCBTti \n
		Snippet: value: int = driver.source.bb.tdscdma.down.cell.enh.dch.hsupa.ncbTti.get(cell = repcap.Cell.Default) \n
		Queries the number of bits after coding. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:return: ncb_tti: integer"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:ENH:DCH:HSUPA:NCBTti?')
		return Conversions.str_to_int(response)
