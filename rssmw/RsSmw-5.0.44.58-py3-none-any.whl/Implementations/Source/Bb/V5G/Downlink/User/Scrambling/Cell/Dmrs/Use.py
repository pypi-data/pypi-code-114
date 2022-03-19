from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Use:
	"""Use commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("use", core, parent)

	def set(self, use: bool, userIx=repcap.UserIx.Default, cell=repcap.Cell.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:USER<CH>:SCRambling:CELL<ST>:DMRS:USE \n
		Snippet: driver.source.bb.v5G.downlink.user.scrambling.cell.dmrs.use.set(use = False, userIx = repcap.UserIx.Default, cell = repcap.Cell.Default) \n
		No command help available \n
			:param use: No help available
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
		"""
		param = Conversions.bool_to_str(use)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:USER{userIx_cmd_val}:SCRambling:CELL{cell_cmd_val}:DMRS:USE {param}')

	def get(self, userIx=repcap.UserIx.Default, cell=repcap.Cell.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:USER<CH>:SCRambling:CELL<ST>:DMRS:USE \n
		Snippet: value: bool = driver.source.bb.v5G.downlink.user.scrambling.cell.dmrs.use.get(userIx = repcap.UserIx.Default, cell = repcap.Cell.Default) \n
		No command help available \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:return: use: No help available"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:V5G:DL:USER{userIx_cmd_val}:SCRambling:CELL{cell_cmd_val}:DMRS:USE?')
		return Conversions.str_to_bool(response)
