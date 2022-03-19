from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal.Types import DataType
from ..........Internal.StructBase import StructBase
from ..........Internal.ArgStruct import ArgStruct
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Decimal:
	"""Decimal commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("decimal", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Longitude: float: float Range: -180 to 180
			- Latitude: float: float Range: -90 to 90
			- Altitude: float: float Range: -10E3 to 50E6"""
		__meta_args_list = [
			ArgStruct.scalar_float('Longitude'),
			ArgStruct.scalar_float('Latitude'),
			ArgStruct.scalar_float('Altitude')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Longitude: float = None
			self.Latitude: float = None
			self.Altitude: float = None

	def get(self, time_basis: enums.TimeBasis, ycoorear: int, month: int, day: int, hour: int, minutes: int, seconds: float, week_number: int, time_of_week: float, vehicle=repcap.Vehicle.Default) -> GetStruct:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RT:RECeiver:[V<ST>]:RLOCation:COORdinates:DECimal \n
		Snippet: value: GetStruct = driver.source.bb.gnss.rt.receiver.v.rlocation.coordinates.decimal.get(time_basis = enums.TimeBasis.BDT, ycoorear = 1, month = 1, day = 1, hour = 1, minutes = 1, seconds = 1.0, week_number = 1, time_of_week = 1.0, vehicle = repcap.Vehicle.Default) \n
		Queries the coordinates of the receiver location in decimal format for the selected moment of time. The required query
		parameters depend on the selected timebase. \n
			:param time_basis: select
			:param ycoorear: No help available
			:param month: integer Range: 1 to 12
			:param day: integer Range: 1 to 31
			:param hour: integer Range: 0 to 23
			:param minutes: integer Range: 0 to 59
			:param seconds: float Range: 0 to 59.999
			:param week_number: integer Range: 0 to 529947
			:param time_of_week: float Range: 0 to 604799.999
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('time_basis', time_basis, DataType.Enum, enums.TimeBasis), ArgSingle('ycoorear', ycoorear, DataType.Integer), ArgSingle('month', month, DataType.Integer), ArgSingle('day', day, DataType.Integer), ArgSingle('hour', hour, DataType.Integer), ArgSingle('minutes', minutes, DataType.Integer), ArgSingle('seconds', seconds, DataType.Float), ArgSingle('week_number', week_number, DataType.Integer), ArgSingle('time_of_week', time_of_week, DataType.Float))
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:GNSS:RT:RECeiver:V{vehicle_cmd_val}:RLOCation:COORdinates:DECimal? {param}'.rstrip(), self.__class__.GetStruct())
