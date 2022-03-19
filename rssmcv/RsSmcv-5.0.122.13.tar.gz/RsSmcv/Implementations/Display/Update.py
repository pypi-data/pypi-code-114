from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Update:
	"""Update commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("update", core, parent)

	def get_hold(self) -> bool:
		"""SCPI: DISPlay:UPDate:HOLD \n
		Snippet: value: bool = driver.display.update.get_hold() \n
		No command help available \n
			:return: hold: No help available
		"""
		response = self._core.io.query_str('DISPlay:UPDate:HOLD?')
		return Conversions.str_to_bool(response)

	def set_hold(self, hold: bool) -> None:
		"""SCPI: DISPlay:UPDate:HOLD \n
		Snippet: driver.display.update.set_hold(hold = False) \n
		No command help available \n
			:param hold: No help available
		"""
		param = Conversions.bool_to_str(hold)
		self._core.io.write(f'DISPlay:UPDate:HOLD {param}')

	def get_state(self) -> bool:
		"""SCPI: DISPlay:UPDate:[STATe] \n
		Snippet: value: bool = driver.display.update.get_state() \n
		Activates the refresh mode of the display. \n
			:return: update: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('DISPlay:UPDate:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, update: bool) -> None:
		"""SCPI: DISPlay:UPDate:[STATe] \n
		Snippet: driver.display.update.set_state(update = False) \n
		Activates the refresh mode of the display. \n
			:param update: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(update)
		self._core.io.write(f'DISPlay:UPDate:STATe {param}')
