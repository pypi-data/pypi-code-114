from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Code:
	"""Code commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("code", core, parent)

	def get_all(self) -> str:
		"""SCPI: SYSTem:ERRor:CODE:ALL \n
		Snippet: value: str = driver.system.error.code.get_all() \n
		Queries the error numbers of all entries in the error queue and then deletes them. \n
			:return: all: string Returns the error numbers. To retrieve the entire error text, send the command method RsSmw.System.Error.all. 0 'No error', i.e. the error queue is empty Positive value Positive error numbers denote device-specific errors Negative value Negative error numbers denote error messages defined by SCPI.
		"""
		response = self._core.io.query_str('SYSTem:ERRor:CODE:ALL?')
		return trim_str_response(response)

	def get_next(self) -> str:
		"""SCPI: SYSTem:ERRor:CODE:[NEXT] \n
		Snippet: value: str = driver.system.error.code.get_next() \n
		Queries the error number of the oldest entry in the error queue and then deletes it. \n
			:return: next_py: string Returns the error number. To retrieve the entire error text, send the command method RsSmw.System.Error.all. 0 'No error', i.e. the error queue is empty Positive value Positive error numbers denote device-specific errors Negative value Negative error numbers denote error messages defined by SCPI.
		"""
		response = self._core.io.query_str('SYSTem:ERRor:CODE:NEXT?')
		return trim_str_response(response)
