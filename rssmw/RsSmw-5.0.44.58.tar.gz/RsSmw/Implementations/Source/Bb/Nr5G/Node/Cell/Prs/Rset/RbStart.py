from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RbStart:
	"""RbStart commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rbStart", core, parent)

	def set(self, prs_rsrb_start: int, cellNull=repcap.CellNull.Nr0, resourceSetNull=repcap.ResourceSetNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:PRS:RSET<ST0>:RBSTart \n
		Snippet: driver.source.bb.nr5G.node.cell.prs.rset.rbStart.set(prs_rsrb_start = 1, cellNull = repcap.CellNull.Nr0, resourceSetNull = repcap.ResourceSetNull.Default) \n
		Sets the starting RB index of the resource set with respect to the reference point A. The point A is defined as the
		absolute frequency of the reference resource block. \n
			:param prs_rsrb_start: integer Range: 0 to 2176
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:param resourceSetNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Rset')
		"""
		param = Conversions.decimal_value_to_str(prs_rsrb_start)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		resourceSetNull_cmd_val = self._cmd_group.get_repcap_cmd_value(resourceSetNull, repcap.ResourceSetNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:PRS:RSET{resourceSetNull_cmd_val}:RBSTart {param}')

	def get(self, cellNull=repcap.CellNull.Nr0, resourceSetNull=repcap.ResourceSetNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:PRS:RSET<ST0>:RBSTart \n
		Snippet: value: int = driver.source.bb.nr5G.node.cell.prs.rset.rbStart.get(cellNull = repcap.CellNull.Nr0, resourceSetNull = repcap.ResourceSetNull.Default) \n
		Sets the starting RB index of the resource set with respect to the reference point A. The point A is defined as the
		absolute frequency of the reference resource block. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:param resourceSetNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Rset')
			:return: prs_rsrb_start: integer Range: 0 to 2176"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		resourceSetNull_cmd_val = self._cmd_group.get_repcap_cmd_value(resourceSetNull, repcap.ResourceSetNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:PRS:RSET{resourceSetNull_cmd_val}:RBSTart?')
		return Conversions.str_to_int(response)
