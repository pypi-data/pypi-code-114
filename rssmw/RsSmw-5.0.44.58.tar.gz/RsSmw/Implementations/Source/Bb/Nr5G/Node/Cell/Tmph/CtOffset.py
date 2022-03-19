from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CtOffset:
	"""CtOffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ctOffset", core, parent)

	def set(self, cust_timing_offs: int, cellNull=repcap.CellNull.Nr0) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:TMPH:CTOFfset \n
		Snippet: driver.source.bb.nr5G.node.cell.tmph.ctOffset.set(cust_timing_offs = 1, cellNull = repcap.CellNull.Nr0) \n
		Defines a cell specific custom timing advance offset in terms of time (Tc) .
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select more than one carrier ([:SOURce<hw>]:BB:NR5G:NODE:NCARrier) . \n
			:param cust_timing_offs: integer Range: -2004572 to 1964636
			:param cellNull: optional repeated capability selector. Default value: Nr0
		"""
		param = Conversions.decimal_value_to_str(cust_timing_offs)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:TMPH:CTOFfset {param}')

	def get(self, cellNull=repcap.CellNull.Nr0) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:TMPH:CTOFfset \n
		Snippet: value: int = driver.source.bb.nr5G.node.cell.tmph.ctOffset.get(cellNull = repcap.CellNull.Nr0) \n
		Defines a cell specific custom timing advance offset in terms of time (Tc) .
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select more than one carrier ([:SOURce<hw>]:BB:NR5G:NODE:NCARrier) . \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:return: cust_timing_offs: No help available"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:TMPH:CTOFfset?')
		return Conversions.str_to_int(response)
