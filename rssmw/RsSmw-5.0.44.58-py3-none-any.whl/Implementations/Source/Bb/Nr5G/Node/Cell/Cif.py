from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cif:
	"""Cif commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cif", core, parent)

	def set(self, cif: enums.CifAll, cellNull=repcap.CellNull.Nr0) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:CIF \n
		Snippet: driver.source.bb.nr5G.node.cell.cif.set(cif = enums.CifAll._0, cellNull = repcap.CellNull.Nr0) \n
		Queries the value of the carrier indicator field (CIF) . \n
			:param cif: 0| 1| 2| 3| 4| 5| 6| 7
			:param cellNull: optional repeated capability selector. Default value: Nr0
		"""
		param = Conversions.enum_scalar_to_str(cif, enums.CifAll)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:CIF {param}')

	# noinspection PyTypeChecker
	def get(self, cellNull=repcap.CellNull.Nr0) -> enums.CifAll:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:CIF \n
		Snippet: value: enums.CifAll = driver.source.bb.nr5G.node.cell.cif.get(cellNull = repcap.CellNull.Nr0) \n
		Queries the value of the carrier indicator field (CIF) . \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:return: cif: 0| 1| 2| 3| 4| 5| 6| 7"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:CIF?')
		return Conversions.str_to_scalar_enum(response, enums.CifAll)
