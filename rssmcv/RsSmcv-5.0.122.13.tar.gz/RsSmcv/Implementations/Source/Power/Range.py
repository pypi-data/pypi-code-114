from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Range:
	"""Range commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("range", core, parent)

	def get_lower(self) -> float:
		"""SCPI: [SOURce<HW>]:POWer:RANGe:LOWer \n
		Snippet: value: float = driver.source.power.range.get_lower() \n
		Queries the current interruption-free range of the level. \n
			:return: lower: float Unit: dBm
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:POWer:RANGe:LOWer?')
		return Conversions.str_to_float(response)

	def get_upper(self) -> float:
		"""SCPI: [SOURce<HW>]:POWer:RANGe:UPPer \n
		Snippet: value: float = driver.source.power.range.get_upper() \n
		Queries the current interruption-free range of the level. \n
			:return: upper: float Unit: dBm
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:POWer:RANGe:UPPer?')
		return Conversions.str_to_float(response)
