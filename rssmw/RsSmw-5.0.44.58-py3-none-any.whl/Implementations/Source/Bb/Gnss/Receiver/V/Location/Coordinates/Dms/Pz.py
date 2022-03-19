from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal.StructBase import StructBase
from ..........Internal.ArgStruct import ArgStruct
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pz:
	"""Pz commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pz", core, parent)

	# noinspection PyTypeChecker
	class PzStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Longitude_Deg: int: integer Defines the longitude degrees. Range: 0 to 180
			- Longitude_Min: int: integer Defines the longitude minutes. Range: 0 to 59
			- Longitude_Sec: float: float Defines the longitude seconds. Range: 0 to 59.999
			- Longitude_Dir: str: EAST | WEST Defines the longitude direction.
			- Latitude_Deg: int: integer Defines the latitude degrees. Range: 0 to 90
			- Latitude_Min: int: integer Defines the latitude minutes. Range: 0 to 59
			- Latitude_Sec: float: float Defines the latitude seconds. Range: 0 to 59.999
			- Latitude_Dir: str: NORTh | SOUTh Defines the latitude direction.
			- Altitude: float: float Defines the altitude. The altitude value is the height above the reference ellipsoid. Range: -10E3 to 50E6"""
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

	def set(self, structure: PzStruct, vehicle=repcap.Vehicle.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:LOCation:COORdinates:DMS:PZ \n
		Snippet with structure: \n
		structure = driver.source.bb.gnss.receiver.v.location.coordinates.dms.pz.PzStruct() \n
		structure.Longitude_Deg: int = 1 \n
		structure.Longitude_Min: int = 1 \n
		structure.Longitude_Sec: float = 1.0 \n
		structure.Longitude_Dir: str = '1' \n
		structure.Latitude_Deg: int = 1 \n
		structure.Latitude_Min: int = 1 \n
		structure.Latitude_Sec: float = 1.0 \n
		structure.Latitude_Dir: str = '1' \n
		structure.Altitude: float = 1.0 \n
		driver.source.bb.gnss.receiver.v.location.coordinates.dms.pz.set(structure, vehicle = repcap.Vehicle.Default) \n
		Defines the coordinates of the geographic location of the GNSS receiver in degrees, minutes and seconds. \n
			:param structure: for set value, see the help for PzStruct structure arguments.
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
		"""
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		self._core.io.write_struct(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:LOCation:COORdinates:DMS:PZ', structure)

	def get(self, vehicle=repcap.Vehicle.Default) -> PzStruct:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:LOCation:COORdinates:DMS:PZ \n
		Snippet: value: PzStruct = driver.source.bb.gnss.receiver.v.location.coordinates.dms.pz.get(vehicle = repcap.Vehicle.Default) \n
		Defines the coordinates of the geographic location of the GNSS receiver in degrees, minutes and seconds. \n
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
			:return: structure: for return value, see the help for PzStruct structure arguments."""
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:LOCation:COORdinates:DMS:PZ?', self.__class__.PzStruct())
