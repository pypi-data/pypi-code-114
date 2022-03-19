from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ResPool:
	"""ResPool commands group definition. 20 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("resPool", core, parent)

	@property
	def nresPool(self):
		"""nresPool commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nresPool'):
			from .NresPool import NresPool
			self._nresPool = NresPool(self._core, self._cmd_group)
		return self._nresPool

	@property
	def res(self):
		"""res commands group. 19 Sub-classes, 0 commands."""
		if not hasattr(self, '_res'):
			from .Res import Res
			self._res = Res(self._core, self._cmd_group)
		return self._res

	def clone(self) -> 'ResPool':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ResPool(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
