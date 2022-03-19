from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Delay:
	"""Delay commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("delay", core, parent)

	def get_mean(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:MDELay:MOVing:DELay:MEAN \n
		Snippet: value: float = driver.source.fsimulator.mdelay.moving.delay.get_mean() \n
		Sets the mean delay of the moving fading path for moving propagation. \n
			:return: mean: float Range: 0 to 40E-6
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:MDELay:MOVing:DELay:MEAN?')
		return Conversions.str_to_float(response)

	def set_mean(self, mean: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MDELay:MOVing:DELay:MEAN \n
		Snippet: driver.source.fsimulator.mdelay.moving.delay.set_mean(mean = 1.0) \n
		Sets the mean delay of the moving fading path for moving propagation. \n
			:param mean: float Range: 0 to 40E-6
		"""
		param = Conversions.decimal_value_to_str(mean)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MDELay:MOVing:DELay:MEAN {param}')

	def get_variation(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:MDELay:MOVing:DELay:VARiation \n
		Snippet: value: float = driver.source.fsimulator.mdelay.moving.delay.get_variation() \n
		Enters the range for the delay of the moving fading path for moving propagation. The delay of the moving path slowly
		varies sinusoidal within this range. \n
			:return: variation: float Range: 0.3E-6 to dynamic
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:MDELay:MOVing:DELay:VARiation?')
		return Conversions.str_to_float(response)

	def set_variation(self, variation: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MDELay:MOVing:DELay:VARiation \n
		Snippet: driver.source.fsimulator.mdelay.moving.delay.set_variation(variation = 1.0) \n
		Enters the range for the delay of the moving fading path for moving propagation. The delay of the moving path slowly
		varies sinusoidal within this range. \n
			:param variation: float Range: 0.3E-6 to dynamic
		"""
		param = Conversions.decimal_value_to_str(variation)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MDELay:MOVing:DELay:VARiation {param}')
