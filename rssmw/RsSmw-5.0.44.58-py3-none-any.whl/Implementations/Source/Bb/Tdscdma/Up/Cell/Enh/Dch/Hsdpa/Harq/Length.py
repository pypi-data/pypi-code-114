from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Length:
	"""Length commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("length", core, parent)

	def set(self, length: int, cell=repcap.Cell.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:ENH:DCH:HSDPA:HARQ:LENGth \n
		Snippet: driver.source.bb.tdscdma.up.cell.enh.dch.hsdpa.harq.length.set(length = 1, cell = repcap.Cell.Default) \n
		Sets the number of HARQ processes. This value determines the distribution of the payload in the subframes and depends on
		the inter-TTI distance. A minimum of three HARQ Processes are required to achieve continuous data transmission. \n
			:param length: integer Range: 1 to 8
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
		"""
		param = Conversions.decimal_value_to_str(length)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:ENH:DCH:HSDPA:HARQ:LENGth {param}')

	def get(self, cell=repcap.Cell.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:ENH:DCH:HSDPA:HARQ:LENGth \n
		Snippet: value: int = driver.source.bb.tdscdma.up.cell.enh.dch.hsdpa.harq.length.get(cell = repcap.Cell.Default) \n
		Sets the number of HARQ processes. This value determines the distribution of the payload in the subframes and depends on
		the inter-TTI distance. A minimum of three HARQ Processes are required to achieve continuous data transmission. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:return: length: integer Range: 1 to 8"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:ENH:DCH:HSDPA:HARQ:LENGth?')
		return Conversions.str_to_int(response)
