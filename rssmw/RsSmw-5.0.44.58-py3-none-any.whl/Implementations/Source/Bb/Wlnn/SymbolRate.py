from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SymbolRate:
	"""SymbolRate commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbolRate", core, parent)

	def get_variation(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:WLNN:SRATe:VARiation \n
		Snippet: value: float = driver.source.bb.wlnn.symbolRate.get_variation() \n
		Sets the sample rate of the signal. \n
			:return: variation: float Range: 400 to 40000000, Unit: Hz (c/s)
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLNN:SRATe:VARiation?')
		return Conversions.str_to_float(response)

	def set_variation(self, variation: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:SRATe:VARiation \n
		Snippet: driver.source.bb.wlnn.symbolRate.set_variation(variation = 1.0) \n
		Sets the sample rate of the signal. \n
			:param variation: float Range: 400 to 40000000, Unit: Hz (c/s)
		"""
		param = Conversions.decimal_value_to_str(variation)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:SRATe:VARiation {param}')

	def get_value(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:WLNN:SRATe \n
		Snippet: value: float = driver.source.bb.wlnn.symbolRate.get_value() \n
		Displays the sample rate specific for the selected bandwidth ([:SOURce<hw>]:BB:WLNN:BWidth) . \n
			:return: samp_rate: float 20MHz for BW20, 60MHz for BW40.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLNN:SRATe?')
		return Conversions.str_to_float(response)
