from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Port:
	"""Port commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: PortNull, default value after init: PortNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("port", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_portNull_get', 'repcap_portNull_set', repcap.PortNull.Nr0)

	def repcap_portNull_set(self, portNull: repcap.PortNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to PortNull.Default
		Default value after init: PortNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(portNull)

	def repcap_portNull_get(self) -> repcap.PortNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, pattern: List[str], bitcount: int, portNull=repcap.PortNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:CQIPattern:PORT<CH0> \n
		Snippet: driver.source.bb.eutra.tcw.ws.cqiPattern.port.set(pattern = ['raw1', 'raw2', 'raw3'], bitcount = 1, portNull = repcap.PortNull.Default) \n
		In performance test cases, sets the CQI Pattern. \n
			:param pattern: numeric
			:param bitcount: integer Range: 4 to 4
			:param portNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Port')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('pattern', pattern, DataType.RawStringList, None), ArgSingle('bitcount', bitcount, DataType.Integer))
		portNull_cmd_val = self._cmd_group.get_repcap_cmd_value(portNull, repcap.PortNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TCW:WS:CQIPattern:PORT{portNull_cmd_val} {param}'.rstrip())

	# noinspection PyTypeChecker
	class PortStruct(StructBase):
		"""Response structure. Fields: \n
			- Pattern: List[str]: numeric
			- Bitcount: int: integer Range: 4 to 4"""
		__meta_args_list = [
			ArgStruct('Pattern', DataType.RawStringList, None, False, True, 1),
			ArgStruct.scalar_int('Bitcount')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Pattern: List[str] = None
			self.Bitcount: int = None

	def get(self, portNull=repcap.PortNull.Default) -> PortStruct:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:CQIPattern:PORT<CH0> \n
		Snippet: value: PortStruct = driver.source.bb.eutra.tcw.ws.cqiPattern.port.get(portNull = repcap.PortNull.Default) \n
		In performance test cases, sets the CQI Pattern. \n
			:param portNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Port')
			:return: structure: for return value, see the help for PortStruct structure arguments."""
		portNull_cmd_val = self._cmd_group.get_repcap_cmd_value(portNull, repcap.PortNull)
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:EUTRa:TCW:WS:CQIPattern:PORT{portNull_cmd_val}?', self.__class__.PortStruct())

	def clone(self) -> 'Port':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Port(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
