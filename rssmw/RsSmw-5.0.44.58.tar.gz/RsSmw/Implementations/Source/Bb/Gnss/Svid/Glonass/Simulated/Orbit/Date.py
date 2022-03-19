from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Date:
	"""Date commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("date", core, parent)

	def set(self, year: int, month: int, day: int, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GLONass:SIMulated:ORBit:DATE \n
		Snippet: driver.source.bb.gnss.svid.glonass.simulated.orbit.date.set(year = 1, month = 1, day = 1, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the reference date. \n
			:param year: integer Range: 1996 to 9999
			:param month: integer Range: 1 to 12
			:param day: integer Range: 1 to 31
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('year', year, DataType.Integer), ArgSingle('month', month, DataType.Integer), ArgSingle('day', day, DataType.Integer))
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GLONass:SIMulated:ORBit:DATE {param}'.rstrip())

	# noinspection PyTypeChecker
	class DateStruct(StructBase):
		"""Response structure. Fields: \n
			- Year: int: integer Range: 1996 to 9999
			- Month: int: integer Range: 1 to 12
			- Day: int: integer Range: 1 to 31"""
		__meta_args_list = [
			ArgStruct.scalar_int('Year'),
			ArgStruct.scalar_int('Month'),
			ArgStruct.scalar_int('Day')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Year: int = None
			self.Month: int = None
			self.Day: int = None

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> DateStruct:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GLONass:SIMulated:ORBit:DATE \n
		Snippet: value: DateStruct = driver.source.bb.gnss.svid.glonass.simulated.orbit.date.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the reference date. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: structure: for return value, see the help for DateStruct structure arguments."""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GLONass:SIMulated:ORBit:DATE?', self.__class__.DateStruct())
