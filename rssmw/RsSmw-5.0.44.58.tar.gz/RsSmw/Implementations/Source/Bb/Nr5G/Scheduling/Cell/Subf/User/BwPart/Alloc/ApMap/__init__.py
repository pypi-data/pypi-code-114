from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ApMap:
	"""ApMap commands group definition. 5 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("apMap", core, parent)

	@property
	def col(self):
		"""col commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_col'):
			from .Col import Col
			self._col = Col(self._core, self._cmd_group)
		return self._col

	@property
	def nap(self):
		"""nap commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nap'):
			from .Nap import Nap
			self._nap = Nap(self._core, self._cmd_group)
		return self._nap

	def clone(self) -> 'ApMap':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ApMap(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
