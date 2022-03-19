from typing import List

from ..............Internal.Core import Core
from ..............Internal.CommandsGroup import CommandsGroup
from ..............Internal.Types import DataType
from ..............Internal.StructBase import StructBase
from ..............Internal.ArgStruct import ArgStruct
from ..............Internal.ArgSingleList import ArgSingleList
from ..............Internal.ArgSingle import ArgSingle
from .............. import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pattern:
	"""Pattern commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pattern", core, parent)

	def set(self, cgu_ci_pattern: List[str], cgu_ci_bit_count: int, cellNull=repcap.CellNull.Default, subframeNull=repcap.SubframeNull.Default, userNull=repcap.UserNull.Default, bwPartNull=repcap.BwPartNull.Default, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:SCHed:CELL<CH0>:SUBF<ST0>:USER<DIR0>:BWPart<GR0>:ALLoc<USER0>:PUSCh:UCI:CGUCi:PATTern \n
		Snippet: driver.source.bb.nr5G.scheduling.cell.subf.user.bwPart.alloc.pusch.uci.cguci.pattern.set(cgu_ci_pattern = ['raw1', 'raw2', 'raw3'], cgu_ci_bit_count = 1, cellNull = repcap.CellNull.Default, subframeNull = repcap.SubframeNull.Default, userNull = repcap.UserNull.Default, bwPartNull = repcap.BwPartNull.Default, allocationNull = repcap.AllocationNull.Default) \n
		Sets the ACK/CSI 1/CSI 2 bits in pattern form. \n
			:param cgu_ci_pattern: 1024 bits Bit pattern
			:param cgu_ci_bit_count: integer Pattern length, should be the same as the length set with the command [:SOURcehw]:BB:NR5G:SCHed:CELLch0:SUBFst0:USERdir0:BWPartgr0:ALLocuser0:PUSCh:UCI:CGUCi:BITS. Range: 0 to 1024
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:param bwPartNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'BwPart')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('cgu_ci_pattern', cgu_ci_pattern, DataType.RawStringList, None), ArgSingle('cgu_ci_bit_count', cgu_ci_bit_count, DataType.Integer))
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		bwPartNull_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPartNull, repcap.BwPartNull)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:SCHed:CELL{cellNull_cmd_val}:SUBF{subframeNull_cmd_val}:USER{userNull_cmd_val}:BWPart{bwPartNull_cmd_val}:ALLoc{allocationNull_cmd_val}:PUSCh:UCI:CGUCi:PATTern {param}'.rstrip())

	# noinspection PyTypeChecker
	class PatternStruct(StructBase):
		"""Response structure. Fields: \n
			- Cgu_Ci_Pattern: List[str]: 1024 bits Bit pattern
			- Cgu_Ci_Bit_Count: int: integer Pattern length, should be the same as the length set with the command [:SOURcehw]:BB:NR5G:SCHed:CELLch0:SUBFst0:USERdir0:BWPartgr0:ALLocuser0:PUSCh:UCI:CGUCi:BITS. Range: 0 to 1024"""
		__meta_args_list = [
			ArgStruct('Cgu_Ci_Pattern', DataType.RawStringList, None, False, True, 1),
			ArgStruct.scalar_int('Cgu_Ci_Bit_Count')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cgu_Ci_Pattern: List[str] = None
			self.Cgu_Ci_Bit_Count: int = None

	def get(self, cellNull=repcap.CellNull.Default, subframeNull=repcap.SubframeNull.Default, userNull=repcap.UserNull.Default, bwPartNull=repcap.BwPartNull.Default, allocationNull=repcap.AllocationNull.Default) -> PatternStruct:
		"""SCPI: [SOURce<HW>]:BB:NR5G:SCHed:CELL<CH0>:SUBF<ST0>:USER<DIR0>:BWPart<GR0>:ALLoc<USER0>:PUSCh:UCI:CGUCi:PATTern \n
		Snippet: value: PatternStruct = driver.source.bb.nr5G.scheduling.cell.subf.user.bwPart.alloc.pusch.uci.cguci.pattern.get(cellNull = repcap.CellNull.Default, subframeNull = repcap.SubframeNull.Default, userNull = repcap.UserNull.Default, bwPartNull = repcap.BwPartNull.Default, allocationNull = repcap.AllocationNull.Default) \n
		Sets the ACK/CSI 1/CSI 2 bits in pattern form. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:param bwPartNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'BwPart')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: structure: for return value, see the help for PatternStruct structure arguments."""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		bwPartNull_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPartNull, repcap.BwPartNull)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:NR5G:SCHed:CELL{cellNull_cmd_val}:SUBF{subframeNull_cmd_val}:USER{userNull_cmd_val}:BWPart{bwPartNull_cmd_val}:ALLoc{allocationNull_cmd_val}:PUSCh:UCI:CGUCi:PATTern?', self.__class__.PatternStruct())
