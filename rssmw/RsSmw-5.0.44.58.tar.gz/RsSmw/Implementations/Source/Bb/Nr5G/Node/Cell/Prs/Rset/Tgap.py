from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tgap:
	"""Tgap commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tgap", core, parent)

	def set(self, prs_rs_time_gap: enums.PrsTimeGap, cellNull=repcap.CellNull.Nr0, resourceSetNull=repcap.ResourceSetNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:PRS:RSET<ST0>:TGAP \n
		Snippet: driver.source.bb.nr5G.node.cell.prs.rset.tgap.set(prs_rs_time_gap = enums.PrsTimeGap.TG1, cellNull = repcap.CellNull.Nr0, resourceSetNull = repcap.ResourceSetNull.Default) \n
		Sets an offset in slots between two resources with the same resource ID within a resource set. The time gap should not
		exceed the 'Periodicity (T_per) '. \n
			:param prs_rs_time_gap: TG1| TG2| TG4| TG8| TG16| TG32
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:param resourceSetNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Rset')
		"""
		param = Conversions.enum_scalar_to_str(prs_rs_time_gap, enums.PrsTimeGap)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		resourceSetNull_cmd_val = self._cmd_group.get_repcap_cmd_value(resourceSetNull, repcap.ResourceSetNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:PRS:RSET{resourceSetNull_cmd_val}:TGAP {param}')

	# noinspection PyTypeChecker
	def get(self, cellNull=repcap.CellNull.Nr0, resourceSetNull=repcap.ResourceSetNull.Default) -> enums.PrsTimeGap:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:PRS:RSET<ST0>:TGAP \n
		Snippet: value: enums.PrsTimeGap = driver.source.bb.nr5G.node.cell.prs.rset.tgap.get(cellNull = repcap.CellNull.Nr0, resourceSetNull = repcap.ResourceSetNull.Default) \n
		Sets an offset in slots between two resources with the same resource ID within a resource set. The time gap should not
		exceed the 'Periodicity (T_per) '. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:param resourceSetNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Rset')
			:return: prs_rs_time_gap: TG1| TG2| TG4| TG8| TG16| TG32"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		resourceSetNull_cmd_val = self._cmd_group.get_repcap_cmd_value(resourceSetNull, repcap.ResourceSetNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:PRS:RSET{resourceSetNull_cmd_val}:TGAP?')
		return Conversions.str_to_scalar_enum(response, enums.PrsTimeGap)
