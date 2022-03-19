from typing import List

from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal.Types import DataType
from ............Internal.StructBase import StructBase
from ............Internal.ArgStruct import ArgStruct
from ............Internal.ArgSingleList import ArgSingleList
from ............Internal.ArgSingle import ArgSingle
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SltPatt:
	"""SltPatt commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sltPatt", core, parent)

	def set(self, rate_mat_slot_patt: List[str], bitcount: int, userNull=repcap.UserNull.Default, cellNull=repcap.CellNull.Default, bwPartNull=repcap.BwPartNull.Default, rateSettingNull=repcap.RateSettingNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:CELL<ST0>:DL:BWP<DIR0>:RATM:RS<GR0>:SLTPatt \n
		Snippet: driver.source.bb.nr5G.ubwp.user.cell.downlink.bwp.ratm.rs.sltPatt.set(rate_mat_slot_patt = ['raw1', 'raw2', 'raw3'], bitcount = 1, userNull = repcap.UserNull.Default, cellNull = repcap.CellNull.Default, bwPartNull = repcap.BwPartNull.Default, rateSettingNull = repcap.RateSettingNull.Default) \n
		Set the slots to be used as a pattern. \n
			:param rate_mat_slot_patt: 28 bits
			:param bitcount: integer Range: 14 to 28
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param bwPartNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Bwp')
			:param rateSettingNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Rs')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('rate_mat_slot_patt', rate_mat_slot_patt, DataType.RawStringList, None), ArgSingle('bitcount', bitcount, DataType.Integer))
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		bwPartNull_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPartNull, repcap.BwPartNull)
		rateSettingNull_cmd_val = self._cmd_group.get_repcap_cmd_value(rateSettingNull, repcap.RateSettingNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:CELL{cellNull_cmd_val}:DL:BWP{bwPartNull_cmd_val}:RATM:RS{rateSettingNull_cmd_val}:SLTPatt {param}'.rstrip())

	# noinspection PyTypeChecker
	class SltPattStruct(StructBase):
		"""Response structure. Fields: \n
			- Rate_Mat_Slot_Patt: List[str]: 28 bits
			- Bitcount: int: integer Range: 14 to 28"""
		__meta_args_list = [
			ArgStruct('Rate_Mat_Slot_Patt', DataType.RawStringList, None, False, True, 1),
			ArgStruct.scalar_int('Bitcount')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rate_Mat_Slot_Patt: List[str] = None
			self.Bitcount: int = None

	def get(self, userNull=repcap.UserNull.Default, cellNull=repcap.CellNull.Default, bwPartNull=repcap.BwPartNull.Default, rateSettingNull=repcap.RateSettingNull.Default) -> SltPattStruct:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:CELL<ST0>:DL:BWP<DIR0>:RATM:RS<GR0>:SLTPatt \n
		Snippet: value: SltPattStruct = driver.source.bb.nr5G.ubwp.user.cell.downlink.bwp.ratm.rs.sltPatt.get(userNull = repcap.UserNull.Default, cellNull = repcap.CellNull.Default, bwPartNull = repcap.BwPartNull.Default, rateSettingNull = repcap.RateSettingNull.Default) \n
		Set the slots to be used as a pattern. \n
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param bwPartNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Bwp')
			:param rateSettingNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Rs')
			:return: structure: for return value, see the help for SltPattStruct structure arguments."""
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		bwPartNull_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPartNull, repcap.BwPartNull)
		rateSettingNull_cmd_val = self._cmd_group.get_repcap_cmd_value(rateSettingNull, repcap.RateSettingNull)
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:CELL{cellNull_cmd_val}:DL:BWP{bwPartNull_cmd_val}:RATM:RS{rateSettingNull_cmd_val}:SLTPatt?', self.__class__.SltPattStruct())
