from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Enh:
	"""Enh commands group definition. 88 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("enh", core, parent)

	@property
	def dch(self):
		"""dch commands group. 17 Sub-classes, 0 commands."""
		if not hasattr(self, '_dch'):
			from .Dch import Dch
			self._dch = Dch(self._core, self._cmd_group)
		return self._dch

	def clone(self) -> 'Enh':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Enh(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
