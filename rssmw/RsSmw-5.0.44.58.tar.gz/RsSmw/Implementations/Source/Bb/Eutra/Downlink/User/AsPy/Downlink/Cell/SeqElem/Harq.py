from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Harq:
	"""Harq commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("harq", core, parent)

	def set(self, harq_proc: int, userIx=repcap.UserIx.Default, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:USER<CH>:AS:DL:CELL<ST0>:SEQelem:HARQ \n
		Snippet: driver.source.bb.eutra.downlink.user.asPy.downlink.cell.seqElem.harq.set(harq_proc = 1, userIx = repcap.UserIx.Default, cellNull = repcap.CellNull.Default) \n
		Sets the HARQ process. \n
			:param harq_proc: integer Range: 0 to 15
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.decimal_value_to_str(harq_proc)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:USER{userIx_cmd_val}:AS:DL:CELL{cellNull_cmd_val}:SEQelem:HARQ {param}')

	def get(self, userIx=repcap.UserIx.Default, cellNull=repcap.CellNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:USER<CH>:AS:DL:CELL<ST0>:SEQelem:HARQ \n
		Snippet: value: int = driver.source.bb.eutra.downlink.user.asPy.downlink.cell.seqElem.harq.get(userIx = repcap.UserIx.Default, cellNull = repcap.CellNull.Default) \n
		Sets the HARQ process. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: harq_proc: integer Range: 0 to 15"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:USER{userIx_cmd_val}:AS:DL:CELL{cellNull_cmd_val}:SEQelem:HARQ?')
		return Conversions.str_to_int(response)
