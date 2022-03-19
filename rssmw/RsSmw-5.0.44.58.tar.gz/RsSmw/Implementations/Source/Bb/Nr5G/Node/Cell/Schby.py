from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Schby:
	"""Schby commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("schby", core, parent)

	def set(self, sched_by: enums.CellAll, cellNull=repcap.CellNull.Nr0) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:SCHBy \n
		Snippet: driver.source.bb.nr5G.node.cell.schby.set(sched_by = enums.CellAll._0, cellNull = repcap.CellNull.Nr0) \n
		Displays in which cell coordinates the carrier aggregation, if there is intra-band CA. Queries the component carrier/cell
		that signals the UL and DL grants for the selected cell. The signaling cell is determined by its cell index. According to
		the 5G NR specification, cross-carrier scheduling has to be enabled per user and per component carrier.
		To enable signaling for one particular cell on the primary cell, i.e. cross-carrier scheduling, set the 'Scheduled By' to
		0. \n
			:param sched_by: 0| 1| 2| 3| 4| 5| 6| 7| 8| 9| 10| 11| 12| 13| 14| 15
			:param cellNull: optional repeated capability selector. Default value: Nr0
		"""
		param = Conversions.enum_scalar_to_str(sched_by, enums.CellAll)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:SCHBy {param}')

	# noinspection PyTypeChecker
	def get(self, cellNull=repcap.CellNull.Nr0) -> enums.CellAll:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:SCHBy \n
		Snippet: value: enums.CellAll = driver.source.bb.nr5G.node.cell.schby.get(cellNull = repcap.CellNull.Nr0) \n
		Displays in which cell coordinates the carrier aggregation, if there is intra-band CA. Queries the component carrier/cell
		that signals the UL and DL grants for the selected cell. The signaling cell is determined by its cell index. According to
		the 5G NR specification, cross-carrier scheduling has to be enabled per user and per component carrier.
		To enable signaling for one particular cell on the primary cell, i.e. cross-carrier scheduling, set the 'Scheduled By' to
		0. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:return: sched_by: 0| 1| 2| 3| 4| 5| 6| 7| 8| 9| 10| 11| 12| 13| 14| 15"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:SCHBy?')
		return Conversions.str_to_scalar_enum(response, enums.CellAll)
