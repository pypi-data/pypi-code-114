from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Npat:
	"""Npat commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("npat", core, parent)

	def set(self, lte_crs_num_pat: int, cellNull=repcap.CellNull.Nr0) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:LTE:NPAT \n
		Snippet: driver.source.bb.nr5G.node.cell.lte.npat.set(lte_crs_num_pat = 1, cellNull = repcap.CellNull.Nr0) \n
		Defines the number of LTE cell specific reference signals in the resource grid. \n
			:param lte_crs_num_pat: integer Range: 1 to 4
			:param cellNull: optional repeated capability selector. Default value: Nr0
		"""
		param = Conversions.decimal_value_to_str(lte_crs_num_pat)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:LTE:NPAT {param}')

	def get(self, cellNull=repcap.CellNull.Nr0) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:LTE:NPAT \n
		Snippet: value: int = driver.source.bb.nr5G.node.cell.lte.npat.get(cellNull = repcap.CellNull.Nr0) \n
		Defines the number of LTE cell specific reference signals in the resource grid. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:return: lte_crs_num_pat: No help available"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:LTE:NPAT?')
		return Conversions.str_to_int(response)
