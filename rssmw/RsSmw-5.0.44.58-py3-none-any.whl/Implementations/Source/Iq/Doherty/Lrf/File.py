from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class File:
	"""File commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("file", core, parent)

	def get_data(self) -> List[float]:
		"""SCPI: [SOURce<HW>]:IQ:DOHerty:LRF:FILE:DATA \n
		Snippet: value: List[float] = driver.source.iq.doherty.lrf.file.get_data() \n
		No command help available \n
			:return: dpd_rf_am_table_data: No help available
		"""
		response = self._core.io.query_bin_or_ascii_float_list('SOURce<HwInstance>:IQ:DOHerty:LRF:FILE:DATA?')
		return response

	def get_value(self) -> str:
		"""SCPI: [SOURce<HW>]:IQ:DOHerty:LRF:FILE \n
		Snippet: value: str = driver.source.iq.doherty.lrf.file.get_value() \n
		No command help available \n
			:return: filename: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:DOHerty:LRF:FILE?')
		return trim_str_response(response)
