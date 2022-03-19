from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Day:
	"""Day commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("day", core, parent)

	def get_state(self) -> bool:
		"""SCPI: HCOPy:FILE:[NAME]:AUTO:[FILE]:DAY:STATe \n
		Snippet: value: bool = driver.hardCopy.file.name.auto.file.day.get_state() \n
		Uses the date parameters (year, month or day) for the automatic naming. You can activate each of the date parameters
		separately. \n
			:return: state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('HCOPy:FILE:NAME:AUTO:FILE:DAY:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: HCOPy:FILE:[NAME]:AUTO:[FILE]:DAY:STATe \n
		Snippet: driver.hardCopy.file.name.auto.file.day.set_state(state = False) \n
		Uses the date parameters (year, month or day) for the automatic naming. You can activate each of the date parameters
		separately. \n
			:param state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'HCOPy:FILE:NAME:AUTO:FILE:DAY:STATe {param}')
