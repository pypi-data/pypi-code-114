from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Synchronize:
	"""Synchronize commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("synchronize", core, parent)

	def get(self, time: str) -> str:
		"""SCPI: SYSTem:SRTime:SYNChronize \n
		Snippet: value: str = driver.system.srtime.synchronize.get(time = '1') \n
		No command help available \n
			:param time: No help available
			:return: time: No help available"""
		param = Conversions.value_to_quoted_str(time)
		response = self._core.io.query_str(f'SYSTem:SRTime:SYNChronize? {param}')
		return trim_str_response(response)
