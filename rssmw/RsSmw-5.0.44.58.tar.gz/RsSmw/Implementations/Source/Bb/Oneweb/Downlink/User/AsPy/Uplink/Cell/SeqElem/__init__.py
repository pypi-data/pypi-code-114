from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SeqElem:
	"""SeqElem commands group definition. 8 total commands, 8 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("seqElem", core, parent)

	@property
	def conflict(self):
		"""conflict commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_conflict'):
			from .Conflict import Conflict
			self._conflict = Conflict(self._core, self._cmd_group)
		return self._conflict

	@property
	def harq(self):
		"""harq commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_harq'):
			from .Harq import Harq
			self._harq = Harq(self._core, self._cmd_group)
		return self._harq

	@property
	def ndi(self):
		"""ndi commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ndi'):
			from .Ndi import Ndi
			self._ndi = Ndi(self._core, self._cmd_group)
		return self._ndi

	@property
	def ptpc(self):
		"""ptpc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ptpc'):
			from .Ptpc import Ptpc
			self._ptpc = Ptpc(self._core, self._cmd_group)
		return self._ptpc

	@property
	def rba(self):
		"""rba commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rba'):
			from .Rba import Rba
			self._rba = Rba(self._core, self._cmd_group)
		return self._rba

	@property
	def rv(self):
		"""rv commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rv'):
			from .Rv import Rv
			self._rv = Rv(self._core, self._cmd_group)
		return self._rv

	@property
	def subframe(self):
		"""subframe commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_subframe'):
			from .Subframe import Subframe
			self._subframe = Subframe(self._core, self._cmd_group)
		return self._subframe

	@property
	def ulIndex(self):
		"""ulIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ulIndex'):
			from .UlIndex import UlIndex
			self._ulIndex = UlIndex(self._core, self._cmd_group)
		return self._ulIndex

	def clone(self) -> 'SeqElem':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SeqElem(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
