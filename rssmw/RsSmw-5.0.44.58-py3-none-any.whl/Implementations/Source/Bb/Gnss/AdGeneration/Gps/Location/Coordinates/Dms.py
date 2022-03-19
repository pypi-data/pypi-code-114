from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dms:
	"""Dms commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dms", core, parent)

	# noinspection PyTypeChecker
	class PzStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Fields: \n
			- Longitude_Deg: int: integer Range: 0 to 180
			- Longitude_Min: int: integer Range: 0 to 59
			- Longitude_Sec: float: float Range: 0 to 59.999
			- Longitude_Dir: str: select
			- Latitude_Deg: int: integer Range: 0 to 90
			- Latitude_Min: int: integer Range: 0 to 59
			- Latitude_Sec: float: float Range: 0 to 59.999
			- Latitude_Dir: str: select
			- Altitude: float: float Range: -10E3 to 50E6"""
		__meta_args_list = [
			ArgStruct.scalar_int('Longitude_Deg'),
			ArgStruct.scalar_int('Longitude_Min'),
			ArgStruct.scalar_float('Longitude_Sec'),
			ArgStruct.scalar_str('Longitude_Dir'),
			ArgStruct.scalar_int('Latitude_Deg'),
			ArgStruct.scalar_int('Latitude_Min'),
			ArgStruct.scalar_float('Latitude_Sec'),
			ArgStruct.scalar_str('Latitude_Dir'),
			ArgStruct.scalar_float('Altitude')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Longitude_Deg: int = None
			self.Longitude_Min: int = None
			self.Longitude_Sec: float = None
			self.Longitude_Dir: str = None
			self.Latitude_Deg: int = None
			self.Latitude_Min: int = None
			self.Latitude_Sec: float = None
			self.Latitude_Dir: str = None
			self.Altitude: float = None

	def get_pz(self) -> PzStruct:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ADGeneration:GPS:LOCation:COORdinates:DMS:PZ \n
		Snippet: value: PzStruct = driver.source.bb.gnss.adGeneration.gps.location.coordinates.dms.get_pz() \n
		Sets the geographic reference location in degrees, minutes and seconds. \n
			:return: structure: for return value, see the help for PzStruct structure arguments.
		"""
		return self._core.io.query_struct('SOURce<HwInstance>:BB:GNSS:ADGeneration:GPS:LOCation:COORdinates:DMS:PZ?', self.__class__.PzStruct())

	def set_pz(self, value: PzStruct) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ADGeneration:GPS:LOCation:COORdinates:DMS:PZ \n
		Snippet with structure: \n
		structure = driver.source.bb.gnss.adGeneration.gps.location.coordinates.dms.PzStruct() \n
		structure.Longitude_Deg: int = 1 \n
		structure.Longitude_Min: int = 1 \n
		structure.Longitude_Sec: float = 1.0 \n
		structure.Longitude_Dir: str = '1' \n
		structure.Latitude_Deg: int = 1 \n
		structure.Latitude_Min: int = 1 \n
		structure.Latitude_Sec: float = 1.0 \n
		structure.Latitude_Dir: str = '1' \n
		structure.Altitude: float = 1.0 \n
		driver.source.bb.gnss.adGeneration.gps.location.coordinates.dms.set_pz(value = structure) \n
		Sets the geographic reference location in degrees, minutes and seconds. \n
			:param value: see the help for PzStruct structure arguments.
		"""
		self._core.io.write_struct('SOURce<HwInstance>:BB:GNSS:ADGeneration:GPS:LOCation:COORdinates:DMS:PZ', value)

	# noinspection PyTypeChecker
	class WgsStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Fields: \n
			- Longitude_Deg: int: integer Range: 0 to 180
			- Longitude_Min: int: integer Range: 0 to 59
			- Longitude_Sec: float: float Range: 0 to 59.999
			- Longitude_Dir: str: select
			- Latitude_Deg: int: integer Range: 0 to 90
			- Latitude_Min: int: integer Range: 0 to 59
			- Latitude_Sec: float: float Range: 0 to 59.999
			- Latitude_Dir: str: select
			- Altitude: float: float Range: -10E3 to 50E6"""
		__meta_args_list = [
			ArgStruct.scalar_int('Longitude_Deg'),
			ArgStruct.scalar_int('Longitude_Min'),
			ArgStruct.scalar_float('Longitude_Sec'),
			ArgStruct.scalar_str('Longitude_Dir'),
			ArgStruct.scalar_int('Latitude_Deg'),
			ArgStruct.scalar_int('Latitude_Min'),
			ArgStruct.scalar_float('Latitude_Sec'),
			ArgStruct.scalar_str('Latitude_Dir'),
			ArgStruct.scalar_float('Altitude')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Longitude_Deg: int = None
			self.Longitude_Min: int = None
			self.Longitude_Sec: float = None
			self.Longitude_Dir: str = None
			self.Latitude_Deg: int = None
			self.Latitude_Min: int = None
			self.Latitude_Sec: float = None
			self.Latitude_Dir: str = None
			self.Altitude: float = None

	def get_wgs(self) -> WgsStruct:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ADGeneration:GPS:LOCation:COORdinates:DMS:[WGS] \n
		Snippet: value: WgsStruct = driver.source.bb.gnss.adGeneration.gps.location.coordinates.dms.get_wgs() \n
		Sets the geographic reference location in degrees, minutes and seconds. \n
			:return: structure: for return value, see the help for WgsStruct structure arguments.
		"""
		return self._core.io.query_struct('SOURce<HwInstance>:BB:GNSS:ADGeneration:GPS:LOCation:COORdinates:DMS:WGS?', self.__class__.WgsStruct())

	def set_wgs(self, value: WgsStruct) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ADGeneration:GPS:LOCation:COORdinates:DMS:[WGS] \n
		Snippet with structure: \n
		structure = driver.source.bb.gnss.adGeneration.gps.location.coordinates.dms.WgsStruct() \n
		structure.Longitude_Deg: int = 1 \n
		structure.Longitude_Min: int = 1 \n
		structure.Longitude_Sec: float = 1.0 \n
		structure.Longitude_Dir: str = '1' \n
		structure.Latitude_Deg: int = 1 \n
		structure.Latitude_Min: int = 1 \n
		structure.Latitude_Sec: float = 1.0 \n
		structure.Latitude_Dir: str = '1' \n
		structure.Altitude: float = 1.0 \n
		driver.source.bb.gnss.adGeneration.gps.location.coordinates.dms.set_wgs(value = structure) \n
		Sets the geographic reference location in degrees, minutes and seconds. \n
			:param value: see the help for WgsStruct structure arguments.
		"""
		self._core.io.write_struct('SOURce<HwInstance>:BB:GNSS:ADGeneration:GPS:LOCation:COORdinates:DMS:WGS', value)
