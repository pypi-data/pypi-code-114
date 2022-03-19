from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Phase:
	"""Phase commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phase", core, parent)

	def set(self, ap_phase: float, cellNull=repcap.CellNull.Nr0, columnNull=repcap.ColumnNull.Default, rowNull=repcap.RowNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:DUMRes:APMap:COL<ST0>:ROW<DIR0>:PHASe \n
		Snippet: driver.source.bb.nr5G.node.cell.dumRes.apMap.col.row.phase.set(ap_phase = 1.0, cellNull = repcap.CellNull.Nr0, columnNull = repcap.ColumnNull.Default, rowNull = repcap.RowNull.Default) \n
		Define the mapping of the antenna ports to the physical antennas for unused (dummy) resource elements in cylindrical
		mapping format (phase value) . \n
			:param ap_phase: float Range: 0 to 360
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:param columnNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Col')
			:param rowNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Row')
		"""
		param = Conversions.decimal_value_to_str(ap_phase)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		columnNull_cmd_val = self._cmd_group.get_repcap_cmd_value(columnNull, repcap.ColumnNull)
		rowNull_cmd_val = self._cmd_group.get_repcap_cmd_value(rowNull, repcap.RowNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:DUMRes:APMap:COL{columnNull_cmd_val}:ROW{rowNull_cmd_val}:PHASe {param}')

	def get(self, cellNull=repcap.CellNull.Nr0, columnNull=repcap.ColumnNull.Default, rowNull=repcap.RowNull.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:DUMRes:APMap:COL<ST0>:ROW<DIR0>:PHASe \n
		Snippet: value: float = driver.source.bb.nr5G.node.cell.dumRes.apMap.col.row.phase.get(cellNull = repcap.CellNull.Nr0, columnNull = repcap.ColumnNull.Default, rowNull = repcap.RowNull.Default) \n
		Define the mapping of the antenna ports to the physical antennas for unused (dummy) resource elements in cylindrical
		mapping format (phase value) . \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:param columnNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Col')
			:param rowNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Row')
			:return: ap_phase: float Range: 0 to 360"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		columnNull_cmd_val = self._cmd_group.get_repcap_cmd_value(columnNull, repcap.ColumnNull)
		rowNull_cmd_val = self._cmd_group.get_repcap_cmd_value(rowNull, repcap.RowNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:DUMRes:APMap:COL{columnNull_cmd_val}:ROW{rowNull_cmd_val}:PHASe?')
		return Conversions.str_to_float(response)
