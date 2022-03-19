from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AfState:
	"""AfState commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("afState", core, parent)

	def get(self, cellNull=repcap.CellNull.Nr0) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:AFSTate \n
		Snippet: value: bool = driver.source.bb.nr5G.node.cell.afState.get(cellNull = repcap.CellNull.Nr0) \n
		No command help available \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:return: auto_value_state: No help available"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:AFSTate?')
		return Conversions.str_to_bool(response)
