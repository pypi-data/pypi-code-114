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
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:SRATe:VARiation \n
		Snippet: value: float = driver.source.bb.oneweb.symbolRate.get_variation() \n
		Sets the output sample rate. A variation of this parameter affects the ARB clock rate; all other signal parameters remain
		unchanged. The current value of this parameter depends on the current physical settings, like the channel bandwidth. \n
			:return: sample_rate_var: float Range: 400 to 4E7, Unit: Hz
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:SRATe:VARiation?')
		return Conversions.str_to_float(response)

	def set_variation(self, sample_rate_var: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:SRATe:VARiation \n
		Snippet: driver.source.bb.oneweb.symbolRate.set_variation(sample_rate_var = 1.0) \n
		Sets the output sample rate. A variation of this parameter affects the ARB clock rate; all other signal parameters remain
		unchanged. The current value of this parameter depends on the current physical settings, like the channel bandwidth. \n
			:param sample_rate_var: float Range: 400 to 4E7, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(sample_rate_var)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:SRATe:VARiation {param}')
