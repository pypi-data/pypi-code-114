from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, userIx=repcap.UserIx.Default, cellNull=repcap.CellNull.Default, setItem=repcap.SetItem.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:USER<CH>:EPDCch:CELL<ST0>:SET<DIR>:STATe \n
		Snippet: driver.source.bb.eutra.downlink.user.epdcch.cell.set.state.set(state = False, userIx = repcap.UserIx.Default, cellNull = repcap.CellNull.Default, setItem = repcap.SetItem.Default) \n
		Enables the EPDCCH set. \n
			:param state: 1| ON| 0| OFF
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param setItem: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Set')
		"""
		param = Conversions.bool_to_str(state)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		setItem_cmd_val = self._cmd_group.get_repcap_cmd_value(setItem, repcap.SetItem)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:USER{userIx_cmd_val}:EPDCch:CELL{cellNull_cmd_val}:SET{setItem_cmd_val}:STATe {param}')

	def get(self, userIx=repcap.UserIx.Default, cellNull=repcap.CellNull.Default, setItem=repcap.SetItem.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:USER<CH>:EPDCch:CELL<ST0>:SET<DIR>:STATe \n
		Snippet: value: bool = driver.source.bb.eutra.downlink.user.epdcch.cell.set.state.get(userIx = repcap.UserIx.Default, cellNull = repcap.CellNull.Default, setItem = repcap.SetItem.Default) \n
		Enables the EPDCCH set. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param setItem: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Set')
			:return: state: 1| ON| 0| OFF"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		setItem_cmd_val = self._cmd_group.get_repcap_cmd_value(setItem, repcap.SetItem)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:USER{userIx_cmd_val}:EPDCch:CELL{cellNull_cmd_val}:SET{setItem_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
