from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.Utilities import trim_str_response
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rsequence:
	"""Rsequence commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rsequence", core, parent)

	def set(self, rsequence: str, cell=repcap.Cell.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:ENH:DCH:HSUPA:RSEQuence \n
		Snippet: driver.source.bb.tdscdma.up.cell.enh.dch.hsupa.rsequence.set(rsequence = '1', cell = repcap.Cell.Default) \n
		(for 'HSUPA' and 'HARQ Mode' set to constant NACK) Sets the retransmission sequence. \n
			:param rsequence: string
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
		"""
		param = Conversions.value_to_quoted_str(rsequence)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:ENH:DCH:HSUPA:RSEQuence {param}')

	def get(self, cell=repcap.Cell.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:ENH:DCH:HSUPA:RSEQuence \n
		Snippet: value: str = driver.source.bb.tdscdma.up.cell.enh.dch.hsupa.rsequence.get(cell = repcap.Cell.Default) \n
		(for 'HSUPA' and 'HARQ Mode' set to constant NACK) Sets the retransmission sequence. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:return: rsequence: string"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:ENH:DCH:HSUPA:RSEQuence?')
		return trim_str_response(response)
