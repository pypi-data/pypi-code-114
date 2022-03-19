from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class N1Id:
	"""N1Id commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("n1Id", core, parent)

	def get(self, cellNull=repcap.CellNull.Nr0) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:N1ID \n
		Snippet: value: int = driver.source.bb.nr5G.node.cell.n1Id.get(cellNull = repcap.CellNull.Nr0) \n
		Queries the physical cell indicator group (NID(1) ) and the physical layer identity (NID(2) ). \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:return: carrier_n_1_id: integer Range: 0 to 2"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:N1ID?')
		return Conversions.str_to_int(response)
