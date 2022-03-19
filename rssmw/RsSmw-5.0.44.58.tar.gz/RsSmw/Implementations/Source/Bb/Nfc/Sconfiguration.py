from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sconfiguration:
	"""Sconfiguration commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sconfiguration", core, parent)

	def get_tn_samples(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:NFC:SCONfiguration:TNSamples \n
		Snippet: value: int = driver.source.bb.nfc.sconfiguration.get_tn_samples() \n
		Queries the total number of samples allocated to the current frame. \n
			:return: tn_samples: integer
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NFC:SCONfiguration:TNSamples?')
		return Conversions.str_to_int(response)

	def get_ts_duration(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:NFC:SCONfiguration:TSDuration \n
		Snippet: value: float = driver.source.bb.nfc.sconfiguration.get_ts_duration() \n
		Queries the total sequence duration for the current settings. \n
			:return: ts_duration: float
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NFC:SCONfiguration:TSDuration?')
		return Conversions.str_to_float(response)
