from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	def get_max(self) -> float:
		"""SCPI: [SOURce<HW>]:FREQuency:CONVerter:EXTernal:OVERrange:FREQuency:MAX \n
		Snippet: value: float = driver.source.frequency.converter.external.overrange.frequency.get_max() \n
		Indicates the minimum and maximum frequency range values of the connected R&S SZU. The frequency overrange is based on
		the calibration data of the specific device. \n
			:return: overrang_freq_max: float Range: OverrangeMin to OverrangeMax
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FREQuency:CONVerter:EXTernal:OVERrange:FREQuency:MAX?')
		return Conversions.str_to_float(response)

	def get_min(self) -> float:
		"""SCPI: [SOURce<HW>]:FREQuency:CONVerter:EXTernal:OVERrange:FREQuency:MIN \n
		Snippet: value: float = driver.source.frequency.converter.external.overrange.frequency.get_min() \n
		Indicates the minimum frequency value of the connected R&S SZU. The frequency overrange is based on the calibration data
		of the specific device. \n
			:return: overrang_min_freq: float Range: OverrangeMin to OverrangeMax
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FREQuency:CONVerter:EXTernal:OVERrange:FREQuency:MIN?')
		return Conversions.str_to_float(response)
