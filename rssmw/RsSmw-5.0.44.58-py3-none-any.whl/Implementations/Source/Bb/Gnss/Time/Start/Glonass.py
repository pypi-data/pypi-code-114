from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Glonass:
	"""Glonass commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("glonass", core, parent)

	# noinspection PyTypeChecker
	class DateStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Year: int: integer Range: 1980 to 9999
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

	def get_date(self) -> DateStruct:
		"""SCPI: [SOURce<HW>]:BB:GNSS:TIME:STARt:GLONass:DATE \n
		Snippet: value: DateStruct = driver.source.bb.gnss.time.start.glonass.get_date() \n
		Queries the date at the simulation start time of the selected navigation standard. \n
			:return: structure: for return value, see the help for DateStruct structure arguments.
		"""
		return self._core.io.query_struct('SOURce<HwInstance>:BB:GNSS:TIME:STARt:GLONass:DATE?', self.__class__.DateStruct())

	def get_offset(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:TIME:STARt:GLONass:OFFSet \n
		Snippet: value: float = driver.source.bb.gnss.time.start.glonass.get_offset() \n
		Queries the time offset between the time in the navigation standard and UTC. \n
			:return: utc_offset: float Range: -1E6 to 1E6
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:TIME:STARt:GLONass:OFFSet?')
		return Conversions.str_to_float(response)

	# noinspection PyTypeChecker
	class TimeStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
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

	def get_time(self) -> TimeStruct:
		"""SCPI: [SOURce<HW>]:BB:GNSS:TIME:STARt:GLONass:TIME \n
		Snippet: value: TimeStruct = driver.source.bb.gnss.time.start.glonass.get_time() \n
		Queries the simulation start time of the selected navigation standard. \n
			:return: structure: for return value, see the help for TimeStruct structure arguments.
		"""
		return self._core.io.query_struct('SOURce<HwInstance>:BB:GNSS:TIME:STARt:GLONass:TIME?', self.__class__.TimeStruct())
