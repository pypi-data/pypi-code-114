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
class UsPattern:
	"""UsPattern commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("usPattern", core, parent)

	def set(self, use_subfr_pat: List[str], bitcount: int, userIx=repcap.UserIx.Default, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:USER<CH>:AS:DL:[CELL<CCIDX>]:USPattern \n
		Snippet: driver.source.bb.oneweb.downlink.user.asPy.downlink.cell.usPattern.set(use_subfr_pat = ['raw1', 'raw2', 'raw3'], bitcount = 1, userIx = repcap.UserIx.Default, cellNull = repcap.CellNull.Default) \n
		No command help available \n
			:param use_subfr_pat: No help available
			:param bitcount: No help available
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('use_subfr_pat', use_subfr_pat, DataType.RawStringList, None), ArgSingle('bitcount', bitcount, DataType.Integer))
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:USER{userIx_cmd_val}:AS:DL:CELL{cellNull_cmd_val}:USPattern {param}'.rstrip())

	# noinspection PyTypeChecker
	class UsPatternStruct(StructBase):
		"""Response structure. Fields: \n
			- Use_Subfr_Pat: List[str]: No parameter help available
			- Bitcount: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct('Use_Subfr_Pat', DataType.RawStringList, None, False, True, 1),
			ArgStruct.scalar_int('Bitcount')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Use_Subfr_Pat: List[str] = None
			self.Bitcount: int = None

	def get(self, userIx=repcap.UserIx.Default, cellNull=repcap.CellNull.Default) -> UsPatternStruct:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:USER<CH>:AS:DL:[CELL<CCIDX>]:USPattern \n
		Snippet: value: UsPatternStruct = driver.source.bb.oneweb.downlink.user.asPy.downlink.cell.usPattern.get(userIx = repcap.UserIx.Default, cellNull = repcap.CellNull.Default) \n
		No command help available \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: structure: for return value, see the help for UsPatternStruct structure arguments."""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:ONEWeb:DL:USER{userIx_cmd_val}:AS:DL:CELL{cellNull_cmd_val}:USPattern?', self.__class__.UsPatternStruct())
