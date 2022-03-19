from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ethernet:
	"""Ethernet commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ethernet", core, parent)

	def get_active(self) -> str:
		"""SCPI: SYSTem:COMMunicate:SCPI:ETHernet:[ACTive] \n
		Snippet: value: str = driver.system.communicate.scpi.ethernet.get_active() \n
		No command help available \n
			:return: active_connection: No help available
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:SCPI:ETHernet:ACTive?')
		return trim_str_response(response)
