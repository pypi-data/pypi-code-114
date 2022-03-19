from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PhOffset:
	"""PhOffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phOffset", core, parent)

	def set(self, phase_offset: float, cellNull=repcap.CellNull.Nr0) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:TMPH:PHOFfset \n
		Snippet: driver.source.bb.nr5G.node.cell.tmph.phOffset.set(phase_offset = 1.0, cellNull = repcap.CellNull.Nr0) \n
		Defines a cell specific phase offset. \n
			:param phase_offset: float Range: 0 to 360
			:param cellNull: optional repeated capability selector. Default value: Nr0
		"""
		param = Conversions.decimal_value_to_str(phase_offset)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:TMPH:PHOFfset {param}')

	def get(self, cellNull=repcap.CellNull.Nr0) -> float:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:TMPH:PHOFfset \n
		Snippet: value: float = driver.source.bb.nr5G.node.cell.tmph.phOffset.get(cellNull = repcap.CellNull.Nr0) \n
		Defines a cell specific phase offset. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:return: phase_offset: No help available"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:TMPH:PHOFfset?')
		return Conversions.str_to_float(response)
