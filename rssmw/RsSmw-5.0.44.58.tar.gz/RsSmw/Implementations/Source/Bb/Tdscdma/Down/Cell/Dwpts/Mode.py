from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.AutoMode, cell=repcap.Cell.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:DWPTs:MODE \n
		Snippet: driver.source.bb.tdscdma.down.cell.dwpts.mode.set(mode = enums.AutoMode.AUTO, cell = repcap.Cell.Default) \n
		Selects whether to use the pilot time slot and its power or not. \n
			:param mode: AUTO| ON| OFF
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.AutoMode)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:DWPTs:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, cell=repcap.Cell.Default) -> enums.AutoMode:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:DWPTs:MODE \n
		Snippet: value: enums.AutoMode = driver.source.bb.tdscdma.down.cell.dwpts.mode.get(cell = repcap.Cell.Default) \n
		Selects whether to use the pilot time slot and its power or not. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:return: mode: AUTO| ON| OFF"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:DWPTs:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.AutoMode)
