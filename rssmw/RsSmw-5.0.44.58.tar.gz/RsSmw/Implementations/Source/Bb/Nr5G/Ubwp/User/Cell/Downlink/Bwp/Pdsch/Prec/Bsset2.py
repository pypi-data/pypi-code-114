from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions
from ............ import enums
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bsset2:
	"""Bsset2 commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bsset2", core, parent)

	def set(self, dl_bwp_bundle_set_2: enums.PrbBundleSizeSet2, userNull=repcap.UserNull.Default, cellNull=repcap.CellNull.Default, bwPartNull=repcap.BwPartNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:CELL<ST0>:DL:BWP<DIR0>:PDSCh:PREC:BSSet2 \n
		Snippet: driver.source.bb.nr5G.ubwp.user.cell.downlink.bwp.pdsch.prec.bsset2.set(dl_bwp_bundle_set_2 = enums.PrbBundleSizeSet2.N4, userNull = repcap.UserNull.Default, cellNull = repcap.CellNull.Default, bwPartNull = repcap.BwPartNull.Default) \n
		Configures the dynamic PRB bundle type. Only available if 'Precoding' is enabled and 'Dynamic' is selected as 'PRB
		Bundling Type'. \n
			:param dl_bwp_bundle_set_2: N4| WIDeband N4 Default value. Dynamic PRB bundle size set 2 is set to N4. WIDeband Dynamic PRB bundle size set 2 is set to wideband.
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param bwPartNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Bwp')
		"""
		param = Conversions.enum_scalar_to_str(dl_bwp_bundle_set_2, enums.PrbBundleSizeSet2)
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		bwPartNull_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPartNull, repcap.BwPartNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:CELL{cellNull_cmd_val}:DL:BWP{bwPartNull_cmd_val}:PDSCh:PREC:BSSet2 {param}')

	# noinspection PyTypeChecker
	def get(self, userNull=repcap.UserNull.Default, cellNull=repcap.CellNull.Default, bwPartNull=repcap.BwPartNull.Default) -> enums.PrbBundleSizeSet2:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:CELL<ST0>:DL:BWP<DIR0>:PDSCh:PREC:BSSet2 \n
		Snippet: value: enums.PrbBundleSizeSet2 = driver.source.bb.nr5G.ubwp.user.cell.downlink.bwp.pdsch.prec.bsset2.get(userNull = repcap.UserNull.Default, cellNull = repcap.CellNull.Default, bwPartNull = repcap.BwPartNull.Default) \n
		Configures the dynamic PRB bundle type. Only available if 'Precoding' is enabled and 'Dynamic' is selected as 'PRB
		Bundling Type'. \n
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param bwPartNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Bwp')
			:return: dl_bwp_bundle_set_2: N4| WIDeband N4 Default value. Dynamic PRB bundle size set 2 is set to N4. WIDeband Dynamic PRB bundle size set 2 is set to wideband."""
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		bwPartNull_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPartNull, repcap.BwPartNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:CELL{cellNull_cmd_val}:DL:BWP{bwPartNull_cmd_val}:PDSCh:PREC:BSSet2?')
		return Conversions.str_to_scalar_enum(response, enums.PrbBundleSizeSet2)
