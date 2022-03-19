from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Symbol:
	"""Symbol commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbol", core, parent)

	# noinspection PyTypeChecker
	def get_interleaver(self) -> enums.DvbtCodingDvbhSymbolInterleaver:
		"""SCPI: [SOURce<HW>]:BB:DVBT:DVBH:SYMBol:[INTerleaver] \n
		Snippet: value: enums.DvbtCodingDvbhSymbolInterleaver = driver.source.bb.dvbt.dvbh.symbol.get_interleaver() \n
		Sets the symbol interleaver. \n
			:return: symb_interleaver: INDepth| NATive
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBT:DVBH:SYMBol:INTerleaver?')
		return Conversions.str_to_scalar_enum(response, enums.DvbtCodingDvbhSymbolInterleaver)

	def set_interleaver(self, symb_interleaver: enums.DvbtCodingDvbhSymbolInterleaver) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBT:DVBH:SYMBol:[INTerleaver] \n
		Snippet: driver.source.bb.dvbt.dvbh.symbol.set_interleaver(symb_interleaver = enums.DvbtCodingDvbhSymbolInterleaver.INDepth) \n
		Sets the symbol interleaver. \n
			:param symb_interleaver: INDepth| NATive
		"""
		param = Conversions.enum_scalar_to_str(symb_interleaver, enums.DvbtCodingDvbhSymbolInterleaver)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBT:DVBH:SYMBol:INTerleaver {param}')
