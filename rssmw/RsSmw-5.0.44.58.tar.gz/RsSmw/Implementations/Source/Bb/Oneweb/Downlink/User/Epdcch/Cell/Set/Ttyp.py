from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ttyp:
	"""Ttyp commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ttyp", core, parent)

	def set(self, trans_type: enums.EpdcchTransType, userIx=repcap.UserIx.Default, cellNull=repcap.CellNull.Default, setItem=repcap.SetItem.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:USER<CH>:EPDCch:CELL<ST0>:SET<DIR>:TTYP \n
		Snippet: driver.source.bb.oneweb.downlink.user.epdcch.cell.set.ttyp.set(trans_type = enums.EpdcchTransType.DISTributed, userIx = repcap.UserIx.Default, cellNull = repcap.CellNull.Default, setItem = repcap.SetItem.Default) \n
		No command help available \n
			:param trans_type: No help available
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param setItem: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Set')
		"""
		param = Conversions.enum_scalar_to_str(trans_type, enums.EpdcchTransType)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		setItem_cmd_val = self._cmd_group.get_repcap_cmd_value(setItem, repcap.SetItem)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:USER{userIx_cmd_val}:EPDCch:CELL{cellNull_cmd_val}:SET{setItem_cmd_val}:TTYP {param}')

	# noinspection PyTypeChecker
	def get(self, userIx=repcap.UserIx.Default, cellNull=repcap.CellNull.Default, setItem=repcap.SetItem.Default) -> enums.EpdcchTransType:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:USER<CH>:EPDCch:CELL<ST0>:SET<DIR>:TTYP \n
		Snippet: value: enums.EpdcchTransType = driver.source.bb.oneweb.downlink.user.epdcch.cell.set.ttyp.get(userIx = repcap.UserIx.Default, cellNull = repcap.CellNull.Default, setItem = repcap.SetItem.Default) \n
		No command help available \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param setItem: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Set')
			:return: trans_type: No help available"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		setItem_cmd_val = self._cmd_group.get_repcap_cmd_value(setItem, repcap.SetItem)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ONEWeb:DL:USER{userIx_cmd_val}:EPDCch:CELL{cellNull_cmd_val}:SET{setItem_cmd_val}:TTYP?')
		return Conversions.str_to_scalar_enum(response, enums.EpdcchTransType)
