from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Path:
	"""Path commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("path", core, parent)

	def get_count(self) -> int:
		"""SCPI: [SOURce]:PATH:COUNt \n
		Snippet: value: int = driver.source.path.get_count() \n
		No command help available \n
			:return: count: No help available
		"""
		response = self._core.io.query_str('SOURce:PATH:COUNt?')
		return Conversions.str_to_int(response)
