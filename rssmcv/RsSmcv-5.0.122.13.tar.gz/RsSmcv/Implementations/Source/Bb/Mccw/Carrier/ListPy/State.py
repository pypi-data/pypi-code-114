from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, states: List[int]) -> None:
		"""SCPI: [SOURce<HW>]:BB:MCCW:CARRier:LIST:STATe \n
		Snippet: driver.source.bb.mccw.carrier.listPy.state.set(states = [1, 2, 3]) \n
		No command help available \n
			:param states: No help available
		"""
		param = Conversions.list_to_csv_str(states)
		self._core.io.write(f'SOURce<HwInstance>:BB:MCCW:CARRier:LIST:STATe {param}')

	def get(self, start: int, count: int) -> List[int]:
		"""SCPI: [SOURce<HW>]:BB:MCCW:CARRier:LIST:STATe \n
		Snippet: value: List[int] = driver.source.bb.mccw.carrier.listPy.state.get(start = 1, count = 1) \n
		No command help available \n
			:param start: No help available
			:param count: No help available
			:return: states: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('start', start, DataType.Integer), ArgSingle('count', count, DataType.Integer))
		response = self._core.io.query_bin_or_ascii_int_list(f'SOURce<HwInstance>:BB:MCCW:CARRier:LIST:STATe? {param}'.rstrip())
		return response
