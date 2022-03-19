from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IndSize:
	"""IndSize commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("indSize", core, parent)

	def set(self, indicator_size_12: int, cellNull=repcap.CellNull.Nr0) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:SYINfo:INDSize \n
		Snippet: driver.source.bb.nr5G.node.cell.syInfo.indSize.set(indicator_size_12 = 1, cellNull = repcap.CellNull.Nr0) \n
		Defines the bit length of the DCI field 'Carrier Indicator' available in DCI formats 1_2. \n
			:param indicator_size_12: integer Range: 0 to 3
			:param cellNull: optional repeated capability selector. Default value: Nr0
		"""
		param = Conversions.decimal_value_to_str(indicator_size_12)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:SYINfo:INDSize {param}')

	def get(self, cellNull=repcap.CellNull.Nr0) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:SYINfo:INDSize \n
		Snippet: value: int = driver.source.bb.nr5G.node.cell.syInfo.indSize.get(cellNull = repcap.CellNull.Nr0) \n
		Defines the bit length of the DCI field 'Carrier Indicator' available in DCI formats 1_2. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:return: indicator_size_12: No help available"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:SYINfo:INDSize?')
		return Conversions.str_to_int(response)
