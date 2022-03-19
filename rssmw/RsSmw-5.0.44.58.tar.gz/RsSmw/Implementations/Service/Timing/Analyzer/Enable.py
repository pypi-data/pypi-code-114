from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Enable:
	"""Enable commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("enable", core, parent)

	def get_list_py(self) -> List[int]:
		"""SCPI: SERVice:TIMing:ANALyzer:ENABle:[LIST] \n
		Snippet: value: List[int] = driver.service.timing.analyzer.enable.get_list_py() \n
		No command help available \n
			:return: timing_analyzer_enable: No help available
		"""
		response = self._core.io.query_bin_or_ascii_int_list('SERVice:TIMing:ANALyzer:ENABle:LIST?')
		return response

	def set_list_py(self, timing_analyzer_enable: List[int]) -> None:
		"""SCPI: SERVice:TIMing:ANALyzer:ENABle:[LIST] \n
		Snippet: driver.service.timing.analyzer.enable.set_list_py(timing_analyzer_enable = [1, 2, 3]) \n
		No command help available \n
			:param timing_analyzer_enable: No help available
		"""
		param = Conversions.list_to_csv_str(timing_analyzer_enable)
		self._core.io.write(f'SERVice:TIMing:ANALyzer:ENABle:LIST {param}')
