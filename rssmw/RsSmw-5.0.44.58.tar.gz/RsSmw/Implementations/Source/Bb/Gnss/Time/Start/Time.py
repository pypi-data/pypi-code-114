from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Time:
	"""Time commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("time", core, parent)

	def set(self, hour: int, minute: int, second: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:TIME:STARt:TIME \n
		Snippet: driver.source.bb.gnss.time.start.time.set(hour = 1, minute = 1, second = 1.0) \n
		If the time base is UTC, sets the simulation start time in UTC time format. \n
			:param hour: integer Range: 0 to 23
			:param minute: integer Range: 0 to 59
			:param second: float Range: 0 to 59.999
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('hour', hour, DataType.Integer), ArgSingle('minute', minute, DataType.Integer), ArgSingle('second', second, DataType.Float))
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:TIME:STARt:TIME {param}'.rstrip())

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

	def get(self) -> TimeStruct:
		"""SCPI: [SOURce<HW>]:BB:GNSS:TIME:STARt:TIME \n
		Snippet: value: TimeStruct = driver.source.bb.gnss.time.start.time.get() \n
		If the time base is UTC, sets the simulation start time in UTC time format. \n
			:return: structure: for return value, see the help for TimeStruct structure arguments."""
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:GNSS:TIME:STARt:TIME?', self.__class__.TimeStruct())
