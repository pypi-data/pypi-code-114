from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Count:
	"""Count commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def get_max(self) -> float:
		"""SCPI: SYSTem:PROFiling:RECord:COUNt:MAX \n
		Snippet: value: float = driver.system.profiling.record.count.get_max() \n
		No command help available \n
			:return: count: No help available
		"""
		response = self._core.io.query_str('SYSTem:PROFiling:RECord:COUNt:MAX?')
		return Conversions.str_to_float(response)

	def set_max(self, count: float) -> None:
		"""SCPI: SYSTem:PROFiling:RECord:COUNt:MAX \n
		Snippet: driver.system.profiling.record.count.set_max(count = 1.0) \n
		No command help available \n
			:param count: No help available
		"""
		param = Conversions.decimal_value_to_str(count)
		self._core.io.write(f'SYSTem:PROFiling:RECord:COUNt:MAX {param}')

	def get_value(self) -> float:
		"""SCPI: SYSTem:PROFiling:RECord:COUNt \n
		Snippet: value: float = driver.system.profiling.record.count.get_value() \n
		No command help available \n
			:return: count: No help available
		"""
		response = self._core.io.query_str('SYSTem:PROFiling:RECord:COUNt?')
		return Conversions.str_to_float(response)
