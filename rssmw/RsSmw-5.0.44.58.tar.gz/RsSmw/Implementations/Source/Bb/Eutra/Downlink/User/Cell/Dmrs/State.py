from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, dmrs_alt_table: bool, userIx=repcap.UserIx.Default, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:USER<CH>:CELL<ST0>:DMRS:STATe \n
		Snippet: driver.source.bb.eutra.downlink.user.cell.dmrs.state.set(dmrs_alt_table = False, userIx = repcap.UserIx.Default, cellNull = repcap.CellNull.Default) \n
		Sets the value of the higher-layer parameter dmrs-tableAlt. \n
			:param dmrs_alt_table: 1| ON| 0| OFF
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.bool_to_str(dmrs_alt_table)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:USER{userIx_cmd_val}:CELL{cellNull_cmd_val}:DMRS:STATe {param}')

	def get(self, userIx=repcap.UserIx.Default, cellNull=repcap.CellNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:USER<CH>:CELL<ST0>:DMRS:STATe \n
		Snippet: value: bool = driver.source.bb.eutra.downlink.user.cell.dmrs.state.get(userIx = repcap.UserIx.Default, cellNull = repcap.CellNull.Default) \n
		Sets the value of the higher-layer parameter dmrs-tableAlt. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: dmrs_alt_table: 1| ON| 0| OFF"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:USER{userIx_cmd_val}:CELL{cellNull_cmd_val}:DMRS:STATe?')
		return Conversions.str_to_bool(response)
