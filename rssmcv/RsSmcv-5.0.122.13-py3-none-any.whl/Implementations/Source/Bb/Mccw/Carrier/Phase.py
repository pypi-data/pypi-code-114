from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Phase:
	"""Phase commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phase", core, parent)

	def set(self, carrier_index: int, phase: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:MCCW:CARRier:PHASe \n
		Snippet: driver.source.bb.mccw.carrier.phase.set(carrier_index = 1, phase = 1.0) \n
		No command help available \n
			:param carrier_index: No help available
			:param phase: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('carrier_index', carrier_index, DataType.Integer), ArgSingle('phase', phase, DataType.Float))
		self._core.io.write(f'SOURce<HwInstance>:BB:MCCW:CARRier:PHASe {param}'.rstrip())

	# noinspection PyTypeChecker
	class PhaseStruct(StructBase):
		"""Response structure. Fields: \n
			- Carrier_Index: int: No parameter help available
			- Phase: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Carrier_Index'),
			ArgStruct.scalar_float('Phase')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Carrier_Index: int = None
			self.Phase: float = None

	def get(self) -> PhaseStruct:
		"""SCPI: [SOURce<HW>]:BB:MCCW:CARRier:PHASe \n
		Snippet: value: PhaseStruct = driver.source.bb.mccw.carrier.phase.get() \n
		No command help available \n
			:return: structure: for return value, see the help for PhaseStruct structure arguments."""
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:MCCW:CARRier:PHASe?', self.__class__.PhaseStruct())
