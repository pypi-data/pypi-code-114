from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	def get_multiplier(self) -> int:
		"""SCPI: [SOURce<HW>]:FREQuency:CONVerter:EXTernal:FREQuency:MULTiplier \n
		Snippet: value: int = driver.source.frequency.converter.external.frequency.get_multiplier() \n
		No command help available \n
			:return: freq_multiplier: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FREQuency:CONVerter:EXTernal:FREQuency:MULTiplier?')
		return Conversions.str_to_int(response)
