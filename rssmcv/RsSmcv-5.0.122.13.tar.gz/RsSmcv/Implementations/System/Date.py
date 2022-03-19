from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Types import DataType
from ...Internal.Utilities import trim_str_response
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ...Internal.ArgSingleList import ArgSingleList
from ...Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Date:
	"""Date commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("date", core, parent)

	def set(self, year: List[int], month: int, day: int) -> None:
		"""SCPI: SYSTem:DATE \n
		Snippet: driver.system.date.set(year = [1, 2, 3], month = 1, day = 1) \n
		Queries or sets the date for the instrument-internal calendar. This is a password-protected function.
		Unlock the protection level 1 to access it. See method RsSmcv.System.Protect.State.set. \n
			:param year: integer
			:param month: integer Range: 1 to 12
			:param day: integer Range: 1 to 31
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('year', year, DataType.IntegerList, None), ArgSingle('month', month, DataType.Integer), ArgSingle('day', day, DataType.Integer))
		self._core.io.write(f'SYSTem:DATE {param}'.rstrip())

	# noinspection PyTypeChecker
	class DateStruct(StructBase):
		"""Response structure. Fields: \n
			- Year: List[int]: integer
			- Month: int: integer Range: 1 to 12
			- Day: int: integer Range: 1 to 31"""
		__meta_args_list = [
			ArgStruct('Year', DataType.IntegerList, None, False, True, 1),
			ArgStruct.scalar_int('Month'),
			ArgStruct.scalar_int('Day')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Year: List[int] = None
			self.Month: int = None
			self.Day: int = None

	def get(self) -> DateStruct:
		"""SCPI: SYSTem:DATE \n
		Snippet: value: DateStruct = driver.system.date.get() \n
		Queries or sets the date for the instrument-internal calendar. This is a password-protected function.
		Unlock the protection level 1 to access it. See method RsSmcv.System.Protect.State.set. \n
			:return: structure: for return value, see the help for DateStruct structure arguments."""
		return self._core.io.query_struct(f'SYSTem:DATE?', self.__class__.DateStruct())

	def get_local(self) -> str:
		"""SCPI: SYSTem:DATE:LOCal \n
		Snippet: value: str = driver.system.date.get_local() \n
		No command help available \n
			:return: pseudo_string: No help available
		"""
		response = self._core.io.query_str('SYSTem:DATE:LOCal?')
		return trim_str_response(response)

	def set_local(self, pseudo_string: str) -> None:
		"""SCPI: SYSTem:DATE:LOCal \n
		Snippet: driver.system.date.set_local(pseudo_string = '1') \n
		No command help available \n
			:param pseudo_string: No help available
		"""
		param = Conversions.value_to_quoted_str(pseudo_string)
		self._core.io.write(f'SYSTem:DATE:LOCal {param}')

	def get_utc(self) -> str:
		"""SCPI: SYSTem:DATE:UTC \n
		Snippet: value: str = driver.system.date.get_utc() \n
		No command help available \n
			:return: pseudo_string: No help available
		"""
		response = self._core.io.query_str('SYSTem:DATE:UTC?')
		return trim_str_response(response)

	def set_utc(self, pseudo_string: str) -> None:
		"""SCPI: SYSTem:DATE:UTC \n
		Snippet: driver.system.date.set_utc(pseudo_string = '1') \n
		No command help available \n
			:param pseudo_string: No help available
		"""
		param = Conversions.value_to_quoted_str(pseudo_string)
		self._core.io.write(f'SYSTem:DATE:UTC {param}')
