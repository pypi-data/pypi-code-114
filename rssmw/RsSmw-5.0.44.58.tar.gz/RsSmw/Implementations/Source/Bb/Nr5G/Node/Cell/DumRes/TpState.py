from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TpState:
	"""TpState commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tpState", core, parent)

	def set(self, tr_prec_state: bool, cellNull=repcap.CellNull.Nr0) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:DUMRes:TPSTate \n
		Snippet: driver.source.bb.nr5G.node.cell.dumRes.tpState.set(tr_prec_state = False, cellNull = repcap.CellNull.Nr0) \n
		In uplink, enables using the optional DFT-S scheme. \n
			:param tr_prec_state: 1| ON| 0| OFF
			:param cellNull: optional repeated capability selector. Default value: Nr0
		"""
		param = Conversions.bool_to_str(tr_prec_state)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:DUMRes:TPSTate {param}')

	def get(self, cellNull=repcap.CellNull.Nr0) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:DUMRes:TPSTate \n
		Snippet: value: bool = driver.source.bb.nr5G.node.cell.dumRes.tpState.get(cellNull = repcap.CellNull.Nr0) \n
		In uplink, enables using the optional DFT-S scheme. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:return: tr_prec_state: 1| ON| 0| OFF"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:DUMRes:TPSTate?')
		return Conversions.str_to_bool(response)
