from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Index:
	"""Index commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("index", core, parent)

	def set(self, index: int, cell=repcap.Cell.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:ENH:DCH:HSDPA:TBS:INDex \n
		Snippet: driver.source.bb.tdscdma.up.cell.enh.dch.hsdpa.tbs.index.set(index = 1, cell = repcap.Cell.Default) \n
		Sets the index for the corresponding table, as described in 3GPP TS 25.321. \n
			:param index: integer Range: 0 to 63
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
		"""
		param = Conversions.decimal_value_to_str(index)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:ENH:DCH:HSDPA:TBS:INDex {param}')

	def get(self, cell=repcap.Cell.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:ENH:DCH:HSDPA:TBS:INDex \n
		Snippet: value: int = driver.source.bb.tdscdma.up.cell.enh.dch.hsdpa.tbs.index.get(cell = repcap.Cell.Default) \n
		Sets the index for the corresponding table, as described in 3GPP TS 25.321. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:return: index: integer Range: 0 to 63"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:ENH:DCH:HSDPA:TBS:INDex?')
		return Conversions.str_to_int(response)
