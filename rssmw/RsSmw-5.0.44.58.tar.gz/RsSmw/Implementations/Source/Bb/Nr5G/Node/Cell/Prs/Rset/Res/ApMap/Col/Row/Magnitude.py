from .............Internal.Core import Core
from .............Internal.CommandsGroup import CommandsGroup
from .............Internal import Conversions
from ............. import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Magnitude:
	"""Magnitude commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("magnitude", core, parent)

	def set(self, prs_ap_magn: float, cellNull=repcap.CellNull.Nr0, resourceSetNull=repcap.ResourceSetNull.Default, resourceNull=repcap.ResourceNull.Default, columnNull=repcap.ColumnNull.Default, rowNull=repcap.RowNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:PRS:RSET<ST0>:RES<DIR0>:APMap:COL<GR0>:ROW<USER0>:MAGNitude \n
		Snippet: driver.source.bb.nr5G.node.cell.prs.rset.res.apMap.col.row.magnitude.set(prs_ap_magn = 1.0, cellNull = repcap.CellNull.Nr0, resourceSetNull = repcap.ResourceSetNull.Default, resourceNull = repcap.ResourceNull.Default, columnNull = repcap.ColumnNull.Default, rowNull = repcap.RowNull.Default) \n
		Sets the mapping of the antenna ports (AP) for the PRS resource, if cylindrical coordinates are used. \n
			:param prs_ap_magn: float Range: 0 to 360
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:param resourceSetNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Rset')
			:param resourceNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Res')
			:param columnNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Col')
			:param rowNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Row')
		"""
		param = Conversions.decimal_value_to_str(prs_ap_magn)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		resourceSetNull_cmd_val = self._cmd_group.get_repcap_cmd_value(resourceSetNull, repcap.ResourceSetNull)
		resourceNull_cmd_val = self._cmd_group.get_repcap_cmd_value(resourceNull, repcap.ResourceNull)
		columnNull_cmd_val = self._cmd_group.get_repcap_cmd_value(columnNull, repcap.ColumnNull)
		rowNull_cmd_val = self._cmd_group.get_repcap_cmd_value(rowNull, repcap.RowNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:PRS:RSET{resourceSetNull_cmd_val}:RES{resourceNull_cmd_val}:APMap:COL{columnNull_cmd_val}:ROW{rowNull_cmd_val}:MAGNitude {param}')

	def get(self, cellNull=repcap.CellNull.Nr0, resourceSetNull=repcap.ResourceSetNull.Default, resourceNull=repcap.ResourceNull.Default, columnNull=repcap.ColumnNull.Default, rowNull=repcap.RowNull.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:PRS:RSET<ST0>:RES<DIR0>:APMap:COL<GR0>:ROW<USER0>:MAGNitude \n
		Snippet: value: float = driver.source.bb.nr5G.node.cell.prs.rset.res.apMap.col.row.magnitude.get(cellNull = repcap.CellNull.Nr0, resourceSetNull = repcap.ResourceSetNull.Default, resourceNull = repcap.ResourceNull.Default, columnNull = repcap.ColumnNull.Default, rowNull = repcap.RowNull.Default) \n
		Sets the mapping of the antenna ports (AP) for the PRS resource, if cylindrical coordinates are used. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:param resourceSetNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Rset')
			:param resourceNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Res')
			:param columnNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Col')
			:param rowNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Row')
			:return: prs_ap_magn: No help available"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		resourceSetNull_cmd_val = self._cmd_group.get_repcap_cmd_value(resourceSetNull, repcap.ResourceSetNull)
		resourceNull_cmd_val = self._cmd_group.get_repcap_cmd_value(resourceNull, repcap.ResourceNull)
		columnNull_cmd_val = self._cmd_group.get_repcap_cmd_value(columnNull, repcap.ColumnNull)
		rowNull_cmd_val = self._cmd_group.get_repcap_cmd_value(rowNull, repcap.RowNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:PRS:RSET{resourceSetNull_cmd_val}:RES{resourceNull_cmd_val}:APMap:COL{columnNull_cmd_val}:ROW{rowNull_cmd_val}:MAGNitude?')
		return Conversions.str_to_float(response)
