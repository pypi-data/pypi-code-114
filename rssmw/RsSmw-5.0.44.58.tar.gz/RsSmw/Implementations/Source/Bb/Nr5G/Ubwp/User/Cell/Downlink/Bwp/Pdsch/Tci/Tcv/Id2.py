from .............Internal.Core import Core
from .............Internal.CommandsGroup import CommandsGroup
from .............Internal import Conversions
from ............. import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Id2:
	"""Id2 commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("id2", core, parent)

	def set(self, tci_id_2: int, userNull=repcap.UserNull.Default, cellNull=repcap.CellNull.Default, bwPartNull=repcap.BwPartNull.Default, tciCodepoint=repcap.TciCodepoint.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:CELL<ST0>:DL:BWP<DIR0>:PDSCh:TCI:TCV<GR0>:ID2 \n
		Snippet: driver.source.bb.nr5G.ubwp.user.cell.downlink.bwp.pdsch.tci.tcv.id2.set(tci_id_2 = 1, userNull = repcap.UserNull.Default, cellNull = repcap.CellNull.Default, bwPartNull = repcap.BwPartNull.Default, tciCodepoint = repcap.TciCodepoint.Default) \n
		Defines the value of the state ID 1 for a TCI codepoint.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on usage of state ID 2 ([:SOURce<hw>]:BB:NR5G:UBWP:USER<ch0>:CELL<st0>:DL:BWP<dir0>:PDSCh:TCI:TCV<gr0>:STATe) . \n
			:param tci_id_2: No help available
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param bwPartNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Bwp')
			:param tciCodepoint: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Tcv')
		"""
		param = Conversions.decimal_value_to_str(tci_id_2)
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		bwPartNull_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPartNull, repcap.BwPartNull)
		tciCodepoint_cmd_val = self._cmd_group.get_repcap_cmd_value(tciCodepoint, repcap.TciCodepoint)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:CELL{cellNull_cmd_val}:DL:BWP{bwPartNull_cmd_val}:PDSCh:TCI:TCV{tciCodepoint_cmd_val}:ID2 {param}')

	def get(self, userNull=repcap.UserNull.Default, cellNull=repcap.CellNull.Default, bwPartNull=repcap.BwPartNull.Default, tciCodepoint=repcap.TciCodepoint.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:CELL<ST0>:DL:BWP<DIR0>:PDSCh:TCI:TCV<GR0>:ID2 \n
		Snippet: value: int = driver.source.bb.nr5G.ubwp.user.cell.downlink.bwp.pdsch.tci.tcv.id2.get(userNull = repcap.UserNull.Default, cellNull = repcap.CellNull.Default, bwPartNull = repcap.BwPartNull.Default, tciCodepoint = repcap.TciCodepoint.Default) \n
		Defines the value of the state ID 1 for a TCI codepoint.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on usage of state ID 2 ([:SOURce<hw>]:BB:NR5G:UBWP:USER<ch0>:CELL<st0>:DL:BWP<dir0>:PDSCh:TCI:TCV<gr0>:STATe) . \n
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param bwPartNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Bwp')
			:param tciCodepoint: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Tcv')
			:return: tci_id_2: No help available"""
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		bwPartNull_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPartNull, repcap.BwPartNull)
		tciCodepoint_cmd_val = self._cmd_group.get_repcap_cmd_value(tciCodepoint, repcap.TciCodepoint)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:CELL{cellNull_cmd_val}:DL:BWP{bwPartNull_cmd_val}:PDSCh:TCI:TCV{tciCodepoint_cmd_val}:ID2?')
		return Conversions.str_to_int(response)
