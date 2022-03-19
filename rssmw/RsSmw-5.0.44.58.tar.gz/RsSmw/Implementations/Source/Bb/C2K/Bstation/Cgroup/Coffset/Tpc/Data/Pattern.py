from typing import List

from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal.Types import DataType
from ..........Internal.StructBase import StructBase
from ..........Internal.ArgStruct import ArgStruct
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pattern:
	"""Pattern commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pattern", core, parent)

	def set(self, pattern: List[str], bitcount: int, baseStation=repcap.BaseStation.Default, groupNull=repcap.GroupNull.Default, offset=repcap.Offset.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:CGRoup<DI0>:COFFset<CH>:TPC:DATA:PATTern \n
		Snippet: driver.source.bb.c2K.bstation.cgroup.coffset.tpc.data.pattern.set(pattern = ['raw1', 'raw2', 'raw3'], bitcount = 1, baseStation = repcap.BaseStation.Default, groupNull = repcap.GroupNull.Default, offset = repcap.Offset.Default) \n
		Sets the bit pattern for the PATTern selection. Power control is available for sub channel types F-DCCH and F-FCH. F-DCCH
		is only generated for radio configurations 3, 4 and 5. For the traffic channels, this value is specific for the selected
		radio configuration. \n
			:param pattern: numeric
			:param bitcount: integer Range: 1 to 64
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param groupNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cgroup')
			:param offset: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Coffset')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('pattern', pattern, DataType.RawStringList, None), ArgSingle('bitcount', bitcount, DataType.Integer))
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		groupNull_cmd_val = self._cmd_group.get_repcap_cmd_value(groupNull, repcap.GroupNull)
		offset_cmd_val = self._cmd_group.get_repcap_cmd_value(offset, repcap.Offset)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:CGRoup{groupNull_cmd_val}:COFFset{offset_cmd_val}:TPC:DATA:PATTern {param}'.rstrip())

	# noinspection PyTypeChecker
	class PatternStruct(StructBase):
		"""Response structure. Fields: \n
			- Pattern: List[str]: numeric
			- Bitcount: int: integer Range: 1 to 64"""
		__meta_args_list = [
			ArgStruct('Pattern', DataType.RawStringList, None, False, True, 1),
			ArgStruct.scalar_int('Bitcount')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Pattern: List[str] = None
			self.Bitcount: int = None

	def get(self, baseStation=repcap.BaseStation.Default, groupNull=repcap.GroupNull.Default, offset=repcap.Offset.Default) -> PatternStruct:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:CGRoup<DI0>:COFFset<CH>:TPC:DATA:PATTern \n
		Snippet: value: PatternStruct = driver.source.bb.c2K.bstation.cgroup.coffset.tpc.data.pattern.get(baseStation = repcap.BaseStation.Default, groupNull = repcap.GroupNull.Default, offset = repcap.Offset.Default) \n
		Sets the bit pattern for the PATTern selection. Power control is available for sub channel types F-DCCH and F-FCH. F-DCCH
		is only generated for radio configurations 3, 4 and 5. For the traffic channels, this value is specific for the selected
		radio configuration. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param groupNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cgroup')
			:param offset: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Coffset')
			:return: structure: for return value, see the help for PatternStruct structure arguments."""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		groupNull_cmd_val = self._cmd_group.get_repcap_cmd_value(groupNull, repcap.GroupNull)
		offset_cmd_val = self._cmd_group.get_repcap_cmd_value(offset, repcap.Offset)
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:CGRoup{groupNull_cmd_val}:COFFset{offset_cmd_val}:TPC:DATA:PATTern?', self.__class__.PatternStruct())
