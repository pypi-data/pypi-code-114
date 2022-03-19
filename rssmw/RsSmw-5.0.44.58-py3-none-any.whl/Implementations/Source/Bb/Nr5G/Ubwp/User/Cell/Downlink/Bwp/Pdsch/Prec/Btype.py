from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions
from ............ import enums
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Btype:
	"""Btype commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("btype", core, parent)

	def set(self, dl_bwp_prb_bundl_in: enums.PrbBundlingType, userNull=repcap.UserNull.Default, cellNull=repcap.CellNull.Default, bwPartNull=repcap.BwPartNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:CELL<ST0>:DL:BWP<DIR0>:PDSCh:PREC:BTYPe \n
		Snippet: driver.source.bb.nr5G.ubwp.user.cell.downlink.bwp.pdsch.prec.btype.set(dl_bwp_prb_bundl_in = enums.PrbBundlingType.DYNamic, userNull = repcap.UserNull.Default, cellNull = repcap.CellNull.Default, bwPartNull = repcap.BwPartNull.Default) \n
		Indicates the PRB bundle type and bundle sizes. If 'dynamic' is chosen, the actual bundle size set to use is indicated
		via DCI. Only available if 'Precoding' is enabled. The PRB bundling type supports the UE to reduce the computational
		effort to receive the information which PRBs use the same precoding. The UE only has to do channel estimation per PRB
		bundle not per PRB. Without this information, the UE has to decode all the information itself based on the DMRS. \n
			:param dl_bwp_prb_bundl_in: NOTC| STATic| DYNamic NOTC Default value, PRB bundling is not configured. STATic PRB bundling is set to static and can be adjusted by the 'Static Bundle Size'. DYNamic PRB bundling is set to dynamic and can be adjusted by the 'Bundle Size Set 1' and 'Bundle Size Set 2'.
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param bwPartNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Bwp')
		"""
		param = Conversions.enum_scalar_to_str(dl_bwp_prb_bundl_in, enums.PrbBundlingType)
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		bwPartNull_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPartNull, repcap.BwPartNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:CELL{cellNull_cmd_val}:DL:BWP{bwPartNull_cmd_val}:PDSCh:PREC:BTYPe {param}')

	# noinspection PyTypeChecker
	def get(self, userNull=repcap.UserNull.Default, cellNull=repcap.CellNull.Default, bwPartNull=repcap.BwPartNull.Default) -> enums.PrbBundlingType:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:CELL<ST0>:DL:BWP<DIR0>:PDSCh:PREC:BTYPe \n
		Snippet: value: enums.PrbBundlingType = driver.source.bb.nr5G.ubwp.user.cell.downlink.bwp.pdsch.prec.btype.get(userNull = repcap.UserNull.Default, cellNull = repcap.CellNull.Default, bwPartNull = repcap.BwPartNull.Default) \n
		Indicates the PRB bundle type and bundle sizes. If 'dynamic' is chosen, the actual bundle size set to use is indicated
		via DCI. Only available if 'Precoding' is enabled. The PRB bundling type supports the UE to reduce the computational
		effort to receive the information which PRBs use the same precoding. The UE only has to do channel estimation per PRB
		bundle not per PRB. Without this information, the UE has to decode all the information itself based on the DMRS. \n
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param bwPartNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Bwp')
			:return: dl_bwp_prb_bundl_in: NOTC| STATic| DYNamic NOTC Default value, PRB bundling is not configured. STATic PRB bundling is set to static and can be adjusted by the 'Static Bundle Size'. DYNamic PRB bundling is set to dynamic and can be adjusted by the 'Bundle Size Set 1' and 'Bundle Size Set 2'."""
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		bwPartNull_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPartNull, repcap.BwPartNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:CELL{cellNull_cmd_val}:DL:BWP{bwPartNull_cmd_val}:PDSCh:PREC:BTYPe?')
		return Conversions.str_to_scalar_enum(response, enums.PrbBundlingType)
