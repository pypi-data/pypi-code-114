from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	def get_points(self) -> int:
		"""SCPI: [SOURce<HW>]:CORRection:CSET:DATA:FREQuency:POINts \n
		Snippet: value: int = driver.source.correction.cset.data.frequency.get_points() \n
		Queries the number of frequency/level values in the selected table. \n
			:return: points: integer Range: 0 to 10000
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:CORRection:CSET:DATA:FREQuency:POINts?')
		return Conversions.str_to_int(response)

	def get_value(self) -> List[float]:
		"""SCPI: [SOURce<HW>]:CORRection:CSET:DATA:FREQuency \n
		Snippet: value: List[float] = driver.source.correction.cset.data.frequency.get_value() \n
		Enters the frequency value in the table selected with [:SOURce<hw>]:CORRection:CSET[:SELect]. \n
			:return: frequency: Frequency#1[, Frequency#2, ...] String of values with default unit Hz.
		"""
		response = self._core.io.query_bin_or_ascii_float_list('SOURce<HwInstance>:CORRection:CSET:DATA:FREQuency?')
		return response

	def set_value(self, frequency: List[float]) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:CSET:DATA:FREQuency \n
		Snippet: driver.source.correction.cset.data.frequency.set_value(frequency = [1.1, 2.2, 3.3]) \n
		Enters the frequency value in the table selected with [:SOURce<hw>]:CORRection:CSET[:SELect]. \n
			:param frequency: Frequency#1[, Frequency#2, ...] String of values with default unit Hz.
		"""
		param = Conversions.list_to_csv_str(frequency)
		self._core.io.write(f'SOURce<HwInstance>:CORRection:CSET:DATA:FREQuency {param}')
