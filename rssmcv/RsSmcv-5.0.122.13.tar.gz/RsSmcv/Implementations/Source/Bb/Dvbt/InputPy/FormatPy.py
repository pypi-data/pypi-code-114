from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FormatPy:
	"""FormatPy commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("formatPy", core, parent)

	# noinspection PyTypeChecker
	def get_low(self) -> enums.CodingInputFormat:
		"""SCPI: [SOURce<HW>]:BB:DVBT:INPut:FORMat:LOW \n
		Snippet: value: enums.CodingInputFormat = driver.source.bb.dvbt.inputPy.formatPy.get_low() \n
		Sets the format of the input signal. \n
			:return: input_format_lp: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBT:INPut:FORMat:LOW?')
		return Conversions.str_to_scalar_enum(response, enums.CodingInputFormat)

	def set_low(self, input_format_lp: enums.CodingInputFormat) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBT:INPut:FORMat:LOW \n
		Snippet: driver.source.bb.dvbt.inputPy.formatPy.set_low(input_format_lp = enums.CodingInputFormat.ASI) \n
		Sets the format of the input signal. \n
			:param input_format_lp: ASI| SMPTE
		"""
		param = Conversions.enum_scalar_to_str(input_format_lp, enums.CodingInputFormat)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBT:INPut:FORMat:LOW {param}')

	# noinspection PyTypeChecker
	def get_value(self) -> enums.CodingInputFormat:
		"""SCPI: [SOURce<HW>]:BB:DVBT:INPut:FORMat \n
		Snippet: value: enums.CodingInputFormat = driver.source.bb.dvbt.inputPy.formatPy.get_value() \n
		Sets the format of the input signal. \n
			:return: input_format: ASI| SMPTE
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBT:INPut:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.CodingInputFormat)

	def set_value(self, input_format: enums.CodingInputFormat) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBT:INPut:FORMat \n
		Snippet: driver.source.bb.dvbt.inputPy.formatPy.set_value(input_format = enums.CodingInputFormat.ASI) \n
		Sets the format of the input signal. \n
			:param input_format: ASI| SMPTE
		"""
		param = Conversions.enum_scalar_to_str(input_format, enums.CodingInputFormat)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBT:INPut:FORMat {param}')
