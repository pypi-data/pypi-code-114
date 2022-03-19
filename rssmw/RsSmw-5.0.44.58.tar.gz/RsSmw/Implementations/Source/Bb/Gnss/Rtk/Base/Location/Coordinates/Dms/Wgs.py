from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal.StructBase import StructBase
from ..........Internal.ArgStruct import ArgStruct
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Wgs:
	"""Wgs commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("wgs", core, parent)

	# noinspection PyTypeChecker
	class WgsStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Longitude_Deg: int: No parameter help available
			- Longitude_Min: int: No parameter help available
			- Longitude_Sec: float: No parameter help available
			- Longitude_Dir: str: No parameter help available
			- Latitude_Deg: int: No parameter help available
			- Latitude_Min: int: No parameter help available
			- Latitude_Sec: float: No parameter help available
			- Latitude_Dir: str: No parameter help available
			- Altitude: float: No parameter help available"""
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

	def set(self, structure: WgsStruct, baseSt=repcap.BaseSt.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RTK:BASE<ST>:LOCation:COORdinates:DMS:[WGS] \n
		Snippet with structure: \n
		structure = driver.source.bb.gnss.rtk.base.location.coordinates.dms.wgs.WgsStruct() \n
		structure.Longitude_Deg: int = 1 \n
		structure.Longitude_Min: int = 1 \n
		structure.Longitude_Sec: float = 1.0 \n
		structure.Longitude_Dir: str = '1' \n
		structure.Latitude_Deg: int = 1 \n
		structure.Latitude_Min: int = 1 \n
		structure.Latitude_Sec: float = 1.0 \n
		structure.Latitude_Dir: str = '1' \n
		structure.Altitude: float = 1.0 \n
		driver.source.bb.gnss.rtk.base.location.coordinates.dms.wgs.set(structure, baseSt = repcap.BaseSt.Default) \n
		No command help available \n
			:param structure: for set value, see the help for WgsStruct structure arguments.
			:param baseSt: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Base')
		"""
		baseSt_cmd_val = self._cmd_group.get_repcap_cmd_value(baseSt, repcap.BaseSt)
		self._core.io.write_struct(f'SOURce<HwInstance>:BB:GNSS:RTK:BASE{baseSt_cmd_val}:LOCation:COORdinates:DMS:WGS', structure)

	def get(self, baseSt=repcap.BaseSt.Default) -> WgsStruct:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RTK:BASE<ST>:LOCation:COORdinates:DMS:[WGS] \n
		Snippet: value: WgsStruct = driver.source.bb.gnss.rtk.base.location.coordinates.dms.wgs.get(baseSt = repcap.BaseSt.Default) \n
		No command help available \n
			:param baseSt: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Base')
			:return: structure: for return value, see the help for WgsStruct structure arguments."""
		baseSt_cmd_val = self._cmd_group.get_repcap_cmd_value(baseSt, repcap.BaseSt)
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:GNSS:RTK:BASE{baseSt_cmd_val}:LOCation:COORdinates:DMS:WGS?', self.__class__.WgsStruct())
