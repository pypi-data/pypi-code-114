from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Qcomponent:
	"""Qcomponent commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("qcomponent", core, parent)

	def get(self, frameBlock=repcap.FrameBlock.Default, row=repcap.Row.Default, column=repcap.Column.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:SMAPping:ROW<ST>:COL<DIR>:Q \n
		Snippet: value: float = driver.source.bb.wlnn.fblock.smapping.row.col.qcomponent.get(frameBlock = repcap.FrameBlock.Default, row = repcap.Row.Default, column = repcap.Column.Default) \n
		Queries the time shift value of element Q of the selected row and column of the spatial transmit matrix. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:param row: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Row')
			:param column: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Col')
			:return: qpart: float"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		row_cmd_val = self._cmd_group.get_repcap_cmd_value(row, repcap.Row)
		column_cmd_val = self._cmd_group.get_repcap_cmd_value(column, repcap.Column)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:SMAPping:ROW{row_cmd_val}:COL{column_cmd_val}:Q?')
		return Conversions.str_to_float(response)
