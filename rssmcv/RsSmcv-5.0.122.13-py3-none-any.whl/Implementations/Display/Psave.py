from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Psave:
	"""Psave commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("psave", core, parent)

	def get_holdoff(self) -> int:
		"""SCPI: DISPlay:PSAVe:HOLDoff \n
		Snippet: value: int = driver.display.psave.get_holdoff() \n
		Sets the wait time for the screen saver mode of the display. \n
			:return: holdoff_time_min: integer Range: 1 to 60, Unit: minute
		"""
		response = self._core.io.query_str('DISPlay:PSAVe:HOLDoff?')
		return Conversions.str_to_int(response)

	def set_holdoff(self, holdoff_time_min: int) -> None:
		"""SCPI: DISPlay:PSAVe:HOLDoff \n
		Snippet: driver.display.psave.set_holdoff(holdoff_time_min = 1) \n
		Sets the wait time for the screen saver mode of the display. \n
			:param holdoff_time_min: integer Range: 1 to 60, Unit: minute
		"""
		param = Conversions.decimal_value_to_str(holdoff_time_min)
		self._core.io.write(f'DISPlay:PSAVe:HOLDoff {param}')

	def get_state(self) -> bool:
		"""SCPI: DISPlay:PSAVe:[STATe] \n
		Snippet: value: bool = driver.display.psave.get_state() \n
		Activates the screen saver mode of the display. We recommend that you use this mode to protect the display, if you
		operate the instrument in remote control. To define the wait time, use the command method RsSmcv.Display.Psave.holdoff. \n
			:return: state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('DISPlay:PSAVe:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: DISPlay:PSAVe:[STATe] \n
		Snippet: driver.display.psave.set_state(state = False) \n
		Activates the screen saver mode of the display. We recommend that you use this mode to protect the display, if you
		operate the instrument in remote control. To define the wait time, use the command method RsSmcv.Display.Psave.holdoff. \n
			:param state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'DISPlay:PSAVe:STATe {param}')
