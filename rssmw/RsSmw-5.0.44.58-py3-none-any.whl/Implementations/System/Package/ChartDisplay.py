from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ChartDisplay:
	"""ChartDisplay commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("chartDisplay", core, parent)

	def get_version(self) -> str:
		"""SCPI: SYSTem:PACKage:CHARtdisplay:VERSion \n
		Snippet: value: str = driver.system.package.chartDisplay.get_version() \n
		No command help available \n
			:return: version: No help available
		"""
		response = self._core.io.query_str('SYSTem:PACKage:CHARtdisplay:VERSion?')
		return trim_str_response(response)
