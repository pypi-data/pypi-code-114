from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Beidou:
	"""Beidou commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("beidou", core, parent)

	def get_offset(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:TIME:STARt:BEIDou:OFFSet \n
		Snippet: value: float = driver.source.bb.gnss.time.start.beidou.get_offset() \n
		Queries the time offset between the time in the navigation standard and UTC. \n
			:return: utc_offset: float Range: -1E6 to 1E6
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:TIME:STARt:BEIDou:OFFSet?')
		return Conversions.str_to_float(response)

	def get_to_week(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:TIME:STARt:BEIDou:TOWeek \n
		Snippet: value: float = driver.source.bb.gnss.time.start.beidou.get_to_week() \n
		Queries the time of week at the simulation start of the selected navigation standard. \n
			:return: tow: float Range: 0 to 604799.999
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:TIME:STARt:BEIDou:TOWeek?')
		return Conversions.str_to_float(response)

	def get_wnumber(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:TIME:STARt:BEIDou:WNUMber \n
		Snippet: value: int = driver.source.bb.gnss.time.start.beidou.get_wnumber() \n
		Queries the week number at the simulation start of the selected navigation standard. \n
			:return: system_week_number: integer Range: 0 to 10000
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:TIME:STARt:BEIDou:WNUMber?')
		return Conversions.str_to_int(response)
