from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Table:
	"""Table commands group definition. 7 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("table", core, parent)

	@property
	def long(self):
		"""long commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_long'):
			from .Long import Long
			self._long = Long(self._core, self._cmd_group)
		return self._long

	@property
	def short(self):
		"""short commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_short'):
			from .Short import Short
			self._short = Short(self._core, self._cmd_group)
		return self._short

	def clone(self) -> 'Table':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Table(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
