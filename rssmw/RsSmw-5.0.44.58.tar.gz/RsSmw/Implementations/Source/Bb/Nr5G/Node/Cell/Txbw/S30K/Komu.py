from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Komu:
	"""Komu commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("komu", core, parent)

	def get(self, cellNull=repcap.CellNull.Nr0) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:TXBW:S30K:KOMU \n
		Snippet: value: int = driver.source.bb.nr5G.node.cell.txbw.s30K.komu.get(cellNull = repcap.CellNull.Nr0) \n
		Queries the value of the parameter k0μ. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:return: komu: integer Range: -6; 0; 6 further values indicate conflict"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:TXBW:S30K:KOMU?')
		return Conversions.str_to_int(response)
