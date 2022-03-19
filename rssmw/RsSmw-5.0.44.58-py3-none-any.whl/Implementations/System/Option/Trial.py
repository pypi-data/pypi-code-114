from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trial:
	"""Trial commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trial", core, parent)

	def get_list_py(self) -> List[str]:
		"""SCPI: SYSTem:OPTion:TRIal:LIST \n
		Snippet: value: List[str] = driver.system.option.trial.get_list_py() \n
		Queries the options included in the trial license. For a list of all available options and their description, refer to
		the data sheet. \n
			:return: trial_opt_list: string
		"""
		response = self._core.io.query_str('SYSTem:OPTion:TRIal:LIST?')
		return Conversions.str_to_str_list(response)

	def get_state(self) -> bool:
		"""SCPI: SYSTem:OPTion:TRIal:[STATe] \n
		Snippet: value: bool = driver.system.option.trial.get_state() \n
		Activates the trial license. \n
			:return: trial_opt_state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SYSTem:OPTion:TRIal:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, trial_opt_state: bool) -> None:
		"""SCPI: SYSTem:OPTion:TRIal:[STATe] \n
		Snippet: driver.system.option.trial.set_state(trial_opt_state = False) \n
		Activates the trial license. \n
			:param trial_opt_state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(trial_opt_state)
		self._core.io.write(f'SYSTem:OPTion:TRIal:STATe {param}')
