from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RepFactor:
	"""RepFactor commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("repFactor", core, parent)

	def set(self, prs_rs_rep_factor: enums.PrsRepFactor, cellNull=repcap.CellNull.Nr0, resourceSetNull=repcap.ResourceSetNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:PRS:RSET<ST0>:REPFactor \n
		Snippet: driver.source.bb.nr5G.node.cell.prs.rset.repFactor.set(prs_rs_rep_factor = enums.PrsRepFactor.REP1, cellNull = repcap.CellNull.Nr0, resourceSetNull = repcap.ResourceSetNull.Default) \n
		Sets the number of repetitions of each resource for a single instance of the resource set. \n
			:param prs_rs_rep_factor: REP32| REP16| REP8| REP4| REP1| REP2
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:param resourceSetNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Rset')
		"""
		param = Conversions.enum_scalar_to_str(prs_rs_rep_factor, enums.PrsRepFactor)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		resourceSetNull_cmd_val = self._cmd_group.get_repcap_cmd_value(resourceSetNull, repcap.ResourceSetNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:PRS:RSET{resourceSetNull_cmd_val}:REPFactor {param}')

	# noinspection PyTypeChecker
	def get(self, cellNull=repcap.CellNull.Nr0, resourceSetNull=repcap.ResourceSetNull.Default) -> enums.PrsRepFactor:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:PRS:RSET<ST0>:REPFactor \n
		Snippet: value: enums.PrsRepFactor = driver.source.bb.nr5G.node.cell.prs.rset.repFactor.get(cellNull = repcap.CellNull.Nr0, resourceSetNull = repcap.ResourceSetNull.Default) \n
		Sets the number of repetitions of each resource for a single instance of the resource set. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:param resourceSetNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Rset')
			:return: prs_rs_rep_factor: REP32| REP16| REP8| REP4| REP1| REP2"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		resourceSetNull_cmd_val = self._cmd_group.get_repcap_cmd_value(resourceSetNull, repcap.ResourceSetNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:PRS:RSET{resourceSetNull_cmd_val}:REPFactor?')
		return Conversions.str_to_scalar_enum(response, enums.PrsRepFactor)
