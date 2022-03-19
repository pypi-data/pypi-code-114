from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Separator:
	"""Separator commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("separator", core, parent)

	# noinspection PyTypeChecker
	def get_column(self) -> enums.DexchSepCol:
		"""SCPI: [SOURce<HW>]:LIST:DEXChange:AFILe:SEParator:COLumn \n
		Snippet: value: enums.DexchSepCol = driver.source.listPy.dexchange.afile.separator.get_column() \n
		Selects the separator between the frequency and level column of the ASCII table. \n
			:return: column: TABulator| SEMicolon| COMMa| SPACe
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:LIST:DEXChange:AFILe:SEParator:COLumn?')
		return Conversions.str_to_scalar_enum(response, enums.DexchSepCol)

	def set_column(self, column: enums.DexchSepCol) -> None:
		"""SCPI: [SOURce<HW>]:LIST:DEXChange:AFILe:SEParator:COLumn \n
		Snippet: driver.source.listPy.dexchange.afile.separator.set_column(column = enums.DexchSepCol.COMMa) \n
		Selects the separator between the frequency and level column of the ASCII table. \n
			:param column: TABulator| SEMicolon| COMMa| SPACe
		"""
		param = Conversions.enum_scalar_to_str(column, enums.DexchSepCol)
		self._core.io.write(f'SOURce<HwInstance>:LIST:DEXChange:AFILe:SEParator:COLumn {param}')

	# noinspection PyTypeChecker
	def get_decimal(self) -> enums.DexchSepDec:
		"""SCPI: [SOURce<HW>]:LIST:DEXChange:AFILe:SEParator:DECimal \n
		Snippet: value: enums.DexchSepDec = driver.source.listPy.dexchange.afile.separator.get_decimal() \n
		Sets '.' (decimal point) or ',' (comma) as the decimal separator used in the ASCII data with floating-point numerals. \n
			:return: decimal: DOT| COMMa
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:LIST:DEXChange:AFILe:SEParator:DECimal?')
		return Conversions.str_to_scalar_enum(response, enums.DexchSepDec)

	def set_decimal(self, decimal: enums.DexchSepDec) -> None:
		"""SCPI: [SOURce<HW>]:LIST:DEXChange:AFILe:SEParator:DECimal \n
		Snippet: driver.source.listPy.dexchange.afile.separator.set_decimal(decimal = enums.DexchSepDec.COMMa) \n
		Sets '.' (decimal point) or ',' (comma) as the decimal separator used in the ASCII data with floating-point numerals. \n
			:param decimal: DOT| COMMa
		"""
		param = Conversions.enum_scalar_to_str(decimal, enums.DexchSepDec)
		self._core.io.write(f'SOURce<HwInstance>:LIST:DEXChange:AFILe:SEParator:DECimal {param}')
