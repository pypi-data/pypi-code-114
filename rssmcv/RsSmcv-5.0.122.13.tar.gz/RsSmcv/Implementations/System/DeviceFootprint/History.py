from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class History:
	"""History commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("history", core, parent)

	def get_count(self) -> str:
		"""SCPI: SYSTem:DFPRint:HISTory:COUNt \n
		Snippet: value: str = driver.system.deviceFootprint.history.get_count() \n
		No command help available \n
			:return: pseudo_string: No help available
		"""
		response = self._core.io.query_str('SYSTem:DFPRint:HISTory:COUNt?')
		return trim_str_response(response)

	def get_entry(self) -> str:
		"""SCPI: SYSTem:DFPRint:HISTory:ENTRy \n
		Snippet: value: str = driver.system.deviceFootprint.history.get_entry() \n
		No command help available \n
			:return: pseudo_string: No help available
		"""
		response = self._core.io.query_str('SYSTem:DFPRint:HISTory:ENTRy?')
		return trim_str_response(response)
