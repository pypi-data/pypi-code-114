from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Absolute:
	"""Absolute commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("absolute", core, parent)

	def get_set(self) -> str:
		"""SCPI: SYSTem:TIME:HRTimer:ABSolute:SET \n
		Snippet: value: str = driver.system.time.hrTimer.absolute.get_set() \n
		No command help available \n
			:return: pseudo_string: No help available
		"""
		response = self._core.io.query_str('SYSTem:TIME:HRTimer:ABSolute:SET?')
		return trim_str_response(response)

	def set_set(self, pseudo_string: str) -> None:
		"""SCPI: SYSTem:TIME:HRTimer:ABSolute:SET \n
		Snippet: driver.system.time.hrTimer.absolute.set_set(pseudo_string = '1') \n
		No command help available \n
			:param pseudo_string: No help available
		"""
		param = Conversions.value_to_quoted_str(pseudo_string)
		self._core.io.write(f'SYSTem:TIME:HRTimer:ABSolute:SET {param}')

	def set_value(self, pseudo_string: str) -> None:
		"""SCPI: SYSTem:TIME:HRTimer:ABSolute \n
		Snippet: driver.system.time.hrTimer.absolute.set_value(pseudo_string = '1') \n
		No command help available \n
			:param pseudo_string: No help available
		"""
		param = Conversions.value_to_quoted_str(pseudo_string)
		self._core.io.write(f'SYSTem:TIME:HRTimer:ABSolute {param}')
