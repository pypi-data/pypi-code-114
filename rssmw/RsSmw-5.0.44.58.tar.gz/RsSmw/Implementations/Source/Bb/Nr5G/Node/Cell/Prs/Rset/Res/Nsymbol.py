from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nsymbol:
	"""Nsymbol commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nsymbol", core, parent)

	# noinspection PyTypeChecker
	def get(self, cellNull=repcap.CellNull.Nr0, resourceSetNull=repcap.ResourceSetNull.Default, resourceNull=repcap.ResourceNull.Default) -> enums.PrsNumSymbols:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:PRS:RSET<ST0>:RES<DIR0>:NSYMbol \n
		Snippet: value: enums.PrsNumSymbols = driver.source.bb.nr5G.node.cell.prs.rset.res.nsymbol.get(cellNull = repcap.CellNull.Nr0, resourceSetNull = repcap.ResourceSetNull.Default, resourceNull = repcap.ResourceNull.Default) \n
		Sets the number of symbols of the resource within a slot. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:param resourceSetNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Rset')
			:param resourceNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Res')
			:return: prs_res_nsymb: S12| S6| S4| S2"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		resourceSetNull_cmd_val = self._cmd_group.get_repcap_cmd_value(resourceSetNull, repcap.ResourceSetNull)
		resourceNull_cmd_val = self._cmd_group.get_repcap_cmd_value(resourceNull, repcap.ResourceNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:PRS:RSET{resourceSetNull_cmd_val}:RES{resourceNull_cmd_val}:NSYMbol?')
		return Conversions.str_to_scalar_enum(response, enums.PrsNumSymbols)
