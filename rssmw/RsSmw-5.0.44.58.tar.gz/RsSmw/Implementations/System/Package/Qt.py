from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Qt:
	"""Qt commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("qt", core, parent)

	def get_version(self) -> str:
		"""SCPI: SYSTem:PACKage:QT:VERSion \n
		Snippet: value: str = driver.system.package.qt.get_version() \n
		No command help available \n
			:return: version: No help available
		"""
		response = self._core.io.query_str('SYSTem:PACKage:QT:VERSion?')
		return trim_str_response(response)
