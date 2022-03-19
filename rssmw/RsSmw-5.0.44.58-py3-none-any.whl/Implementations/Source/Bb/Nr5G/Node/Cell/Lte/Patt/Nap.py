from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nap:
	"""Nap commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nap", core, parent)

	def set(self, lte_antenna_ports: enums.NumberOfPorts, cellNull=repcap.CellNull.Nr0, patternNull=repcap.PatternNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:LTE:PATT<ST0>:NAP \n
		Snippet: driver.source.bb.nr5G.node.cell.lte.patt.nap.set(lte_antenna_ports = enums.NumberOfPorts.AP1, cellNull = repcap.CellNull.Nr0, patternNull = repcap.PatternNull.Default) \n
		Selects the number of antenna ports for an LTE signal.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on LTE-CRS coexistence ([:SOURce<hw>]:BB:NR5G:NODE:CELL<ch0>:LTE:STATe) . \n
			:param lte_antenna_ports: AP1| AP2| AP4
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:param patternNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Patt')
		"""
		param = Conversions.enum_scalar_to_str(lte_antenna_ports, enums.NumberOfPorts)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		patternNull_cmd_val = self._cmd_group.get_repcap_cmd_value(patternNull, repcap.PatternNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:LTE:PATT{patternNull_cmd_val}:NAP {param}')

	# noinspection PyTypeChecker
	def get(self, cellNull=repcap.CellNull.Nr0, patternNull=repcap.PatternNull.Default) -> enums.NumberOfPorts:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:LTE:PATT<ST0>:NAP \n
		Snippet: value: enums.NumberOfPorts = driver.source.bb.nr5G.node.cell.lte.patt.nap.get(cellNull = repcap.CellNull.Nr0, patternNull = repcap.PatternNull.Default) \n
		Selects the number of antenna ports for an LTE signal.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on LTE-CRS coexistence ([:SOURce<hw>]:BB:NR5G:NODE:CELL<ch0>:LTE:STATe) . \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:param patternNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Patt')
			:return: lte_antenna_ports: No help available"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		patternNull_cmd_val = self._cmd_group.get_repcap_cmd_value(patternNull, repcap.PatternNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:LTE:PATT{patternNull_cmd_val}:NAP?')
		return Conversions.str_to_scalar_enum(response, enums.NumberOfPorts)
