from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal.Types import DataType
from ..........Internal.StructBase import StructBase
from ..........Internal.ArgStruct import ArgStruct
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Xyz:
	"""Xyz commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("xyz", core, parent)

	def set(self, xcoor: float, ycoor: float, altitude: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:USER:TX:TRAJectory:FAPoint:COORdinates:XYZ \n
		Snippet: driver.source.fsimulator.dsSimulation.user.tx.trajectory.fapoint.coordinates.xyz.set(xcoor = 1.0, ycoor = 1.0, altitude = 1.0) \n
		No command help available \n
			:param xcoor: No help available
			:param ycoor: No help available
			:param altitude: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('xcoor', xcoor, DataType.Float), ArgSingle('ycoor', ycoor, DataType.Float), ArgSingle('altitude', altitude, DataType.Float))
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:USER:TX:TRAJectory:FAPoint:COORdinates:XYZ {param}'.rstrip())

	# noinspection PyTypeChecker
	class XyzStruct(StructBase):
		"""Response structure. Fields: \n
			- Xcoor: float: No parameter help available
			- Ycoor: float: No parameter help available
			- Altitude: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Xcoor'),
			ArgStruct.scalar_float('Ycoor'),
			ArgStruct.scalar_float('Altitude')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Xcoor: float = None
			self.Ycoor: float = None
			self.Altitude: float = None

	def get(self) -> XyzStruct:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:USER:TX:TRAJectory:FAPoint:COORdinates:XYZ \n
		Snippet: value: XyzStruct = driver.source.fsimulator.dsSimulation.user.tx.trajectory.fapoint.coordinates.xyz.get() \n
		No command help available \n
			:return: structure: for return value, see the help for XyzStruct structure arguments."""
		return self._core.io.query_struct(f'SOURce<HwInstance>:FSIMulator:DSSimulation:USER:TX:TRAJectory:FAPoint:COORdinates:XYZ?', self.__class__.XyzStruct())
