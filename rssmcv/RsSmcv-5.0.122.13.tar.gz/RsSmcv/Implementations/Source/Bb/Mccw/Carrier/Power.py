from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	def set(self, carrier_index: int, power: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:MCCW:CARRier:POWer \n
		Snippet: driver.source.bb.mccw.carrier.power.set(carrier_index = 1, power = 1.0) \n
		No command help available \n
			:param carrier_index: No help available
			:param power: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('carrier_index', carrier_index, DataType.Integer), ArgSingle('power', power, DataType.Float))
		self._core.io.write(f'SOURce<HwInstance>:BB:MCCW:CARRier:POWer {param}'.rstrip())

	# noinspection PyTypeChecker
	class PowerStruct(StructBase):
		"""Response structure. Fields: \n
			- Carrier_Index: int: No parameter help available
			- Power: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Carrier_Index'),
			ArgStruct.scalar_float('Power')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Carrier_Index: int = None
			self.Power: float = None

	def get(self) -> PowerStruct:
		"""SCPI: [SOURce<HW>]:BB:MCCW:CARRier:POWer \n
		Snippet: value: PowerStruct = driver.source.bb.mccw.carrier.power.get() \n
		No command help available \n
			:return: structure: for return value, see the help for PowerStruct structure arguments."""
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:MCCW:CARRier:POWer?', self.__class__.PowerStruct())
