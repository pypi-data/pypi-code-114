from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Noffsets:
	"""Noffsets commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("noffsets", core, parent)

	def set(self, num_freq_hop_off: int, userNull=repcap.UserNull.Default, cellNull=repcap.CellNull.Default, bwPartNull=repcap.BwPartNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:CELL<ST0>:UL:BWP<DIR0>:PUSCh:FHOFfsets:NOFFsets \n
		Snippet: driver.source.bb.nr5G.ubwp.user.cell.uplink.bwp.pusch.fhOffsets.noffsets.set(num_freq_hop_off = 1, userNull = repcap.UserNull.Default, cellNull = repcap.CellNull.Default, bwPartNull = repcap.BwPartNull.Default) \n
		Defines the number off frequency hopping offsets.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- If the size of the active BWP is fewer than 50 PRBs, one of two higher layer configured offsets are indicated in the UL grant.
			- If the size of the active BWP is equal to or greater than 50 PRBs, one of four higher layer configured offsets are indicated in the UL grant. \n
			:param num_freq_hop_off: integer Range: 2 to 4
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param bwPartNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Bwp')
		"""
		param = Conversions.decimal_value_to_str(num_freq_hop_off)
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		bwPartNull_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPartNull, repcap.BwPartNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:CELL{cellNull_cmd_val}:UL:BWP{bwPartNull_cmd_val}:PUSCh:FHOFfsets:NOFFsets {param}')

	def get(self, userNull=repcap.UserNull.Default, cellNull=repcap.CellNull.Default, bwPartNull=repcap.BwPartNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:CELL<ST0>:UL:BWP<DIR0>:PUSCh:FHOFfsets:NOFFsets \n
		Snippet: value: int = driver.source.bb.nr5G.ubwp.user.cell.uplink.bwp.pusch.fhOffsets.noffsets.get(userNull = repcap.UserNull.Default, cellNull = repcap.CellNull.Default, bwPartNull = repcap.BwPartNull.Default) \n
		Defines the number off frequency hopping offsets.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- If the size of the active BWP is fewer than 50 PRBs, one of two higher layer configured offsets are indicated in the UL grant.
			- If the size of the active BWP is equal to or greater than 50 PRBs, one of four higher layer configured offsets are indicated in the UL grant. \n
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param bwPartNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Bwp')
			:return: num_freq_hop_off: integer Range: 2 to 4"""
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		bwPartNull_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPartNull, repcap.BwPartNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:CELL{cellNull_cmd_val}:UL:BWP{bwPartNull_cmd_val}:PUSCh:FHOFfsets:NOFFsets?')
		return Conversions.str_to_int(response)
