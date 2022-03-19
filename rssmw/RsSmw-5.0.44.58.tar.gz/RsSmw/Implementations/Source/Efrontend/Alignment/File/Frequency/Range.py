from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Range:
	"""Range commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("range", core, parent)

	def get_lower(self) -> float:
		"""SCPI: [SOURce<HW>]:EFRontend:ALIGnment:FILE:FREQuency:RANGe:LOWer \n
		Snippet: value: float = driver.source.efrontend.alignment.file.frequency.range.get_lower() \n
		Queries the upper/lower frequency range of IF values required at the connected external frontend. We recommend that you
		cover this range in the cable correction *.s2p file. \n
			:return: cable_corr_freq_lo: float
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:EFRontend:ALIGnment:FILE:FREQuency:RANGe:LOWer?')
		return Conversions.str_to_float(response)

	def get_upper(self) -> float:
		"""SCPI: [SOURce<HW>]:EFRontend:ALIGnment:FILE:FREQuency:RANGe:UPPer \n
		Snippet: value: float = driver.source.efrontend.alignment.file.frequency.range.get_upper() \n
		Queries the upper/lower frequency range of IF values required at the connected external frontend. We recommend that you
		cover this range in the cable correction *.s2p file. \n
			:return: cable_corr_freq_up: float
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:EFRontend:ALIGnment:FILE:FREQuency:RANGe:UPPer?')
		return Conversions.str_to_float(response)
