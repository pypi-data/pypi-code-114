from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Lion:
	"""Lion commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lion", core, parent)

	@property
	def eg(self):
		"""eg commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_eg'):
			from .Eg import Eg
			self._eg = Eg(self._core, self._cmd_group)
		return self._eg

	@property
	def ils(self):
		"""ils commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ils'):
			from .Ils import Ils
			self._ils = Ils(self._core, self._cmd_group)
		return self._ils

	@property
	def la(self):
		"""la commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_la'):
			from .La import La
			self._la = La(self._core, self._cmd_group)
		return self._la

	@property
	def lsn(self):
		"""lsn commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lsn'):
			from .Lsn import Lsn
			self._lsn = Lsn(self._core, self._cmd_group)
		return self._lsn

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def clone(self) -> 'Lion':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Lion(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
