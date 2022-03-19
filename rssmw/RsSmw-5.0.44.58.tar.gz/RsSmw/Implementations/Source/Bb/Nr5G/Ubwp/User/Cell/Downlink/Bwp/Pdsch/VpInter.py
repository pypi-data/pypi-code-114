from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import enums
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class VpInter:
	"""VpInter commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("vpInter", core, parent)

	def set(self, vrb_to_prb_interle: enums.VrbToPrbInterleaverAll, userNull=repcap.UserNull.Default, cellNull=repcap.CellNull.Default, bwPartNull=repcap.BwPartNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:CELL<ST0>:DL:BWP<DIR0>:PDSCh:VPINter \n
		Snippet: driver.source.bb.nr5G.ubwp.user.cell.downlink.bwp.pdsch.vpInter.set(vrb_to_prb_interle = enums.VrbToPrbInterleaverAll.VP2, userNull = repcap.UserNull.Default, cellNull = repcap.CellNull.Default, bwPartNull = repcap.BwPartNull.Default) \n
		Queries the mapping method used for the mapping of the virtual resource blocks (VRB) to the physical resource blocks
		(PRB) . \n
			:param vrb_to_prb_interle: VPN| VP2| VP4 VPN Non-interleaved VP2|VP4 Interleaving is enabled. The value defines the interleaving unit size: VP2 = 2 and VP4 = 4.
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param bwPartNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Bwp')
		"""
		param = Conversions.enum_scalar_to_str(vrb_to_prb_interle, enums.VrbToPrbInterleaverAll)
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		bwPartNull_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPartNull, repcap.BwPartNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:CELL{cellNull_cmd_val}:DL:BWP{bwPartNull_cmd_val}:PDSCh:VPINter {param}')

	# noinspection PyTypeChecker
	def get(self, userNull=repcap.UserNull.Default, cellNull=repcap.CellNull.Default, bwPartNull=repcap.BwPartNull.Default) -> enums.VrbToPrbInterleaverAll:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:CELL<ST0>:DL:BWP<DIR0>:PDSCh:VPINter \n
		Snippet: value: enums.VrbToPrbInterleaverAll = driver.source.bb.nr5G.ubwp.user.cell.downlink.bwp.pdsch.vpInter.get(userNull = repcap.UserNull.Default, cellNull = repcap.CellNull.Default, bwPartNull = repcap.BwPartNull.Default) \n
		Queries the mapping method used for the mapping of the virtual resource blocks (VRB) to the physical resource blocks
		(PRB) . \n
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param bwPartNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Bwp')
			:return: vrb_to_prb_interle: VPN| VP2| VP4 VPN Non-interleaved VP2|VP4 Interleaving is enabled. The value defines the interleaving unit size: VP2 = 2 and VP4 = 4."""
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		bwPartNull_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPartNull, repcap.BwPartNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:CELL{cellNull_cmd_val}:DL:BWP{bwPartNull_cmd_val}:PDSCh:VPINter?')
		return Conversions.str_to_scalar_enum(response, enums.VrbToPrbInterleaverAll)
