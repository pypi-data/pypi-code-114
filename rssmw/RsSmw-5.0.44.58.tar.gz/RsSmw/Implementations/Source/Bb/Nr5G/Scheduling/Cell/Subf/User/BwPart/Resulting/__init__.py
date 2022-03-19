from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Resulting:
	"""Resulting commands group definition. 19 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("resulting", core, parent)

	@property
	def alloc(self):
		"""alloc commands group. 17 Sub-classes, 0 commands."""
		if not hasattr(self, '_alloc'):
			from .Alloc import Alloc
			self._alloc = Alloc(self._core, self._cmd_group)
		return self._alloc

	@property
	def nalloc(self):
		"""nalloc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nalloc'):
			from .Nalloc import Nalloc
			self._nalloc = Nalloc(self._core, self._cmd_group)
		return self._nalloc

	def clone(self) -> 'Resulting':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Resulting(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
