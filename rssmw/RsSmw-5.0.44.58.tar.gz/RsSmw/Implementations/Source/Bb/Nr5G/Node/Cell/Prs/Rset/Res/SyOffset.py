from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SyOffset:
	"""SyOffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("syOffset", core, parent)

	def set(self, prs_res_symb_off: int, cellNull=repcap.CellNull.Nr0, resourceSetNull=repcap.ResourceSetNull.Default, resourceNull=repcap.ResourceNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:PRS:RSET<ST0>:RES<DIR0>:SYOFfset \n
		Snippet: driver.source.bb.nr5G.node.cell.prs.rset.res.syOffset.set(prs_res_symb_off = 1, cellNull = repcap.CellNull.Nr0, resourceSetNull = repcap.ResourceSetNull.Default, resourceNull = repcap.ResourceNull.Default) \n
		Sets the starting symbol of the resource within a slot. \n
			:param prs_res_symb_off: integer Range: 0 to 12
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:param resourceSetNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Rset')
			:param resourceNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Res')
		"""
		param = Conversions.decimal_value_to_str(prs_res_symb_off)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		resourceSetNull_cmd_val = self._cmd_group.get_repcap_cmd_value(resourceSetNull, repcap.ResourceSetNull)
		resourceNull_cmd_val = self._cmd_group.get_repcap_cmd_value(resourceNull, repcap.ResourceNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:PRS:RSET{resourceSetNull_cmd_val}:RES{resourceNull_cmd_val}:SYOFfset {param}')

	def get(self, cellNull=repcap.CellNull.Nr0, resourceSetNull=repcap.ResourceSetNull.Default, resourceNull=repcap.ResourceNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:PRS:RSET<ST0>:RES<DIR0>:SYOFfset \n
		Snippet: value: int = driver.source.bb.nr5G.node.cell.prs.rset.res.syOffset.get(cellNull = repcap.CellNull.Nr0, resourceSetNull = repcap.ResourceSetNull.Default, resourceNull = repcap.ResourceNull.Default) \n
		Sets the starting symbol of the resource within a slot. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:param resourceSetNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Rset')
			:param resourceNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Res')
			:return: prs_res_symb_off: integer Range: 0 to 12"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		resourceSetNull_cmd_val = self._cmd_group.get_repcap_cmd_value(resourceSetNull, repcap.ResourceSetNull)
		resourceNull_cmd_val = self._cmd_group.get_repcap_cmd_value(resourceNull, repcap.ResourceNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:PRS:RSET{resourceSetNull_cmd_val}:RES{resourceNull_cmd_val}:SYOFfset?')
		return Conversions.str_to_int(response)
