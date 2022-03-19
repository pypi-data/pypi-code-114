from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Delay:
	"""Delay commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("delay", core, parent)

	def get_maximum(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:TCINterferer:MOVing:DELay:MAXimum \n
		Snippet: value: float = driver.source.fsimulator.tcInterferer.moving.delay.get_maximum() \n
		Sets the maximum delay for the moving path. \n
			:return: maximum: float Range: dynamic to 0.001
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:TCINterferer:MOVing:DELay:MAXimum?')
		return Conversions.str_to_float(response)

	def set_maximum(self, maximum: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:TCINterferer:MOVing:DELay:MAXimum \n
		Snippet: driver.source.fsimulator.tcInterferer.moving.delay.set_maximum(maximum = 1.0) \n
		Sets the maximum delay for the moving path. \n
			:param maximum: float Range: dynamic to 0.001
		"""
		param = Conversions.decimal_value_to_str(maximum)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:TCINterferer:MOVing:DELay:MAXimum {param}')

	def get_minimum(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:TCINterferer:MOVing:DELay:MINimum \n
		Snippet: value: float = driver.source.fsimulator.tcInterferer.moving.delay.get_minimum() \n
		Sets the minimum delay for the reference path and the moving path. \n
			:return: minimum: float Range: 0 to dynamic
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:TCINterferer:MOVing:DELay:MINimum?')
		return Conversions.str_to_float(response)

	def set_minimum(self, minimum: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:TCINterferer:MOVing:DELay:MINimum \n
		Snippet: driver.source.fsimulator.tcInterferer.moving.delay.set_minimum(minimum = 1.0) \n
		Sets the minimum delay for the reference path and the moving path. \n
			:param minimum: float Range: 0 to dynamic
		"""
		param = Conversions.decimal_value_to_str(minimum)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:TCINterferer:MOVing:DELay:MINimum {param}')
