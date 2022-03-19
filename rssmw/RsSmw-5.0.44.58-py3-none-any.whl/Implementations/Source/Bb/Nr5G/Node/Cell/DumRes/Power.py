from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	def set(self, power: float, cellNull=repcap.CellNull.Nr0) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:DUMRes:POWer \n
		Snippet: driver.source.bb.nr5G.node.cell.dumRes.power.set(power = 1.0, cellNull = repcap.CellNull.Nr0) \n
		Sets the power of the resource elements filled in with dummy data. \n
			:param power: float Range: -80 to 10
			:param cellNull: optional repeated capability selector. Default value: Nr0
		"""
		param = Conversions.decimal_value_to_str(power)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:DUMRes:POWer {param}')

	def get(self, cellNull=repcap.CellNull.Nr0) -> float:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:DUMRes:POWer \n
		Snippet: value: float = driver.source.bb.nr5G.node.cell.dumRes.power.get(cellNull = repcap.CellNull.Nr0) \n
		Sets the power of the resource elements filled in with dummy data. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:return: power: float Range: -80 to 10"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:DUMRes:POWer?')
		return Conversions.str_to_float(response)
