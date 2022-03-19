from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Decimal:
	"""Decimal commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("decimal", core, parent)

	def set(self, longitude: float, latitude: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:SHIPtoship:RX:COORdinates:[DECimal] \n
		Snippet: driver.source.fsimulator.dsSimulation.shiptoship.rx.coordinates.decimal.set(longitude = 1.0, latitude = 1.0) \n
		No command help available \n
			:param longitude: No help available
			:param latitude: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('longitude', longitude, DataType.Float), ArgSingle('latitude', latitude, DataType.Float))
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:SHIPtoship:RX:COORdinates:DECimal {param}'.rstrip())

	# noinspection PyTypeChecker
	class DecimalStruct(StructBase):
		"""Response structure. Fields: \n
			- Longitude: float: No parameter help available
			- Latitude: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Longitude'),
			ArgStruct.scalar_float('Latitude')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Longitude: float = None
			self.Latitude: float = None

	def get(self) -> DecimalStruct:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:SHIPtoship:RX:COORdinates:[DECimal] \n
		Snippet: value: DecimalStruct = driver.source.fsimulator.dsSimulation.shiptoship.rx.coordinates.decimal.get() \n
		No command help available \n
			:return: structure: for return value, see the help for DecimalStruct structure arguments."""
		return self._core.io.query_struct(f'SOURce<HwInstance>:FSIMulator:DSSimulation:SHIPtoship:RX:COORdinates:DECimal?', self.__class__.DecimalStruct())
