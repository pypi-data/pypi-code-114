from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Subframe:
	"""Subframe commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("subframe", core, parent)

	def set(self, dl_subfr_no: int, userIx=repcap.UserIx.Default, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:USER<CH>:AS:DL:CELL<ST0>:SEQelem:SUBFrame \n
		Snippet: driver.source.bb.eutra.downlink.user.asPy.downlink.cell.seqElem.subframe.set(dl_subfr_no = 1, userIx = repcap.UserIx.Default, cellNull = repcap.CellNull.Default) \n
		Sets the subframe number. \n
			:param dl_subfr_no: integer Range: 0 to max
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.decimal_value_to_str(dl_subfr_no)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:USER{userIx_cmd_val}:AS:DL:CELL{cellNull_cmd_val}:SEQelem:SUBFrame {param}')

	def get(self, userIx=repcap.UserIx.Default, cellNull=repcap.CellNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:USER<CH>:AS:DL:CELL<ST0>:SEQelem:SUBFrame \n
		Snippet: value: int = driver.source.bb.eutra.downlink.user.asPy.downlink.cell.seqElem.subframe.get(userIx = repcap.UserIx.Default, cellNull = repcap.CellNull.Default) \n
		Sets the subframe number. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: dl_subfr_no: No help available"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:USER{userIx_cmd_val}:AS:DL:CELL{cellNull_cmd_val}:SEQelem:SUBFrame?')
		return Conversions.str_to_int(response)
