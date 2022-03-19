from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Azero:
	"""Azero commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("azero", core, parent)

	def get_unscaled(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:TIME:CONVersion:GALileo:UTC:AZERo:UNSCaled \n
		Snippet: value: float = driver.source.bb.gnss.time.conversion.galileo.utc.azero.get_unscaled() \n
		Sets the constant term of polynomial, A0. \n
			:return: a_0: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:TIME:CONVersion:GALileo:UTC:AZERo:UNSCaled?')
		return Conversions.str_to_float(response)

	def set_unscaled(self, a_0: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:TIME:CONVersion:GALileo:UTC:AZERo:UNSCaled \n
		Snippet: driver.source.bb.gnss.time.conversion.galileo.utc.azero.set_unscaled(a_0 = 1.0) \n
		Sets the constant term of polynomial, A0. \n
			:param a_0: integer Range: -2147483648 to 2147483647
		"""
		param = Conversions.decimal_value_to_str(a_0)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:TIME:CONVersion:GALileo:UTC:AZERo:UNSCaled {param}')

	def get_value(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:TIME:CONVersion:GALileo:UTC:AZERo \n
		Snippet: value: int = driver.source.bb.gnss.time.conversion.galileo.utc.azero.get_value() \n
		Sets the constant term of polynomial, A0. \n
			:return: azero: integer Range: -2147483648 to 2147483647
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:TIME:CONVersion:GALileo:UTC:AZERo?')
		return Conversions.str_to_int(response)

	def set_value(self, azero: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:TIME:CONVersion:GALileo:UTC:AZERo \n
		Snippet: driver.source.bb.gnss.time.conversion.galileo.utc.azero.set_value(azero = 1) \n
		Sets the constant term of polynomial, A0. \n
			:param azero: integer Range: -2147483648 to 2147483647
		"""
		param = Conversions.decimal_value_to_str(azero)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:TIME:CONVersion:GALileo:UTC:AZERo {param}')
