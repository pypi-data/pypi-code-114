from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Name:
	"""Name commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("name", core, parent)

	def get_detailed(self) -> str:
		"""SCPI: SYSTem:LOCK:NAME:DETailed \n
		Snippet: value: str = driver.system.lock.name.get_detailed() \n
		No command help available \n
			:return: details: No help available
		"""
		response = self._core.io.query_str('SYSTem:LOCK:NAME:DETailed?')
		return trim_str_response(response)

	def get_value(self) -> str:
		"""SCPI: SYSTem:LOCK:NAME \n
		Snippet: value: str = driver.system.lock.name.get_value() \n
		No command help available \n
			:return: name: No help available
		"""
		response = self._core.io.query_str('SYSTem:LOCK:NAME?')
		return trim_str_response(response)
