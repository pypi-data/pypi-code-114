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

	def set(self, csi_rs_state: bool, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:CSIS:[CELL<CH0>]:STATe \n
		Snippet: driver.source.bb.v5G.downlink.csis.cell.state.set(csi_rs_state = False, cellNull = repcap.CellNull.Default) \n
		No command help available \n
			:param csi_rs_state: No help available
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.bool_to_str(csi_rs_state)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:CSIS:CELL{cellNull_cmd_val}:STATe {param}')

	def get(self, cellNull=repcap.CellNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:CSIS:[CELL<CH0>]:STATe \n
		Snippet: value: bool = driver.source.bb.v5G.downlink.csis.cell.state.get(cellNull = repcap.CellNull.Default) \n
		No command help available \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: csi_rs_state: No help available"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:V5G:DL:CSIS:CELL{cellNull_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
