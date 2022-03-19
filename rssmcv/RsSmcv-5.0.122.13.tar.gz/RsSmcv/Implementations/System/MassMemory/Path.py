from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Path:
	"""Path commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("path", core, parent)

	def get(self, path_type: str) -> str:
		"""SCPI: SYSTem:MMEMory:PATH \n
		Snippet: value: str = driver.system.massMemory.path.get(path_type = '1') \n
		No command help available \n
			:param path_type: No help available
			:return: path: No help available"""
		param = Conversions.value_to_quoted_str(path_type)
		response = self._core.io.query_str(f'SYSTem:MMEMory:PATH? {param}')
		return trim_str_response(response)

	def get_user(self) -> str:
		"""SCPI: SYSTem:MMEMory:PATH:USER \n
		Snippet: value: str = driver.system.massMemory.path.get_user() \n
		Queries the user directory, that means the directory the R&S SMCV100B stores user files on. \n
			:return: path_user: string
		"""
		response = self._core.io.query_str('SYSTem:MMEMory:PATH:USER?')
		return trim_str_response(response)
