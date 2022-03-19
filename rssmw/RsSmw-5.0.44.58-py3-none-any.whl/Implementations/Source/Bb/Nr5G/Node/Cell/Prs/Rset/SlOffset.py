from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SlOffset:
	"""SlOffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("slOffset", core, parent)

	def set(self, prs_rs_slot_offset: int, cellNull=repcap.CellNull.Nr0, resourceSetNull=repcap.ResourceSetNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:PRS:RSET<ST0>:SLOFfset \n
		Snippet: driver.source.bb.nr5G.node.cell.prs.rset.slOffset.set(prs_rs_slot_offset = 1, cellNull = repcap.CellNull.Nr0, resourceSetNull = repcap.ResourceSetNull.Default) \n
		Sets a slot offset for the resource set with respect to the SFN0 slot 0. \n
			:param prs_rs_slot_offset: integer Range: 0 to 10239
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:param resourceSetNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Rset')
		"""
		param = Conversions.decimal_value_to_str(prs_rs_slot_offset)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		resourceSetNull_cmd_val = self._cmd_group.get_repcap_cmd_value(resourceSetNull, repcap.ResourceSetNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:PRS:RSET{resourceSetNull_cmd_val}:SLOFfset {param}')

	def get(self, cellNull=repcap.CellNull.Nr0, resourceSetNull=repcap.ResourceSetNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:PRS:RSET<ST0>:SLOFfset \n
		Snippet: value: int = driver.source.bb.nr5G.node.cell.prs.rset.slOffset.get(cellNull = repcap.CellNull.Nr0, resourceSetNull = repcap.ResourceSetNull.Default) \n
		Sets a slot offset for the resource set with respect to the SFN0 slot 0. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:param resourceSetNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Rset')
			:return: prs_rs_slot_offset: integer Range: 0 to 10239"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		resourceSetNull_cmd_val = self._cmd_group.get_repcap_cmd_value(resourceSetNull, repcap.ResourceSetNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:PRS:RSET{resourceSetNull_cmd_val}:SLOFfset?')
		return Conversions.str_to_int(response)
