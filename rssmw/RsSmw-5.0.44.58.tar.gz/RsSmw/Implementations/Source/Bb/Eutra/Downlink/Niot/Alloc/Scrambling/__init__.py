from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scrambling:
	"""Scrambling commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scrambling", core, parent)

	@property
	def legacy(self):
		"""legacy commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_legacy'):
			from .Legacy import Legacy
			self._legacy = Legacy(self._core, self._cmd_group)
		return self._legacy

	@property
	def srot(self):
		"""srot commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_srot'):
			from .Srot import Srot
			self._srot = Srot(self._core, self._cmd_group)
		return self._srot

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def ueId(self):
		"""ueId commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ueId'):
			from .UeId import UeId
			self._ueId = UeId(self._core, self._cmd_group)
		return self._ueId

	def clone(self) -> 'Scrambling':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Scrambling(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
