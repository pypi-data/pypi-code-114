from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pconfiguration:
	"""Pconfiguration commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pconfiguration", core, parent)

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:V5G:SETTing:PCONfiguration:CATalog \n
		Snippet: value: List[str] = driver.source.bb.v5G.setting.pconfiguration.get_catalog() \n
		Queries the available configuration files in the default directory. Only predefined files are listed. \n
			:return: v_5_gcat_name_test_scenario: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:SETTing:PCONfiguration:CATalog?')
		return Conversions.str_to_str_list(response)

	def get_value(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:V5G:SETTing:PCONfiguration \n
		Snippet: value: str = driver.source.bb.v5G.setting.pconfiguration.get_value() \n
		Selects a predefined configuration. \n
			:return: test_scenario: string Filename as returned by the query [:SOURcehw]:BB:V5G:SETTing:PCONfiguration:CATalog. File extension is omitted.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:SETTing:PCONfiguration?')
		return trim_str_response(response)

	def set_value(self, test_scenario: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:SETTing:PCONfiguration \n
		Snippet: driver.source.bb.v5G.setting.pconfiguration.set_value(test_scenario = '1') \n
		Selects a predefined configuration. \n
			:param test_scenario: string Filename as returned by the query [:SOURcehw]:BB:V5G:SETTing:PCONfiguration:CATalog. File extension is omitted.
		"""
		param = Conversions.value_to_quoted_str(test_scenario)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:SETTing:PCONfiguration {param}')
