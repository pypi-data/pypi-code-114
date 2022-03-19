from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, carrier_index: int, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:MCCW:CARRier:STATe \n
		Snippet: driver.source.bb.mccw.carrier.state.set(carrier_index = 1, state = False) \n
		No command help available \n
			:param carrier_index: No help available
			:param state: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('carrier_index', carrier_index, DataType.Integer), ArgSingle('state', state, DataType.Boolean))
		self._core.io.write(f'SOURce<HwInstance>:BB:MCCW:CARRier:STATe {param}'.rstrip())

	# noinspection PyTypeChecker
	class StateStruct(StructBase):
		"""Response structure. Fields: \n
			- Carrier_Index: int: No parameter help available
			- State: bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Carrier_Index'),
			ArgStruct.scalar_bool('State')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Carrier_Index: int = None
			self.State: bool = None

	def get(self) -> StateStruct:
		"""SCPI: [SOURce<HW>]:BB:MCCW:CARRier:STATe \n
		Snippet: value: StateStruct = driver.source.bb.mccw.carrier.state.get() \n
		No command help available \n
			:return: structure: for return value, see the help for StateStruct structure arguments."""
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:MCCW:CARRier:STATe?', self.__class__.StateStruct())
