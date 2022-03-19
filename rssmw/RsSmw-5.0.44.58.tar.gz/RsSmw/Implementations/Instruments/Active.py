from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Active:
	"""Active commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("active", core, parent)

	def get_state(self) -> List[bool]:
		"""SCPI: INSTruments:ACTive:[STATe] \n
		Snippet: value: List[bool] = driver.instruments.active.get_state() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('INSTruments:ACTive:STATe?')
		return Conversions.str_to_bool_list(response)

	def set_state(self, state: List[bool]) -> None:
		"""SCPI: INSTruments:ACTive:[STATe] \n
		Snippet: driver.instruments.active.set_state(state = [True, False, True]) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.list_to_csv_str(state)
		self._core.io.write(f'INSTruments:ACTive:STATe {param}')
