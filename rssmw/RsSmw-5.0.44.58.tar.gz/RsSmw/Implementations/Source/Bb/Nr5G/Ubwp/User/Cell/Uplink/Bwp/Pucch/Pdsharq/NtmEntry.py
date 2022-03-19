from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NtmEntry:
	"""NtmEntry commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ntmEntry", core, parent)

	def set(self, num_ul_bp_pucch_ack: float, userNull=repcap.UserNull.Default, cellNull=repcap.CellNull.Default, bwPartNull=repcap.BwPartNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:CELL<ST0>:UL:BWP<DIR0>:PUCCh:PDSHarq:NTMentry \n
		Snippet: driver.source.bb.nr5G.ubwp.user.cell.uplink.bwp.pucch.pdsharq.ntmEntry.set(num_ul_bp_pucch_ack = 1.0, userNull = repcap.UserNull.Default, cellNull = repcap.CellNull.Default, bwPartNull = repcap.BwPartNull.Default) \n
		Sets the number of entries in the sequence of PDSCH to HARQ timing values. The value set here defines the available
		suffixes in the command [:SOURce<hw>]:BB:NR5G:UBWP:USER<ch0>:CELL<st0>:UL:BWP<dir0>:PUCCh:PDSHarq:TMIValue<gr0>. \n
			:param num_ul_bp_pucch_ack: float Range: 0 to 8
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param bwPartNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Bwp')
		"""
		param = Conversions.decimal_value_to_str(num_ul_bp_pucch_ack)
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		bwPartNull_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPartNull, repcap.BwPartNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:CELL{cellNull_cmd_val}:UL:BWP{bwPartNull_cmd_val}:PUCCh:PDSHarq:NTMentry {param}')

	def get(self, userNull=repcap.UserNull.Default, cellNull=repcap.CellNull.Default, bwPartNull=repcap.BwPartNull.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:CELL<ST0>:UL:BWP<DIR0>:PUCCh:PDSHarq:NTMentry \n
		Snippet: value: float = driver.source.bb.nr5G.ubwp.user.cell.uplink.bwp.pucch.pdsharq.ntmEntry.get(userNull = repcap.UserNull.Default, cellNull = repcap.CellNull.Default, bwPartNull = repcap.BwPartNull.Default) \n
		Sets the number of entries in the sequence of PDSCH to HARQ timing values. The value set here defines the available
		suffixes in the command [:SOURce<hw>]:BB:NR5G:UBWP:USER<ch0>:CELL<st0>:UL:BWP<dir0>:PUCCh:PDSHarq:TMIValue<gr0>. \n
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param bwPartNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Bwp')
			:return: num_ul_bp_pucch_ack: float Range: 0 to 8"""
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		bwPartNull_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPartNull, repcap.BwPartNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:CELL{cellNull_cmd_val}:UL:BWP{bwPartNull_cmd_val}:PUCCh:PDSHarq:NTMentry?')
		return Conversions.str_to_float(response)
