from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Time:
	"""Time commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("time", core, parent)

	# noinspection PyTypeChecker
	def get_next(self) -> enums.Atsc30MinTimeToNext:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:INFO:BOOTstrap:TIME:NEXT \n
		Snippet: value: enums.Atsc30MinTimeToNext = driver.source.bb.a3Tsc.info.bootstrap.time.get_next() \n
		Queries minimum time interval to the next frame that matches the same major and minor version number of the current frame. \n
			:return: min_timeto_next: N50| N100| N150| N200| N250| N300| N350| N400| N500| N600| N700| N800| N900| N1000| N1100| N1200| N1300| N1400| N1500| N1600| N1700| N1900| N2100| N2300| N2500| N2700| N2900| N3300| N3700| N4100| N4500| N4900| N5300| NOTapplicable
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:INFO:BOOTstrap:TIME:NEXT?')
		return Conversions.str_to_scalar_enum(response, enums.Atsc30MinTimeToNext)
