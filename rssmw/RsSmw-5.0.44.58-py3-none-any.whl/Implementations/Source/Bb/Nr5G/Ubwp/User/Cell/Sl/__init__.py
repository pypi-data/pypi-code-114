from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sl:
	"""Sl commands group definition. 27 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sl", core, parent)

	@property
	def bwp(self):
		"""bwp commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_bwp'):
			from .Bwp import Bwp
			self._bwp = Bwp(self._core, self._cmd_group)
		return self._bwp

	@property
	def nbwParts(self):
		"""nbwParts commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nbwParts'):
			from .NbwParts import NbwParts
			self._nbwParts = NbwParts(self._core, self._cmd_group)
		return self._nbwParts

	def clone(self) -> 'Sl':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sl(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
