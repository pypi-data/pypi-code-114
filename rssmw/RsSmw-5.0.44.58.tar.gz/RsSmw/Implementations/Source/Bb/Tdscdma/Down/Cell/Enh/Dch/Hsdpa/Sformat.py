from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal.Utilities import trim_str_response
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sformat:
	"""Sformat commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sformat", core, parent)

	def get(self, cell=repcap.Cell.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:ENH:DCH:HSDPA:SFORmat \n
		Snippet: value: str = driver.source.bb.tdscdma.down.cell.enh.dch.hsdpa.sformat.get(cell = repcap.Cell.Default) \n
		Queries the slot format of the selected channel. A slot format defines the complete structure of a slot made of data and
		control fields. The slot format depends on the coding type selected. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:return: sformat: string"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:ENH:DCH:HSDPA:SFORmat?')
		return trim_str_response(response)
