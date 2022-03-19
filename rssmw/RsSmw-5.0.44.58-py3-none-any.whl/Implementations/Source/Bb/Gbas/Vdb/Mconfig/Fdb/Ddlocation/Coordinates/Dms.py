from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal.StructBase import StructBase
from ..........Internal.ArgStruct import ArgStruct
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dms:
	"""Dms commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dms", core, parent)

	# noinspection PyTypeChecker
	class DmsStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Longitude_Deg: int: integer Range: 0 to 0
			- Longitude_Min: int: integer Range: 0 to 10
			- Longitude_Sec: float: float Range: 0 to 55.358
			- Longitude_Dir: str: select
			- Latitude_Deg: int: integer Range: 0 to 0
			- Latitude_Min: int: integer Range: 0 to 5
			- Latitude_Sec: float: float Range: 0 to 27.679
			- Latitude_Dir: str: select"""
		__meta_args_list = [
			ArgStruct.scalar_int('Longitude_Deg'),
			ArgStruct.scalar_int('Longitude_Min'),
			ArgStruct.scalar_float('Longitude_Sec'),
			ArgStruct.scalar_str('Longitude_Dir'),
			ArgStruct.scalar_int('Latitude_Deg'),
			ArgStruct.scalar_int('Latitude_Min'),
			ArgStruct.scalar_float('Latitude_Sec'),
			ArgStruct.scalar_str('Latitude_Dir')]

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

	def set(self, structure: DmsStruct, vdbTransmitter=repcap.VdbTransmitter.Default, fdbTransmitter=repcap.FdbTransmitter.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:FDB<ST>:DDLocation:COORdinates:DMS \n
		Snippet with structure: \n
		structure = driver.source.bb.gbas.vdb.mconfig.fdb.ddlocation.coordinates.dms.DmsStruct() \n
		structure.Longitude_Deg: int = 1 \n
		structure.Longitude_Min: int = 1 \n
		structure.Longitude_Sec: float = 1.0 \n
		structure.Longitude_Dir: str = '1' \n
		structure.Latitude_Deg: int = 1 \n
		structure.Latitude_Min: int = 1 \n
		structure.Latitude_Sec: float = 1.0 \n
		structure.Latitude_Dir: str = '1' \n
		driver.source.bb.gbas.vdb.mconfig.fdb.ddlocation.coordinates.dms.set(structure, vdbTransmitter = repcap.VdbTransmitter.Default, fdbTransmitter = repcap.FdbTransmitter.Default) \n
		Defines the coordinates of the Delta DERP location in degrees, minutes and seconds. \n
			:param structure: for set value, see the help for DmsStruct structure arguments.
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
			:param fdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fdb')
		"""
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		fdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(fdbTransmitter, repcap.FdbTransmitter)
		self._core.io.write_struct(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:FDB{fdbTransmitter_cmd_val}:DDLocation:COORdinates:DMS', structure)

	def get(self, vdbTransmitter=repcap.VdbTransmitter.Default, fdbTransmitter=repcap.FdbTransmitter.Default) -> DmsStruct:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:FDB<ST>:DDLocation:COORdinates:DMS \n
		Snippet: value: DmsStruct = driver.source.bb.gbas.vdb.mconfig.fdb.ddlocation.coordinates.dms.get(vdbTransmitter = repcap.VdbTransmitter.Default, fdbTransmitter = repcap.FdbTransmitter.Default) \n
		Defines the coordinates of the Delta DERP location in degrees, minutes and seconds. \n
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
			:param fdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fdb')
			:return: structure: for return value, see the help for DmsStruct structure arguments."""
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		fdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(fdbTransmitter, repcap.FdbTransmitter)
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:FDB{fdbTransmitter_cmd_val}:DDLocation:COORdinates:DMS?', self.__class__.DmsStruct())
