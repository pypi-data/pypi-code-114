from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Restart:
	"""Restart commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("restart", core, parent)

	def get_state(self) -> bool:
		"""SCPI: BERT:SETup:RESTart:[STATe] \n
		Snippet: value: bool = driver.bert.setup.restart.get_state() \n
		Activates/deactivates an external restart of the BERT measurement. \n
			:return: state: 0| OFF| 1| ON
		"""
		response = self._core.io.query_str('BERT:SETup:RESTart:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: BERT:SETup:RESTart:[STATe] \n
		Snippet: driver.bert.setup.restart.set_state(state = False) \n
		Activates/deactivates an external restart of the BERT measurement. \n
			:param state: 0| OFF| 1| ON
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'BERT:SETup:RESTart:STATe {param}')
