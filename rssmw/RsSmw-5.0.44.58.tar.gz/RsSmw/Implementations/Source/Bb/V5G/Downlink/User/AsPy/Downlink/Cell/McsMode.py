from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class McsMode:
	"""McsMode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mcsMode", core, parent)

	def set(self, mcs_mode: enums.AsEqMcsMode, userIx=repcap.UserIx.Default, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:USER<CH>:AS:DL:CELL<ST0>:MCSMode \n
		Snippet: driver.source.bb.v5G.downlink.user.asPy.downlink.cell.mcsMode.set(mcs_mode = enums.AsEqMcsMode.FIXed, userIx = repcap.UserIx.Default, cellNull = repcap.CellNull.Default) \n
		No command help available \n
			:param mcs_mode: No help available
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.enum_scalar_to_str(mcs_mode, enums.AsEqMcsMode)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:USER{userIx_cmd_val}:AS:DL:CELL{cellNull_cmd_val}:MCSMode {param}')

	# noinspection PyTypeChecker
	def get(self, userIx=repcap.UserIx.Default, cellNull=repcap.CellNull.Default) -> enums.AsEqMcsMode:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:USER<CH>:AS:DL:CELL<ST0>:MCSMode \n
		Snippet: value: enums.AsEqMcsMode = driver.source.bb.v5G.downlink.user.asPy.downlink.cell.mcsMode.get(userIx = repcap.UserIx.Default, cellNull = repcap.CellNull.Default) \n
		No command help available \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: mcs_mode: No help available"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:V5G:DL:USER{userIx_cmd_val}:AS:DL:CELL{cellNull_cmd_val}:MCSMode?')
		return Conversions.str_to_scalar_enum(response, enums.AsEqMcsMode)
