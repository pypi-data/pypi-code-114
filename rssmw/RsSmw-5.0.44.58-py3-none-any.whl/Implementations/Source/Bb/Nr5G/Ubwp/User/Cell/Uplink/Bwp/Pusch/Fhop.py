from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import enums
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fhop:
	"""Fhop commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fhop", core, parent)

	def set(self, sel_freq_hopp: enums.UlfReqHopping, userNull=repcap.UserNull.Default, cellNull=repcap.CellNull.Default, bwPartNull=repcap.BwPartNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:CELL<ST0>:UL:BWP<DIR0>:PUSCh:FHOP \n
		Snippet: driver.source.bb.nr5G.ubwp.user.cell.uplink.bwp.pusch.fhop.set(sel_freq_hopp = enums.UlfReqHopping.DIS, userNull = repcap.UserNull.Default, cellNull = repcap.CellNull.Default, bwPartNull = repcap.BwPartNull.Default) \n
		Disables or enables inter- or intra-slot frequency hopping. \n
			:param sel_freq_hopp: DIS| INTRA| INTER DIS Disable frequency hopping. INTRA Enable intra slot frequency hopping. Both intra- and inter-subframe hopping are performed. The PUSCH position in terms of used resource blocks is changed each slot and each subframe. INTER Enable inter-slot frequency hopping. The PUSCH position in terms of used resource blocks is changed each subframe.
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param bwPartNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Bwp')
		"""
		param = Conversions.enum_scalar_to_str(sel_freq_hopp, enums.UlfReqHopping)
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		bwPartNull_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPartNull, repcap.BwPartNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:CELL{cellNull_cmd_val}:UL:BWP{bwPartNull_cmd_val}:PUSCh:FHOP {param}')

	# noinspection PyTypeChecker
	def get(self, userNull=repcap.UserNull.Default, cellNull=repcap.CellNull.Default, bwPartNull=repcap.BwPartNull.Default) -> enums.UlfReqHopping:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:CELL<ST0>:UL:BWP<DIR0>:PUSCh:FHOP \n
		Snippet: value: enums.UlfReqHopping = driver.source.bb.nr5G.ubwp.user.cell.uplink.bwp.pusch.fhop.get(userNull = repcap.UserNull.Default, cellNull = repcap.CellNull.Default, bwPartNull = repcap.BwPartNull.Default) \n
		Disables or enables inter- or intra-slot frequency hopping. \n
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param bwPartNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Bwp')
			:return: sel_freq_hopp: DIS| INTRA| INTER DIS Disable frequency hopping. INTRA Enable intra slot frequency hopping. Both intra- and inter-subframe hopping are performed. The PUSCH position in terms of used resource blocks is changed each slot and each subframe. INTER Enable inter-slot frequency hopping. The PUSCH position in terms of used resource blocks is changed each subframe."""
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		bwPartNull_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPartNull, repcap.BwPartNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:CELL{cellNull_cmd_val}:UL:BWP{bwPartNull_cmd_val}:PUSCh:FHOP?')
		return Conversions.str_to_scalar_enum(response, enums.UlfReqHopping)
