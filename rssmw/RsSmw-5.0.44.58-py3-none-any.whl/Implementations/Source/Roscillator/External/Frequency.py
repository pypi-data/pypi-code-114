from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	def get_variable(self) -> float:
		"""SCPI: [SOURce]:ROSCillator:EXTernal:FREQuency:VARiable \n
		Snippet: value: float = driver.source.roscillator.external.frequency.get_variable() \n
		Specifies the user-defined external reference frequency. \n
			:return: frequency: float Range: 1E6 to 100E6, Unit: Hz
		"""
		response = self._core.io.query_str('SOURce:ROSCillator:EXTernal:FREQuency:VARiable?')
		return Conversions.str_to_float(response)

	def set_variable(self, frequency: float) -> None:
		"""SCPI: [SOURce]:ROSCillator:EXTernal:FREQuency:VARiable \n
		Snippet: driver.source.roscillator.external.frequency.set_variable(frequency = 1.0) \n
		Specifies the user-defined external reference frequency. \n
			:param frequency: float Range: 1E6 to 100E6, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'SOURce:ROSCillator:EXTernal:FREQuency:VARiable {param}')

	# noinspection PyTypeChecker
	def get_value(self) -> enums.RoscFreqExt:
		"""SCPI: [SOURce]:ROSCillator:EXTernal:FREQuency \n
		Snippet: value: enums.RoscFreqExt = driver.source.roscillator.external.frequency.get_value() \n
		Sets the frequency of the external reference. \n
			:return: frequency: 10MHZ| VARiable| 5MHZ| 13MHZ
		"""
		response = self._core.io.query_str('SOURce:ROSCillator:EXTernal:FREQuency?')
		return Conversions.str_to_scalar_enum(response, enums.RoscFreqExt)

	def set_value(self, frequency: enums.RoscFreqExt) -> None:
		"""SCPI: [SOURce]:ROSCillator:EXTernal:FREQuency \n
		Snippet: driver.source.roscillator.external.frequency.set_value(frequency = enums.RoscFreqExt._100MHZ) \n
		Sets the frequency of the external reference. \n
			:param frequency: 10MHZ| VARiable| 5MHZ| 13MHZ
		"""
		param = Conversions.enum_scalar_to_str(frequency, enums.RoscFreqExt)
		self._core.io.write(f'SOURce:ROSCillator:EXTernal:FREQuency {param}')
