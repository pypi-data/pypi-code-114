from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rate:
	"""Rate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rate", core, parent)

	def set(self, rate: float, cell=repcap.Cell.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:ENH:DCH:BLOCk:RATE \n
		Snippet: driver.source.bb.tdscdma.down.cell.enh.dch.block.rate.set(rate = 1.0, cell = repcap.Cell.Default) \n
		Sets the block error rate. \n
			:param rate: float Range: 1E-4 to 0.5
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
		"""
		param = Conversions.decimal_value_to_str(rate)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:ENH:DCH:BLOCk:RATE {param}')

	def get(self, cell=repcap.Cell.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:ENH:DCH:BLOCk:RATE \n
		Snippet: value: float = driver.source.bb.tdscdma.down.cell.enh.dch.block.rate.get(cell = repcap.Cell.Default) \n
		Sets the block error rate. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:return: rate: float Range: 1E-4 to 0.5"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:ENH:DCH:BLOCk:RATE?')
		return Conversions.str_to_float(response)
