from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Segment:
	"""Segment commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("segment", core, parent)

	def set_append(self, waveform: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:WSEGment:CONFigure:SEGMent:APPend \n
		Snippet: driver.source.bb.arbitrary.wsegment.configure.segment.set_append(waveform = '1') \n
		Appends the specified waveform to the configuration file. \n
			:param waveform: string
		"""
		param = Conversions.value_to_quoted_str(waveform)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:WSEGment:CONFigure:SEGMent:APPend {param}')

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:WSEGment:CONFigure:SEGMent:CATalog \n
		Snippet: value: List[str] = driver.source.bb.arbitrary.wsegment.configure.segment.get_catalog() \n
		Queries the segments of the currently selected configuration file. \n
			:return: catalog: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:WSEGment:CONFigure:SEGMent:CATalog?')
		return Conversions.str_to_str_list(response)
