from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Duplexing:
	"""Duplexing commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("duplexing", core, parent)

	def set(self, ulca_duplex_mode: enums.EutraDuplexMode, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:CA:CELL<CH0>:DUPLexing \n
		Snippet: driver.source.bb.eutra.uplink.ca.cell.duplexing.set(ulca_duplex_mode = enums.EutraDuplexMode.FDD, cellNull = repcap.CellNull.Default) \n
		Selects the duplexing mode of the component carriers. \n
			:param ulca_duplex_mode: TDD| FDD
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.enum_scalar_to_str(ulca_duplex_mode, enums.EutraDuplexMode)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:CA:CELL{cellNull_cmd_val}:DUPLexing {param}')

	# noinspection PyTypeChecker
	def get(self, cellNull=repcap.CellNull.Default) -> enums.EutraDuplexMode:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:CA:CELL<CH0>:DUPLexing \n
		Snippet: value: enums.EutraDuplexMode = driver.source.bb.eutra.uplink.ca.cell.duplexing.get(cellNull = repcap.CellNull.Default) \n
		Selects the duplexing mode of the component carriers. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: ulca_duplex_mode: TDD| FDD"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:CA:CELL{cellNull_cmd_val}:DUPLexing?')
		return Conversions.str_to_scalar_enum(response, enums.EutraDuplexMode)
