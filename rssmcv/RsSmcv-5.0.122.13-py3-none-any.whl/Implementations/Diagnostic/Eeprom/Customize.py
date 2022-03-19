from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Customize:
	"""Customize commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("customize", core, parent)

	def set(self, board: str, index: int, sub_board: int) -> None:
		"""SCPI: DIAGnostic<HW>:EEPRom:CUSTomize \n
		Snippet: driver.diagnostic.eeprom.customize.set(board = '1', index = 1, sub_board = 1) \n
		No command help available \n
			:param board: No help available
			:param index: No help available
			:param sub_board: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('board', board, DataType.String), ArgSingle('index', index, DataType.Integer), ArgSingle('sub_board', sub_board, DataType.Integer))
		self._core.io.write(f'DIAGnostic<HwInstance>:EEPRom:CUSTomize {param}'.rstrip())
