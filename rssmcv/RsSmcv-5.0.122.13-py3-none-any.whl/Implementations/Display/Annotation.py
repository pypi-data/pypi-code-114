from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Annotation:
	"""Annotation commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("annotation", core, parent)

	def get_amplitude(self) -> bool:
		"""SCPI: DISPlay:ANNotation:AMPLitude \n
		Snippet: value: bool = driver.display.annotation.get_amplitude() \n
		Indicates asterisks instead of the level values in the status bar. \n
			:return: state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('DISPlay:ANNotation:AMPLitude?')
		return Conversions.str_to_bool(response)

	def set_amplitude(self, state: bool) -> None:
		"""SCPI: DISPlay:ANNotation:AMPLitude \n
		Snippet: driver.display.annotation.set_amplitude(state = False) \n
		Indicates asterisks instead of the level values in the status bar. \n
			:param state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'DISPlay:ANNotation:AMPLitude {param}')

	def get_frequency(self) -> bool:
		"""SCPI: DISPlay:ANNotation:FREQuency \n
		Snippet: value: bool = driver.display.annotation.get_frequency() \n
		Indicates asterisks instead of the frequency values in the status bar. \n
			:return: state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('DISPlay:ANNotation:FREQuency?')
		return Conversions.str_to_bool(response)

	def set_frequency(self, state: bool) -> None:
		"""SCPI: DISPlay:ANNotation:FREQuency \n
		Snippet: driver.display.annotation.set_frequency(state = False) \n
		Indicates asterisks instead of the frequency values in the status bar. \n
			:param state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'DISPlay:ANNotation:FREQuency {param}')

	def get_all(self) -> bool:
		"""SCPI: DISPlay:ANNotation:[ALL] \n
		Snippet: value: bool = driver.display.annotation.get_all() \n
		Displays asterisks instead of the level and frequency values in the status bar of the instrument. We recommend that you
		use this mode if you operate the instrument in remote control. \n
			:return: state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('DISPlay:ANNotation:ALL?')
		return Conversions.str_to_bool(response)

	def set_all(self, state: bool) -> None:
		"""SCPI: DISPlay:ANNotation:[ALL] \n
		Snippet: driver.display.annotation.set_all(state = False) \n
		Displays asterisks instead of the level and frequency values in the status bar of the instrument. We recommend that you
		use this mode if you operate the instrument in remote control. \n
			:param state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'DISPlay:ANNotation:ALL {param}')
