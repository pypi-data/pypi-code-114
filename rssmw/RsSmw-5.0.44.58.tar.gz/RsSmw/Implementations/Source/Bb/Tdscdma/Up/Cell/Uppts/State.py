from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def get(self, cell=repcap.Cell.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:UPPTs:STATe \n
		Snippet: value: bool = driver.source.bb.tdscdma.up.cell.uppts.state.get(cell = repcap.Cell.Default) \n
		Queries the state of the downlink/uplink pilot timeslot. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:return: state: 1| ON| 0| OFF"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:UPPTs:STATe?')
		return Conversions.str_to_bool(response)
