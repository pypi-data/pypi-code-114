from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.Utilities import trim_str_response
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RvSequence:
	"""RvSequence commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rvSequence", core, parent)

	def set(self, rv_sequence: str, cell=repcap.Cell.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:ENH:DCH:HSUPA:RVSequence \n
		Snippet: driver.source.bb.tdscdma.up.cell.enh.dch.hsupa.rvSequence.set(rv_sequence = '1', cell = repcap.Cell.Default) \n
		For HARQ mode set to constant NACK, sets the retransmission sequence. For HSUPA, the command is a query only. \n
			:param rv_sequence: string of 30 coma-separated values The sequence length determines the maximum number of retransmissions. New data is retrieved from the data source after reaching the end of the sequence.
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
		"""
		param = Conversions.value_to_quoted_str(rv_sequence)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:ENH:DCH:HSUPA:RVSequence {param}')

	def get(self, cell=repcap.Cell.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:ENH:DCH:HSUPA:RVSequence \n
		Snippet: value: str = driver.source.bb.tdscdma.up.cell.enh.dch.hsupa.rvSequence.get(cell = repcap.Cell.Default) \n
		For HARQ mode set to constant NACK, sets the retransmission sequence. For HSUPA, the command is a query only. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:return: rv_sequence: string of 30 coma-separated values The sequence length determines the maximum number of retransmissions. New data is retrieved from the data source after reaching the end of the sequence."""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:ENH:DCH:HSUPA:RVSequence?')
		return trim_str_response(response)
