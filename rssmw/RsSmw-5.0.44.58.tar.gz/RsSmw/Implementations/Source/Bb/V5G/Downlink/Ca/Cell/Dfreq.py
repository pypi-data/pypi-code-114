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

	def get(self, cellNull=repcap.CellNull.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:CA:CELL<CH0>:DFReq \n
		Snippet: value: float = driver.source.bb.v5G.downlink.ca.cell.dfreq.get(cellNull = repcap.CellNull.Default) \n
		Sets the frequency offset between the central frequency of the corresponding cell and the frequency of the primary cell. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: delta_freq: float Range: -40 to 40, Unit: MHz"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:V5G:DL:CA:CELL{cellNull_cmd_val}:DFReq?')
		return Conversions.str_to_float(response)
