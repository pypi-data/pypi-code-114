from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Id2:
	"""Id2 commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("id2", core, parent)

	def set(self, ident: int, userIx=repcap.UserIx.Default, cell=repcap.Cell.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:USER<CH>:SCRambling:CELL<ST>:DMRS:ID2 \n
		Snippet: driver.source.bb.eutra.downlink.user.scrambling.cell.dmrs.id2.set(ident = 1, userIx = repcap.UserIx.Default, cell = repcap.Cell.Default) \n
		Sets the DMRS scrambling identity. \n
			:param ident: integer Range: 0 to 503
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
		"""
		param = Conversions.decimal_value_to_str(ident)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:USER{userIx_cmd_val}:SCRambling:CELL{cell_cmd_val}:DMRS:ID2 {param}')

	def get(self, userIx=repcap.UserIx.Default, cell=repcap.Cell.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:USER<CH>:SCRambling:CELL<ST>:DMRS:ID2 \n
		Snippet: value: int = driver.source.bb.eutra.downlink.user.scrambling.cell.dmrs.id2.get(userIx = repcap.UserIx.Default, cell = repcap.Cell.Default) \n
		Sets the DMRS scrambling identity. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:return: ident: integer Range: 0 to 503"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:USER{userIx_cmd_val}:SCRambling:CELL{cell_cmd_val}:DMRS:ID2?')
		return Conversions.str_to_int(response)
