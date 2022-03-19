from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Symbols:
	"""Symbols commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbols", core, parent)

	def get_rate(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:SYMBols:[RATE] \n
		Snippet: value: float = driver.source.bb.dvbs2.symbols.get_rate() \n
		Sets the symbol rate. In the transmission spectrum, the symbol rate represents the 3 dB bandwidth. \n
			:return: symbol_rate: float Range: 0,100000 to 90,000000
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBS2:SYMBols:RATE?')
		return Conversions.str_to_float(response)

	def set_rate(self, symbol_rate: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:SYMBols:[RATE] \n
		Snippet: driver.source.bb.dvbs2.symbols.set_rate(symbol_rate = 1.0) \n
		Sets the symbol rate. In the transmission spectrum, the symbol rate represents the 3 dB bandwidth. \n
			:param symbol_rate: float Range: 0,100000 to 90,000000
		"""
		param = Conversions.decimal_value_to_str(symbol_rate)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS2:SYMBols:RATE {param}')
