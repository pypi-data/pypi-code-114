from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Id1:
	"""Id1 commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("id1", core, parent)

	def set(self, ident: int, userIx=repcap.UserIx.Default, cell=repcap.Cell.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:USER<CH>:SCRambling:CELL<ST>:DMRS:ID1 \n
		Snippet: driver.source.bb.oneweb.downlink.user.scrambling.cell.dmrs.id1.set(ident = 1, userIx = repcap.UserIx.Default, cell = repcap.Cell.Default) \n
		No command help available \n
			:param ident: No help available
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
		"""
		param = Conversions.decimal_value_to_str(ident)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:USER{userIx_cmd_val}:SCRambling:CELL{cell_cmd_val}:DMRS:ID1 {param}')

	def get(self, userIx=repcap.UserIx.Default, cell=repcap.Cell.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:USER<CH>:SCRambling:CELL<ST>:DMRS:ID1 \n
		Snippet: value: int = driver.source.bb.oneweb.downlink.user.scrambling.cell.dmrs.id1.get(userIx = repcap.UserIx.Default, cell = repcap.Cell.Default) \n
		No command help available \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:return: ident: No help available"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ONEWeb:DL:USER{userIx_cmd_val}:SCRambling:CELL{cell_cmd_val}:DMRS:ID1?')
		return Conversions.str_to_int(response)
