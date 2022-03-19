from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Kernel:
	"""Kernel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("kernel", core, parent)

	def get_version(self) -> str:
		"""SCPI: SYSTem:LINux:KERNel:VERSion \n
		Snippet: value: str = driver.system.linux.kernel.get_version() \n
		No command help available \n
			:return: version: No help available
		"""
		response = self._core.io.query_str('SYSTem:LINux:KERNel:VERSion?')
		return trim_str_response(response)
