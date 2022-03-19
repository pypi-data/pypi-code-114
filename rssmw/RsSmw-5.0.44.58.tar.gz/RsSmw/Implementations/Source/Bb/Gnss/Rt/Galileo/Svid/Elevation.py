from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Elevation:
	"""Elevation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("elevation", core, parent)

	def get(self, time_basis: enums.TimeBasis, year: int, month: int, day: int, hour: int, minutes: int, seconds: float, week_number: int, time_of_week: float, satelliteSvid=repcap.SatelliteSvid.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RT:GALileo:SVID<CH>:ELEVation \n
		Snippet: value: float = driver.source.bb.gnss.rt.galileo.svid.elevation.get(time_basis = enums.TimeBasis.BDT, year = 1, month = 1, day = 1, hour = 1, minutes = 1, seconds = 1.0, week_number = 1, time_of_week = 1.0, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Queries the satellite elevation in the selected moment of time. The required query parameters, depend on the selected
		timebase. \n
			:param time_basis: UTC | GPS | GST | GLO | BDT
			:param year: integer Required for TimeBasis = UTC Range: 1980 to 9999
			:param month: integer Required for TimeBasis = UTC Range: 1 to 12
			:param day: integer Required for TimeBasis = UTC Range: 1 to 31
			:param hour: integer Required for TimeBasis = UTC Range: 0 to 23
			:param minutes: integer Required for TimeBasis = UTC Range: 0 to 59
			:param seconds: float Required for TimeBasis = UTC Range: 0 to 59.999
			:param week_number: integer Required for TimeBasis = GPS|GST|BDT Range: 0 to 529947
			:param time_of_week: float Required for TimeBasis = GPS|GST|BDT Range: 0 to 604799.999
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: elevation: float"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('time_basis', time_basis, DataType.Enum, enums.TimeBasis), ArgSingle('year', year, DataType.Integer), ArgSingle('month', month, DataType.Integer), ArgSingle('day', day, DataType.Integer), ArgSingle('hour', hour, DataType.Integer), ArgSingle('minutes', minutes, DataType.Integer), ArgSingle('seconds', seconds, DataType.Float), ArgSingle('week_number', week_number, DataType.Integer), ArgSingle('time_of_week', time_of_week, DataType.Float))
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:RT:GALileo:SVID{satelliteSvid_cmd_val}:ELEVation? {param}'.rstrip())
		return Conversions.str_to_float(response)
