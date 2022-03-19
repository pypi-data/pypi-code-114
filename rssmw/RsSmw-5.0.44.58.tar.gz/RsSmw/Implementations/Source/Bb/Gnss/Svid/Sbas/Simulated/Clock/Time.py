from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Time:
	"""Time commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("time", core, parent)

	def set(self, hour: int, minute: int, second: float, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:SBAS:SIMulated:CLOCk:TIME \n
		Snippet: driver.source.bb.gnss.svid.sbas.simulated.clock.time.set(hour = 1, minute = 1, second = 1.0, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the reference time. \n
			:param hour: integer Range: 0 to 23
			:param minute: integer Range: 0 to 59
			:param second: float Range: 0 to 59.999
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('hour', hour, DataType.Integer), ArgSingle('minute', minute, DataType.Integer), ArgSingle('second', second, DataType.Float))
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:SBAS:SIMulated:CLOCk:TIME {param}'.rstrip())

	# noinspection PyTypeChecker
	class TimeStruct(StructBase):
		"""Response structure. Fields: \n
			- Hour: int: integer Range: 0 to 23
			- Minute: int: integer Range: 0 to 59
			- Second: float: float Range: 0 to 59.999"""
		__meta_args_list = [
			ArgStruct.scalar_int('Hour'),
			ArgStruct.scalar_int('Minute'),
			ArgStruct.scalar_float('Second')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Hour: int = None
			self.Minute: int = None
			self.Second: float = None

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> TimeStruct:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:SBAS:SIMulated:CLOCk:TIME \n
		Snippet: value: TimeStruct = driver.source.bb.gnss.svid.sbas.simulated.clock.time.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the reference time. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: structure: for return value, see the help for TimeStruct structure arguments."""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:SBAS:SIMulated:CLOCk:TIME?', self.__class__.TimeStruct())
