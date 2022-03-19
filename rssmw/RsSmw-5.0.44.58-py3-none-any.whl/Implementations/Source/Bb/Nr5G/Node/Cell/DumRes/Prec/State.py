from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, precoding_state: bool, cellNull=repcap.CellNull.Nr0) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:DUMRes:PREC:STATe \n
		Snippet: driver.source.bb.nr5G.node.cell.dumRes.prec.state.set(precoding_state = False, cellNull = repcap.CellNull.Nr0) \n
		Turns precoding for unused resource elements (dummy REs) on and off. \n
			:param precoding_state: 1| ON| 0| OFF
			:param cellNull: optional repeated capability selector. Default value: Nr0
		"""
		param = Conversions.bool_to_str(precoding_state)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:DUMRes:PREC:STATe {param}')

	def get(self, cellNull=repcap.CellNull.Nr0) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:DUMRes:PREC:STATe \n
		Snippet: value: bool = driver.source.bb.nr5G.node.cell.dumRes.prec.state.get(cellNull = repcap.CellNull.Nr0) \n
		Turns precoding for unused resource elements (dummy REs) on and off. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:return: precoding_state: No help available"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:DUMRes:PREC:STATe?')
		return Conversions.str_to_bool(response)
