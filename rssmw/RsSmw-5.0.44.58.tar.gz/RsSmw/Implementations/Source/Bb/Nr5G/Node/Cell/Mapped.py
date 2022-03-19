from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mapped:
	"""Mapped commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mapped", core, parent)

	def set(self, cell_mapped: bool, cell=repcap.Cell.Nr1) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH>:MAPPed \n
		Snippet: driver.source.bb.nr5G.node.cell.mapped.set(cell_mapped = False, cell = repcap.Cell.Nr1) \n
		If enabled, the signal of the selected cell is mapped to the output. \n
			:param cell_mapped: 1| ON| 0| OFF
			:param cell: optional repeated capability selector. Default value: Nr1
		"""
		param = Conversions.bool_to_str(cell_mapped)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cell_cmd_val}:MAPPed {param}')

	def get(self, cell=repcap.Cell.Nr1) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH>:MAPPed \n
		Snippet: value: bool = driver.source.bb.nr5G.node.cell.mapped.get(cell = repcap.Cell.Nr1) \n
		If enabled, the signal of the selected cell is mapped to the output. \n
			:param cell: optional repeated capability selector. Default value: Nr1
			:return: cell_mapped: 1| ON| 0| OFF"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cell_cmd_val}:MAPPed?')
		return Conversions.str_to_bool(response)
