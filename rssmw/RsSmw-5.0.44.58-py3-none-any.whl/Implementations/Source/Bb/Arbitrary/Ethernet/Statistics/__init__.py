from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Statistics:
	"""Statistics commands group definition. 7 total commands, 6 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("statistics", core, parent)

	@property
	def errors(self):
		"""errors commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_errors'):
			from .Errors import Errors
			self._errors = Errors(self._core, self._cmd_group)
		return self._errors

	@property
	def rxcFrames(self):
		"""rxcFrames commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rxcFrames'):
			from .RxcFrames import RxcFrames
			self._rxcFrames = RxcFrames(self._core, self._cmd_group)
		return self._rxcFrames

	@property
	def rxdBytes(self):
		"""rxdBytes commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rxdBytes'):
			from .RxdBytes import RxdBytes
			self._rxdBytes = RxdBytes(self._core, self._cmd_group)
		return self._rxdBytes

	@property
	def rxdFrames(self):
		"""rxdFrames commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rxdFrames'):
			from .RxdFrames import RxdFrames
			self._rxdFrames = RxdFrames(self._core, self._cmd_group)
		return self._rxdFrames

	@property
	def rxuSegments(self):
		"""rxuSegments commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rxuSegments'):
			from .RxuSegments import RxuSegments
			self._rxuSegments = RxuSegments(self._core, self._cmd_group)
		return self._rxuSegments

	@property
	def txrFrames(self):
		"""txrFrames commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_txrFrames'):
			from .TxrFrames import TxrFrames
			self._txrFrames = TxrFrames(self._core, self._cmd_group)
		return self._txrFrames

	# noinspection PyTypeChecker
	class AllStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Rx_Upload_Segment: int: No parameter help available
			- Rx_Control_Frames: int: No parameter help available
			- Rx_Data_Frames: int: No parameter help available
			- Rx_Data_Bytes: int: No parameter help available
			- Tx_Reply_Frames: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Rx_Upload_Segment'),
			ArgStruct.scalar_int('Rx_Control_Frames'),
			ArgStruct.scalar_int('Rx_Data_Frames'),
			ArgStruct.scalar_int('Rx_Data_Bytes'),
			ArgStruct.scalar_int('Tx_Reply_Frames')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rx_Upload_Segment: int = None
			self.Rx_Control_Frames: int = None
			self.Rx_Data_Frames: int = None
			self.Rx_Data_Bytes: int = None
			self.Tx_Reply_Frames: int = None

	def get_all(self) -> AllStruct:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:ETHernet:STATistics:ALL \n
		Snippet: value: AllStruct = driver.source.bb.arbitrary.ethernet.statistics.get_all() \n
		No command help available \n
			:return: structure: for return value, see the help for AllStruct structure arguments.
		"""
		return self._core.io.query_struct('SOURce<HwInstance>:BB:ARBitrary:ETHernet:STATistics:ALL?', self.__class__.AllStruct())

	def clone(self) -> 'Statistics':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Statistics(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
