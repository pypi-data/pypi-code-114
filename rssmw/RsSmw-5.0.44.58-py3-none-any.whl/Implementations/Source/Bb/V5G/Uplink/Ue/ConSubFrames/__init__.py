from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ConSubFrames:
	"""ConSubFrames commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("conSubFrames", core, parent)

	@property
	def xpucch(self):
		"""xpucch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_xpucch'):
			from .Xpucch import Xpucch
			self._xpucch = Xpucch(self._core, self._cmd_group)
		return self._xpucch

	@property
	def xpusch(self):
		"""xpusch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_xpusch'):
			from .Xpusch import Xpusch
			self._xpusch = Xpusch(self._core, self._cmd_group)
		return self._xpusch

	def clone(self) -> 'ConSubFrames':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ConSubFrames(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
