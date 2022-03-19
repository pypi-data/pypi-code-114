from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NzqOffset:
	"""NzqOffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nzqOffset", core, parent)

	def set(self, non_zero_pq_offs: int, cellNull=repcap.CellNull.Default, csiRefSignal=repcap.CsiRefSignal.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:DRS:CELL<CH0>:CSIRs<ST>:NZQoffset \n
		Snippet: driver.source.bb.eutra.downlink.drs.cell.csirs.nzqOffset.set(non_zero_pq_offs = 1, cellNull = repcap.CellNull.Default, csiRefSignal = repcap.CsiRefSignal.Default) \n
		Sets the Q-offset. \n
			:param non_zero_pq_offs: -24| -22| -20| -18| -16| -14| -12| -10| -8| -6| -5| -4| -3| -2| -1| 0| 1| 2| 3| 4| 5| 6| 8| 10| 12| 14| 16| 18| 20| 22| 24 Positive values outside the permitted discrete values are rounded down; negative values are rounded up.
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param csiRefSignal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Csirs')
		"""
		param = Conversions.decimal_value_to_str(non_zero_pq_offs)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		csiRefSignal_cmd_val = self._cmd_group.get_repcap_cmd_value(csiRefSignal, repcap.CsiRefSignal)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:DRS:CELL{cellNull_cmd_val}:CSIRs{csiRefSignal_cmd_val}:NZQoffset {param}')

	def get(self, cellNull=repcap.CellNull.Default, csiRefSignal=repcap.CsiRefSignal.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:DRS:CELL<CH0>:CSIRs<ST>:NZQoffset \n
		Snippet: value: int = driver.source.bb.eutra.downlink.drs.cell.csirs.nzqOffset.get(cellNull = repcap.CellNull.Default, csiRefSignal = repcap.CsiRefSignal.Default) \n
		Sets the Q-offset. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param csiRefSignal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Csirs')
			:return: non_zero_pq_offs: -24| -22| -20| -18| -16| -14| -12| -10| -8| -6| -5| -4| -3| -2| -1| 0| 1| 2| 3| 4| 5| 6| 8| 10| 12| 14| 16| 18| 20| 22| 24 Positive values outside the permitted discrete values are rounded down; negative values are rounded up."""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		csiRefSignal_cmd_val = self._cmd_group.get_repcap_cmd_value(csiRefSignal, repcap.CsiRefSignal)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:DRS:CELL{cellNull_cmd_val}:CSIRs{csiRefSignal_cmd_val}:NZQoffset?')
		return Conversions.str_to_int(response)
