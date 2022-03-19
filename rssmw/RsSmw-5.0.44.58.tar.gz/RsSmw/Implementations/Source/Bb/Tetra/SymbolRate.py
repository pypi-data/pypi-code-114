from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SymbolRate:
	"""SymbolRate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbolRate", core, parent)

	def get_variation(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:TETRa:SRATe:VARiation \n
		Snippet: value: float = driver.source.bb.tetra.symbolRate.get_variation() \n
		Sets the symbol rate of the signal. A variation of this parameter only affects the ARB clock rate; all other signal
		parameters remain unchanged. \n
			:return: variation: float Range: 400 to 15E6
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TETRa:SRATe:VARiation?')
		return Conversions.str_to_float(response)

	def set_variation(self, variation: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:SRATe:VARiation \n
		Snippet: driver.source.bb.tetra.symbolRate.set_variation(variation = 1.0) \n
		Sets the symbol rate of the signal. A variation of this parameter only affects the ARB clock rate; all other signal
		parameters remain unchanged. \n
			:param variation: float Range: 400 to 15E6
		"""
		param = Conversions.decimal_value_to_str(variation)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:SRATe:VARiation {param}')
