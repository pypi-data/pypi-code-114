from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RbNumber:
	"""RbNumber commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rbNumber", core, parent)

	def set(self, prs_rs_num_rb: int, cellNull=repcap.CellNull.Nr0, resourceSetNull=repcap.ResourceSetNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:PRS:RSET<ST0>:RBNumber \n
		Snippet: driver.source.bb.nr5G.node.cell.prs.rset.rbNumber.set(prs_rs_num_rb = 1, cellNull = repcap.CellNull.Nr0, resourceSetNull = repcap.ResourceSetNull.Default) \n
		Sets the number of resource blocks (RBs) for all resources in the resource set in multiples of 4 RBs. \n
			:param prs_rs_num_rb: integer Range: 24 to 272
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:param resourceSetNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Rset')
		"""
		param = Conversions.decimal_value_to_str(prs_rs_num_rb)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		resourceSetNull_cmd_val = self._cmd_group.get_repcap_cmd_value(resourceSetNull, repcap.ResourceSetNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:PRS:RSET{resourceSetNull_cmd_val}:RBNumber {param}')

	def get(self, cellNull=repcap.CellNull.Nr0, resourceSetNull=repcap.ResourceSetNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:PRS:RSET<ST0>:RBNumber \n
		Snippet: value: int = driver.source.bb.nr5G.node.cell.prs.rset.rbNumber.get(cellNull = repcap.CellNull.Nr0, resourceSetNull = repcap.ResourceSetNull.Default) \n
		Sets the number of resource blocks (RBs) for all resources in the resource set in multiples of 4 RBs. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:param resourceSetNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Rset')
			:return: prs_rs_num_rb: integer Range: 24 to 272"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		resourceSetNull_cmd_val = self._cmd_group.get_repcap_cmd_value(resourceSetNull, repcap.ResourceSetNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:PRS:RSET{resourceSetNull_cmd_val}:RBNumber?')
		return Conversions.str_to_int(response)
