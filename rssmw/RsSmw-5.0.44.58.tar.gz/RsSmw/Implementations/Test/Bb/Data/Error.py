from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Error:
	"""Error commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("error", core, parent)

	def get_rate(self) -> float:
		"""SCPI: TEST:BB:DATA:ERRor:RATE \n
		Snippet: value: float = driver.test.bb.data.error.get_rate() \n
		Sets the error bit pattern of the BER/BLER test generator. \n
			:return: error_rate: float Range: 1E-6 to 1
		"""
		response = self._core.io.query_str('TEST:BB:DATA:ERRor:RATE?')
		return Conversions.str_to_float(response)

	def set_rate(self, error_rate: float) -> None:
		"""SCPI: TEST:BB:DATA:ERRor:RATE \n
		Snippet: driver.test.bb.data.error.set_rate(error_rate = 1.0) \n
		Sets the error bit pattern of the BER/BLER test generator. \n
			:param error_rate: float Range: 1E-6 to 1
		"""
		param = Conversions.decimal_value_to_str(error_rate)
		self._core.io.write(f'TEST:BB:DATA:ERRor:RATE {param}')
