from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PointA:
	"""PointA commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pointA", core, parent)

	def set(self, lte_offs_to_point_a: int, cellNull=repcap.CellNull.Nr0, patternNull=repcap.PatternNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:LTE:PATT<ST0>:POINta \n
		Snippet: driver.source.bb.nr5G.node.cell.lte.patt.pointA.set(lte_offs_to_point_a = 1, cellNull = repcap.CellNull.Nr0, patternNull = repcap.PatternNull.Default) \n
		Defines an LTE carrier offset relative to reference point A (in terms of resource blocks) .
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on LTE-CRS coexistence ([:SOURce<hw>]:BB:NR5G:NODE:CELL<ch0>:LTE:STATe) . \n
			:param lte_offs_to_point_a: integer Range: 0 to 30300
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:param patternNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Patt')
		"""
		param = Conversions.decimal_value_to_str(lte_offs_to_point_a)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		patternNull_cmd_val = self._cmd_group.get_repcap_cmd_value(patternNull, repcap.PatternNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:LTE:PATT{patternNull_cmd_val}:POINta {param}')

	def get(self, cellNull=repcap.CellNull.Nr0, patternNull=repcap.PatternNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:LTE:PATT<ST0>:POINta \n
		Snippet: value: int = driver.source.bb.nr5G.node.cell.lte.patt.pointA.get(cellNull = repcap.CellNull.Nr0, patternNull = repcap.PatternNull.Default) \n
		Defines an LTE carrier offset relative to reference point A (in terms of resource blocks) .
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on LTE-CRS coexistence ([:SOURce<hw>]:BB:NR5G:NODE:CELL<ch0>:LTE:STATe) . \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:param patternNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Patt')
			:return: lte_offs_to_point_a: No help available"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		patternNull_cmd_val = self._cmd_group.get_repcap_cmd_value(patternNull, repcap.PatternNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:LTE:PATT{patternNull_cmd_val}:POINta?')
		return Conversions.str_to_int(response)
