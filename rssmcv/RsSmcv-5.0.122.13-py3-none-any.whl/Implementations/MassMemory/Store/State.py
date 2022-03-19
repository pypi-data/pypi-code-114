from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, data_set: int, destination_file: str) -> None:
		"""SCPI: MMEMory:STORe:STATe \n
		Snippet: driver.massMemory.store.state.set(data_set = 1, destination_file = '1') \n
		Stores the current instrument setting in the specified file. The instrument setting must first be stored in an internal
		memory with the same number using the common command *SAV. \n
			:param data_set: No help available
			:param destination_file: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('data_set', data_set, DataType.Integer), ArgSingle('destination_file', destination_file, DataType.String))
		self._core.io.write(f'MMEMory:STORe:STATe {param}'.rstrip())
