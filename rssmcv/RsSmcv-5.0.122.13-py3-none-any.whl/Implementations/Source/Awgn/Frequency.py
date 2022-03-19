from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	def get_result(self) -> float:
		"""SCPI: [SOURce<HW>]:AWGN:FREQuency:RESult \n
		Snippet: value: float = driver.source.awgn.frequency.get_result() \n
		Queries the actual frequency of the sine wave. \n
			:return: result: float Range: -40E6 to 40E6
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AWGN:FREQuency:RESult?')
		return Conversions.str_to_float(response)

	def get_target(self) -> float:
		"""SCPI: [SOURce<HW>]:AWGN:FREQuency:TARGet \n
		Snippet: value: float = driver.source.awgn.frequency.get_target() \n
		Sets the desired frequency of the sine wave. \n
			:return: target: float Range: -40E6 to 40E6
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AWGN:FREQuency:TARGet?')
		return Conversions.str_to_float(response)

	def set_target(self, target: float) -> None:
		"""SCPI: [SOURce<HW>]:AWGN:FREQuency:TARGet \n
		Snippet: driver.source.awgn.frequency.set_target(target = 1.0) \n
		Sets the desired frequency of the sine wave. \n
			:param target: float Range: -40E6 to 40E6
		"""
		param = Conversions.decimal_value_to_str(target)
		self._core.io.write(f'SOURce<HwInstance>:AWGN:FREQuency:TARGet {param}')
