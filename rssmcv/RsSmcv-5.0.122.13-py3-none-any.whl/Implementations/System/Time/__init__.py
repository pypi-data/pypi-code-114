from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Types import DataType
from ....Internal.Utilities import trim_str_response
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Time:
	"""Time commands group definition. 11 total commands, 3 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("time", core, parent)

	@property
	def daylightSavingTime(self):
		"""daylightSavingTime commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_daylightSavingTime'):
			from .DaylightSavingTime import DaylightSavingTime
			self._daylightSavingTime = DaylightSavingTime(self._core, self._cmd_group)
		return self._daylightSavingTime

	@property
	def hrTimer(self):
		"""hrTimer commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_hrTimer'):
			from .HrTimer import HrTimer
			self._hrTimer = HrTimer(self._core, self._cmd_group)
		return self._hrTimer

	@property
	def zone(self):
		"""zone commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_zone'):
			from .Zone import Zone
			self._zone = Zone(self._core, self._cmd_group)
		return self._zone

	def set(self, hour: List[int], minute: int, second: int) -> None:
		"""SCPI: SYSTem:TIME \n
		Snippet: driver.system.time.set(hour = [1, 2, 3], minute = 1, second = 1) \n
		Queries or sets the time for the instrument-internal clock. This is a password-protected function. Unlock the protection
		level 1 to access it. See method RsSmcv.System.Protect.State.set. \n
			:param hour: integer Range: 0 to 23
			:param minute: integer Range: 0 to 59
			:param second: integer Range: 0 to 59
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('hour', hour, DataType.IntegerList, None), ArgSingle('minute', minute, DataType.Integer), ArgSingle('second', second, DataType.Integer))
		self._core.io.write(f'SYSTem:TIME {param}'.rstrip())

	# noinspection PyTypeChecker
	class TimeStruct(StructBase):
		"""Response structure. Fields: \n
			- Hour: List[int]: integer Range: 0 to 23
			- Minute: int: integer Range: 0 to 59
			- Second: int: integer Range: 0 to 59"""
		__meta_args_list = [
			ArgStruct('Hour', DataType.IntegerList, None, False, True, 1),
			ArgStruct.scalar_int('Minute'),
			ArgStruct.scalar_int('Second')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Hour: List[int] = None
			self.Minute: int = None
			self.Second: int = None

	def get(self) -> TimeStruct:
		"""SCPI: SYSTem:TIME \n
		Snippet: value: TimeStruct = driver.system.time.get() \n
		Queries or sets the time for the instrument-internal clock. This is a password-protected function. Unlock the protection
		level 1 to access it. See method RsSmcv.System.Protect.State.set. \n
			:return: structure: for return value, see the help for TimeStruct structure arguments."""
		return self._core.io.query_struct(f'SYSTem:TIME?', self.__class__.TimeStruct())

	def get_local(self) -> str:
		"""SCPI: SYSTem:TIME:LOCal \n
		Snippet: value: str = driver.system.time.get_local() \n
		No command help available \n
			:return: pseudo_string: No help available
		"""
		response = self._core.io.query_str('SYSTem:TIME:LOCal?')
		return trim_str_response(response)

	def set_local(self, pseudo_string: str) -> None:
		"""SCPI: SYSTem:TIME:LOCal \n
		Snippet: driver.system.time.set_local(pseudo_string = '1') \n
		No command help available \n
			:param pseudo_string: No help available
		"""
		param = Conversions.value_to_quoted_str(pseudo_string)
		self._core.io.write(f'SYSTem:TIME:LOCal {param}')

	def get_utc(self) -> str:
		"""SCPI: SYSTem:TIME:UTC \n
		Snippet: value: str = driver.system.time.get_utc() \n
		No command help available \n
			:return: pseudo_string: No help available
		"""
		response = self._core.io.query_str('SYSTem:TIME:UTC?')
		return trim_str_response(response)

	def set_utc(self, pseudo_string: str) -> None:
		"""SCPI: SYSTem:TIME:UTC \n
		Snippet: driver.system.time.set_utc(pseudo_string = '1') \n
		No command help available \n
			:param pseudo_string: No help available
		"""
		param = Conversions.value_to_quoted_str(pseudo_string)
		self._core.io.write(f'SYSTem:TIME:UTC {param}')

	def clone(self) -> 'Time':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Time(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
