from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Module:
	"""Module commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("module", core, parent)

	def get_catalog(self) -> List[str]:
		"""SCPI: SYSTem:PROFiling:MODule:CATalog \n
		Snippet: value: List[str] = driver.system.profiling.module.get_catalog() \n
		No command help available \n
			:return: catalog: No help available
		"""
		response = self._core.io.query_str('SYSTem:PROFiling:MODule:CATalog?')
		return Conversions.str_to_str_list(response)

	def get_state(self) -> bool:
		"""SCPI: SYSTem:PROFiling:MODule:STATe \n
		Snippet: value: bool = driver.system.profiling.module.get_state() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('SYSTem:PROFiling:MODule:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: SYSTem:PROFiling:MODule:STATe \n
		Snippet: driver.system.profiling.module.set_state(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SYSTem:PROFiling:MODule:STATe {param}')
