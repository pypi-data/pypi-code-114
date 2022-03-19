from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Profiling:
	"""Profiling commands group definition. 18 total commands, 6 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("profiling", core, parent)

	@property
	def hwAccess(self):
		"""hwAccess commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_hwAccess'):
			from .HwAccess import HwAccess
			self._hwAccess = HwAccess(self._core, self._cmd_group)
		return self._hwAccess

	@property
	def logging(self):
		"""logging commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_logging'):
			from .Logging import Logging
			self._logging = Logging(self._core, self._cmd_group)
		return self._logging

	@property
	def module(self):
		"""module commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_module'):
			from .Module import Module
			self._module = Module(self._core, self._cmd_group)
		return self._module

	@property
	def record(self):
		"""record commands group. 2 Sub-classes, 4 commands."""
		if not hasattr(self, '_record'):
			from .Record import Record
			self._record = Record(self._core, self._cmd_group)
		return self._record

	@property
	def tick(self):
		"""tick commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_tick'):
			from .Tick import Tick
			self._tick = Tick(self._core, self._cmd_group)
		return self._tick

	@property
	def tpoint(self):
		"""tpoint commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_tpoint'):
			from .Tpoint import Tpoint
			self._tpoint = Tpoint(self._core, self._cmd_group)
		return self._tpoint

	def get_state(self) -> bool:
		"""SCPI: SYSTem:PROFiling:STATe \n
		Snippet: value: bool = driver.system.profiling.get_state() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('SYSTem:PROFiling:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: SYSTem:PROFiling:STATe \n
		Snippet: driver.system.profiling.set_state(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SYSTem:PROFiling:STATe {param}')

	def clone(self) -> 'Profiling':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Profiling(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
