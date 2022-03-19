from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PointA:
	"""PointA commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pointA", core, parent)

	def set(self, carrier_point_a: float, cellNull=repcap.CellNull.Nr0) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:TXBW:POINta \n
		Snippet: driver.source.bb.nr5G.node.cell.txbw.pointA.set(carrier_point_a = 1.0, cellNull = repcap.CellNull.Nr0) \n
		Sets the frequency offset between the reference Point A and the center carrier frequency. \n
			:param carrier_point_a: float Range: -50e6 to 0
			:param cellNull: optional repeated capability selector. Default value: Nr0
		"""
		param = Conversions.decimal_value_to_str(carrier_point_a)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:TXBW:POINta {param}')

	def get(self, cellNull=repcap.CellNull.Nr0) -> float:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:TXBW:POINta \n
		Snippet: value: float = driver.source.bb.nr5G.node.cell.txbw.pointA.get(cellNull = repcap.CellNull.Nr0) \n
		Sets the frequency offset between the reference Point A and the center carrier frequency. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:return: carrier_point_a: float Range: -50e6 to 0"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:TXBW:POINta?')
		return Conversions.str_to_float(response)
