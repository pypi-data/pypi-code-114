from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Utc:
	"""Utc commands group definition. 9 total commands, 3 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("utc", core, parent)

	@property
	def aone(self):
		"""aone commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_aone'):
			from .Aone import Aone
			self._aone = Aone(self._core, self._cmd_group)
		return self._aone

	@property
	def azero(self):
		"""azero commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_azero'):
			from .Azero import Azero
			self._azero = Azero(self._core, self._cmd_group)
		return self._azero

	@property
	def tot(self):
		"""tot commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_tot'):
			from .Tot import Tot
			self._tot = Tot(self._core, self._cmd_group)
		return self._tot

	# noinspection PyTypeChecker
	class DateStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
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

	def get_date(self) -> DateStruct:
		"""SCPI: [SOURce<HW>]:BB:GNSS:TIME:CONVersion:UTCSu:UTC:DATE \n
		Snippet: value: DateStruct = driver.source.bb.gnss.time.conversion.utcsu.utc.get_date() \n
		Enters the date for the UTC-UTC(SU) data in DMS format. \n
			:return: structure: for return value, see the help for DateStruct structure arguments.
		"""
		return self._core.io.query_struct('SOURce<HwInstance>:BB:GNSS:TIME:CONVersion:UTCSu:UTC:DATE?', self.__class__.DateStruct())

	def get_ioffset(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:TIME:CONVersion:UTCSu:UTC:IOFFset \n
		Snippet: value: int = driver.source.bb.gnss.time.conversion.utcsu.utc.get_ioffset() \n
		Queries the integer offset. \n
			:return: integer_offset: integer Range: 0 to 604800
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:TIME:CONVersion:UTCSu:UTC:IOFFset?')
		return Conversions.str_to_int(response)

	def get_wnot(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:TIME:CONVersion:UTCSu:UTC:WNOT \n
		Snippet: value: int = driver.source.bb.gnss.time.conversion.utcsu.utc.get_wnot() \n
		Sets the UTC data reference week number, WNt. \n
			:return: wnot: integer Range: 0 to 255
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:TIME:CONVersion:UTCSu:UTC:WNOT?')
		return Conversions.str_to_int(response)

	def set_wnot(self, wnot: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:TIME:CONVersion:UTCSu:UTC:WNOT \n
		Snippet: driver.source.bb.gnss.time.conversion.utcsu.utc.set_wnot(wnot = 1) \n
		Sets the UTC data reference week number, WNt. \n
			:param wnot: integer Range: 0 to 255
		"""
		param = Conversions.decimal_value_to_str(wnot)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:TIME:CONVersion:UTCSu:UTC:WNOT {param}')

	def clone(self) -> 'Utc':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Utc(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
