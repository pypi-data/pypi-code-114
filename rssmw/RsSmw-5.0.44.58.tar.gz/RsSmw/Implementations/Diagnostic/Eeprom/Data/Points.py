from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Points:
	"""Points commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("points", core, parent)

	def get(self, board: str, sub_board: str) -> int:
		"""SCPI: DIAGnostic<HW>:EEPRom:DATA:POINts \n
		Snippet: value: int = driver.diagnostic.eeprom.data.points.get(board = '1', sub_board = '1') \n
		No command help available \n
			:param board: No help available
			:param sub_board: No help available
			:return: points: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('board', board, DataType.String), ArgSingle('sub_board', sub_board, DataType.String))
		response = self._core.io.query_str(f'DIAGnostic<HwInstance>:EEPRom:DATA:POINts? {param}'.rstrip())
		return Conversions.str_to_int(response)
