from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Symbols:
	"""Symbols commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbols", core, parent)

	def get_rate(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ATSM:SYMBols:[RATE] \n
		Snippet: value: int = driver.source.bb.atsm.symbols.get_rate() \n
		Sets the symbol rate. \n
			:return: symbol_rate: integer Range: 10224126 to 11300350
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ATSM:SYMBols:RATE?')
		return Conversions.str_to_int(response)

	def set_rate(self, symbol_rate: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ATSM:SYMBols:[RATE] \n
		Snippet: driver.source.bb.atsm.symbols.set_rate(symbol_rate = 1) \n
		Sets the symbol rate. \n
			:param symbol_rate: integer Range: 10224126 to 11300350
		"""
		param = Conversions.decimal_value_to_str(symbol_rate)
		self._core.io.write(f'SOURce<HwInstance>:BB:ATSM:SYMBols:RATE {param}')
