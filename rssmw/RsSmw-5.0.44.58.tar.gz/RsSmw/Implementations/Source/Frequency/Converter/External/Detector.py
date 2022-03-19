from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Detector:
	"""Detector commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("detector", core, parent)

	def get_offset(self) -> str:
		"""SCPI: [SOURce<HW>]:FREQuency:CONVerter:EXTernal:DETector:OFFSet \n
		Snippet: value: str = driver.source.frequency.converter.external.detector.get_offset() \n
		No command help available \n
			:return: conv_ext_det_offs: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FREQuency:CONVerter:EXTernal:DETector:OFFSet?')
		return trim_str_response(response)

	def get_temperature(self) -> str:
		"""SCPI: [SOURce<HW>]:FREQuency:CONVerter:EXTernal:DETector:TEMPerature \n
		Snippet: value: str = driver.source.frequency.converter.external.detector.get_temperature() \n
		No command help available \n
			:return: con_ext_det_temp: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FREQuency:CONVerter:EXTernal:DETector:TEMPerature?')
		return trim_str_response(response)

	def get_zerores(self) -> str:
		"""SCPI: [SOURce<HW>]:FREQuency:CONVerter:EXTernal:DETector:ZERores \n
		Snippet: value: str = driver.source.frequency.converter.external.detector.get_zerores() \n
		No command help available \n
			:return: conv_ext_det_zeror: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FREQuency:CONVerter:EXTernal:DETector:ZERores?')
		return trim_str_response(response)
