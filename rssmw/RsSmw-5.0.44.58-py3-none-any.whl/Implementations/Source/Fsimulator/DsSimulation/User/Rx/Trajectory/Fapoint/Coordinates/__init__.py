from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal.StructBase import StructBase
from ..........Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Coordinates:
	"""Coordinates commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("coordinates", core, parent)

	@property
	def xyz(self):
		"""xyz commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_xyz'):
			from .Xyz import Xyz
			self._xyz = Xyz(self._core, self._cmd_group)
		return self._xyz

	@property
	def decimal(self):
		"""decimal commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_decimal'):
			from .Decimal import Decimal
			self._decimal = Decimal(self._core, self._cmd_group)
		return self._decimal

	# noinspection PyTypeChecker
	class DmsStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Fields: \n
			- Longitude_Deg: int: No parameter help available
			- Longitude_Min: int: No parameter help available
			- Longitude_Sec: int: No parameter help available
			- Longitude_Dir: str: No parameter help available
			- Latitude_Deg: int: No parameter help available
			- Latitude_Min: int: No parameter help available
			- Latitude_Sec: int: No parameter help available
			- Latitude_Dir: str: No parameter help available
			- Altitude: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Longitude_Deg'),
			ArgStruct.scalar_int('Longitude_Min'),
			ArgStruct.scalar_int('Longitude_Sec'),
			ArgStruct.scalar_str('Longitude_Dir'),
			ArgStruct.scalar_int('Latitude_Deg'),
			ArgStruct.scalar_int('Latitude_Min'),
			ArgStruct.scalar_int('Latitude_Sec'),
			ArgStruct.scalar_str('Latitude_Dir'),
			ArgStruct.scalar_float('Altitude')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Longitude_Deg: int = None
			self.Longitude_Min: int = None
			self.Longitude_Sec: int = None
			self.Longitude_Dir: str = None
			self.Latitude_Deg: int = None
			self.Latitude_Min: int = None
			self.Latitude_Sec: int = None
			self.Latitude_Dir: str = None
			self.Altitude: float = None

	def get_dms(self) -> DmsStruct:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:USER:RX:TRAJectory:FAPoint:COORdinates:DMS \n
		Snippet: value: DmsStruct = driver.source.fsimulator.dsSimulation.user.rx.trajectory.fapoint.coordinates.get_dms() \n
		No command help available \n
			:return: structure: for return value, see the help for DmsStruct structure arguments.
		"""
		return self._core.io.query_struct('SOURce<HwInstance>:FSIMulator:DSSimulation:USER:RX:TRAJectory:FAPoint:COORdinates:DMS?', self.__class__.DmsStruct())

	def set_dms(self, value: DmsStruct) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:USER:RX:TRAJectory:FAPoint:COORdinates:DMS \n
		Snippet with structure: \n
		structure = driver.source.fsimulator.dsSimulation.user.rx.trajectory.fapoint.coordinates.DmsStruct() \n
		structure.Longitude_Deg: int = 1 \n
		structure.Longitude_Min: int = 1 \n
		structure.Longitude_Sec: int = 1 \n
		structure.Longitude_Dir: str = '1' \n
		structure.Latitude_Deg: int = 1 \n
		structure.Latitude_Min: int = 1 \n
		structure.Latitude_Sec: int = 1 \n
		structure.Latitude_Dir: str = '1' \n
		structure.Altitude: float = 1.0 \n
		driver.source.fsimulator.dsSimulation.user.rx.trajectory.fapoint.coordinates.set_dms(value = structure) \n
		No command help available \n
			:param value: see the help for DmsStruct structure arguments.
		"""
		self._core.io.write_struct('SOURce<HwInstance>:FSIMulator:DSSimulation:USER:RX:TRAJectory:FAPoint:COORdinates:DMS', value)

	def clone(self) -> 'Coordinates':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Coordinates(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
