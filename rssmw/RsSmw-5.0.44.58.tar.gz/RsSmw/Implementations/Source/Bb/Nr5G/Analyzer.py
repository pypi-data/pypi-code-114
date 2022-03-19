from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Analyzer:
	"""Analyzer commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("analyzer", core, parent)

	def get_content(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:NR5G:ANALyzer:CONTent \n
		Snippet: value: str = driver.source.bb.nr5G.analyzer.get_content() \n
		Exports the signal configuration to an .allocation file that you can import into the NR 5G application on a signal and
		spectrum analyzer. \n
			:return: export_xml: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:ANALyzer:CONTent?')
		return trim_str_response(response)

	def set_content(self, export_xml: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:ANALyzer:CONTent \n
		Snippet: driver.source.bb.nr5G.analyzer.set_content(export_xml = '1') \n
		Exports the signal configuration to an .allocation file that you can import into the NR 5G application on a signal and
		spectrum analyzer. \n
			:param export_xml: string
		"""
		param = Conversions.value_to_quoted_str(export_xml)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:ANALyzer:CONTent {param}')

	def get_create(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:NR5G:ANALyzer:CREate \n
		Snippet: value: List[str] = driver.source.bb.nr5G.analyzer.get_create() \n
		No command help available \n
			:return: nr_5_gcat_name_export_xml: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:ANALyzer:CREate?')
		return Conversions.str_to_str_list(response)
