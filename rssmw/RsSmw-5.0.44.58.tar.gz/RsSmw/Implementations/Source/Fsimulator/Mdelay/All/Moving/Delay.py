from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Delay:
	"""Delay commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("delay", core, parent)

	def get_variation(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:MDELay:ALL:MOVing:DELay:VARiation \n
		Snippet: value: float = driver.source.fsimulator.mdelay.all.moving.delay.get_variation() \n
		This command enters the range for the delay of the moving fading paths for moving propagation with all moving channels.
		The delay of the moving path slowly varies sinusoidally within this range. \n
			:return: variation: float Range: 0.3E-6 to 10E-6
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:MDELay:ALL:MOVing:DELay:VARiation?')
		return Conversions.str_to_float(response)

	def set_variation(self, variation: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MDELay:ALL:MOVing:DELay:VARiation \n
		Snippet: driver.source.fsimulator.mdelay.all.moving.delay.set_variation(variation = 1.0) \n
		This command enters the range for the delay of the moving fading paths for moving propagation with all moving channels.
		The delay of the moving path slowly varies sinusoidally within this range. \n
			:param variation: float Range: 0.3E-6 to 10E-6
		"""
		param = Conversions.decimal_value_to_str(variation)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MDELay:ALL:MOVing:DELay:VARiation {param}')
