from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dfreq:
	"""Dfreq commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dfreq", core, parent)

	def set(self, delta_freq: float, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:CA:CELL<CH0>:DFReq \n
		Snippet: driver.source.bb.oneweb.downlink.ca.cell.dfreq.set(delta_freq = 1.0, cellNull = repcap.CellNull.Default) \n
		No command help available \n
			:param delta_freq: No help available
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.decimal_value_to_str(delta_freq)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:CA:CELL{cellNull_cmd_val}:DFReq {param}')

	def get(self, cellNull=repcap.CellNull.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:CA:CELL<CH0>:DFReq \n
		Snippet: value: float = driver.source.bb.oneweb.downlink.ca.cell.dfreq.get(cellNull = repcap.CellNull.Default) \n
		No command help available \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: delta_freq: No help available"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ONEWeb:DL:CA:CELL{cellNull_cmd_val}:DFReq?')
		return Conversions.str_to_float(response)
