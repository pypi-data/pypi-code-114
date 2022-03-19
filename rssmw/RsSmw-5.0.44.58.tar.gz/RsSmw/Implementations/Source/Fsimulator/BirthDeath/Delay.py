from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Delay:
	"""Delay commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("delay", core, parent)

	def get_grid(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:BIRThdeath:DELay:GRID \n
		Snippet: value: float = driver.source.fsimulator.birthDeath.delay.get_grid() \n
		Sets the delay grid for both paths with birth death propagation fading. \n
			:return: grid: float Range: 1E-9 to dynamic
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:BIRThdeath:DELay:GRID?')
		return Conversions.str_to_float(response)

	def set_grid(self, grid: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:BIRThdeath:DELay:GRID \n
		Snippet: driver.source.fsimulator.birthDeath.delay.set_grid(grid = 1.0) \n
		Sets the delay grid for both paths with birth death propagation fading. \n
			:param grid: float Range: 1E-9 to dynamic
		"""
		param = Conversions.decimal_value_to_str(grid)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:BIRThdeath:DELay:GRID {param}')

	def get_maximum(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:BIRThdeath:DELay:MAXimum \n
		Snippet: value: float = driver.source.fsimulator.birthDeath.delay.get_maximum() \n
		Queries the minimum/maximum delay for both paths with birth death propagation fading. \n
			:return: maximum: float Range: 0 to max
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:BIRThdeath:DELay:MAXimum?')
		return Conversions.str_to_float(response)

	def get_minimum(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:BIRThdeath:DELay:MINimum \n
		Snippet: value: float = driver.source.fsimulator.birthDeath.delay.get_minimum() \n
		Queries the minimum/maximum delay for both paths with birth death propagation fading. \n
			:return: minimum: float Range: 0 to max
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:BIRThdeath:DELay:MINimum?')
		return Conversions.str_to_float(response)

	def set_minimum(self, minimum: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:BIRThdeath:DELay:MINimum \n
		Snippet: driver.source.fsimulator.birthDeath.delay.set_minimum(minimum = 1.0) \n
		Queries the minimum/maximum delay for both paths with birth death propagation fading. \n
			:param minimum: No help available
		"""
		param = Conversions.decimal_value_to_str(minimum)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:BIRThdeath:DELay:MINimum {param}')
