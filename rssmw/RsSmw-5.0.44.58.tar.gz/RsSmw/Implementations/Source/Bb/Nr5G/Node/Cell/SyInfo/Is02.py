from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Is02:
	"""Is02 commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("is02", core, parent)

	def set(self, indicator_size_02: int, cellNull=repcap.CellNull.Nr0) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:SYINfo:IS02 \n
		Snippet: driver.source.bb.nr5G.node.cell.syInfo.is02.set(indicator_size_02 = 1, cellNull = repcap.CellNull.Nr0) \n
		Defines the bit length of the DCI field 'Carrier Indicator' available in DCI formats 0_2. \n
			:param indicator_size_02: integer Range: 0 to 3
			:param cellNull: optional repeated capability selector. Default value: Nr0
		"""
		param = Conversions.decimal_value_to_str(indicator_size_02)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:SYINfo:IS02 {param}')

	def get(self, cellNull=repcap.CellNull.Nr0) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:SYINfo:IS02 \n
		Snippet: value: int = driver.source.bb.nr5G.node.cell.syInfo.is02.get(cellNull = repcap.CellNull.Nr0) \n
		Defines the bit length of the DCI field 'Carrier Indicator' available in DCI formats 0_2. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:return: indicator_size_02: No help available"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:SYINfo:IS02?')
		return Conversions.str_to_int(response)
