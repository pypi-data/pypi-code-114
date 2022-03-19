from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, ulca_cell_state: bool, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:CA:CELL<CH0>:STATe \n
		Snippet: driver.source.bb.oneweb.uplink.ca.cell.state.set(ulca_cell_state = False, cellNull = repcap.CellNull.Default) \n
		Activates the corresponding component carrier. \n
			:param ulca_cell_state: 0| 1| OFF| ON
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.bool_to_str(ulca_cell_state)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:UL:CA:CELL{cellNull_cmd_val}:STATe {param}')

	def get(self, cellNull=repcap.CellNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:CA:CELL<CH0>:STATe \n
		Snippet: value: bool = driver.source.bb.oneweb.uplink.ca.cell.state.get(cellNull = repcap.CellNull.Default) \n
		Activates the corresponding component carrier. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: ulca_cell_state: 0| 1| OFF| ON"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ONEWeb:UL:CA:CELL{cellNull_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
