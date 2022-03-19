from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Stsf:
	"""Stsf commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stsf", core, parent)

	def set(self, search_sp_start_sf: enums.EutraEmtcMpdcchStartSf, userIx=repcap.UserIx.Default, cellNull=repcap.CellNull.Default, setItem=repcap.SetItem.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:USER<CH>:EPDCch:CELL<ST0>:SET<DIR>:STSF \n
		Snippet: driver.source.bb.eutra.downlink.user.epdcch.cell.set.stsf.set(search_sp_start_sf = enums.EutraEmtcMpdcchStartSf.S1, userIx = repcap.UserIx.Default, cellNull = repcap.CellNull.Default, setItem = repcap.SetItem.Default) \n
		Sets the first subframe of the search space. \n
			:param search_sp_start_sf: S1| S1_5| S2| S2_5| S5| S8| S10| S20| S4
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param setItem: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Set')
		"""
		param = Conversions.enum_scalar_to_str(search_sp_start_sf, enums.EutraEmtcMpdcchStartSf)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		setItem_cmd_val = self._cmd_group.get_repcap_cmd_value(setItem, repcap.SetItem)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:USER{userIx_cmd_val}:EPDCch:CELL{cellNull_cmd_val}:SET{setItem_cmd_val}:STSF {param}')

	# noinspection PyTypeChecker
	def get(self, userIx=repcap.UserIx.Default, cellNull=repcap.CellNull.Default, setItem=repcap.SetItem.Default) -> enums.EutraEmtcMpdcchStartSf:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:USER<CH>:EPDCch:CELL<ST0>:SET<DIR>:STSF \n
		Snippet: value: enums.EutraEmtcMpdcchStartSf = driver.source.bb.eutra.downlink.user.epdcch.cell.set.stsf.get(userIx = repcap.UserIx.Default, cellNull = repcap.CellNull.Default, setItem = repcap.SetItem.Default) \n
		Sets the first subframe of the search space. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param setItem: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Set')
			:return: search_sp_start_sf: S1| S1_5| S2| S2_5| S5| S8| S10| S20| S4"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		setItem_cmd_val = self._cmd_group.get_repcap_cmd_value(setItem, repcap.SetItem)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:USER{userIx_cmd_val}:EPDCch:CELL{cellNull_cmd_val}:SET{setItem_cmd_val}:STSF?')
		return Conversions.str_to_scalar_enum(response, enums.EutraEmtcMpdcchStartSf)
