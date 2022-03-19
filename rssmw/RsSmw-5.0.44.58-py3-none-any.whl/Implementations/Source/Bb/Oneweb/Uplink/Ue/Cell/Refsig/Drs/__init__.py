from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Drs:
	"""Drs commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("drs", core, parent)

	@property
	def dwocc(self):
		"""dwocc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dwocc'):
			from .Dwocc import Dwocc
			self._dwocc = Dwocc(self._core, self._cmd_group)
		return self._dwocc

	@property
	def powOffset(self):
		"""powOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_powOffset'):
			from .PowOffset import PowOffset
			self._powOffset = PowOffset(self._core, self._cmd_group)
		return self._powOffset

	def clone(self) -> 'Drs':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Drs(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
