from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Record:
	"""Record commands group definition. 7 total commands, 2 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("record", core, parent)

	@property
	def count(self):
		"""count commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_count'):
			from .Count import Count
			self._count = Count(self._core, self._cmd_group)
		return self._count

	@property
	def wrap(self):
		"""wrap commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_wrap'):
			from .Wrap import Wrap
			self._wrap = Wrap(self._core, self._cmd_group)
		return self._wrap

	def get(self, index: List[str]) -> List[str]:
		"""SCPI: SYSTem:PROFiling:RECord \n
		Snippet: value: List[str] = driver.system.profiling.record.get(index = ['1', '2', '3']) \n
		No command help available \n
			:param index: No help available
			:return: index: No help available"""
		param = Conversions.list_to_csv_quoted_str(index)
		response = self._core.io.query_str(f'SYSTem:PROFiling:RECord? {param}')
		return Conversions.str_to_str_list(response)

	def clear(self) -> None:
		"""SCPI: SYSTem:PROFiling:RECord:CLEar \n
		Snippet: driver.system.profiling.record.clear() \n
		No command help available \n
		"""
		self._core.io.write(f'SYSTem:PROFiling:RECord:CLEar')

	def clear_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: SYSTem:PROFiling:RECord:CLEar \n
		Snippet: driver.system.profiling.record.clear_with_opc() \n
		No command help available \n
		Same as clear, but waits for the operation to complete before continuing further. Use the RsSmcv.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SYSTem:PROFiling:RECord:CLEar', opc_timeout_ms)

	def get_ignore(self) -> float:
		"""SCPI: SYSTem:PROFiling:RECord:IGNore \n
		Snippet: value: float = driver.system.profiling.record.get_ignore() \n
		No command help available \n
			:return: count: No help available
		"""
		response = self._core.io.query_str('SYSTem:PROFiling:RECord:IGNore?')
		return Conversions.str_to_float(response)

	def set_ignore(self, count: float) -> None:
		"""SCPI: SYSTem:PROFiling:RECord:IGNore \n
		Snippet: driver.system.profiling.record.set_ignore(count = 1.0) \n
		No command help available \n
			:param count: No help available
		"""
		param = Conversions.decimal_value_to_str(count)
		self._core.io.write(f'SYSTem:PROFiling:RECord:IGNore {param}')

	def save(self, filename: str) -> None:
		"""SCPI: SYSTem:PROFiling:RECord:SAVE \n
		Snippet: driver.system.profiling.record.save(filename = '1') \n
		No command help available \n
			:param filename: No help available
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SYSTem:PROFiling:RECord:SAVE {param}')

	def clone(self) -> 'Record':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Record(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
