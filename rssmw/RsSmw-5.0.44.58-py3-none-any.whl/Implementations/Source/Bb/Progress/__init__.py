from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Progress:
	"""Progress commands group definition. 5 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("progress", core, parent)

	@property
	def mcoder(self):
		"""mcoder commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcoder'):
			from .Mcoder import Mcoder
			self._mcoder = Mcoder(self._core, self._cmd_group)
		return self._mcoder

	def clone(self) -> 'Progress':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Progress(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
