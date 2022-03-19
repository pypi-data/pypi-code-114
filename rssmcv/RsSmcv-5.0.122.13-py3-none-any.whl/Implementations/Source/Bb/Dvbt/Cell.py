from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cell:
	"""Cell commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cell", core, parent)

	def get_id(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVBT:CELL:ID \n
		Snippet: value: int = driver.source.bb.dvbt.cell.get_id() \n
		Sets the cell ID in four-digit hexadecimal format. \n
			:return: cell_id: integer Range: #H0000 to #HFFFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBT:CELL:ID?')
		return Conversions.str_to_int(response)

	def set_id(self, cell_id: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBT:CELL:ID \n
		Snippet: driver.source.bb.dvbt.cell.set_id(cell_id = 1) \n
		Sets the cell ID in four-digit hexadecimal format. \n
			:param cell_id: integer Range: #H0000 to #HFFFF
		"""
		param = Conversions.decimal_value_to_str(cell_id)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBT:CELL:ID {param}')
