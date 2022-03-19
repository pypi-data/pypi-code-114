from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Niot:
	"""Niot commands group definition. 41 total commands, 10 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("niot", core, parent)

	@property
	def arb(self):
		"""arb commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_arb'):
			from .Arb import Arb
			self._arb = Arb(self._core, self._cmd_group)
		return self._arb

	@property
	def dfreq(self):
		"""dfreq commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dfreq'):
			from .Dfreq import Dfreq
			self._dfreq = Dfreq(self._core, self._cmd_group)
		return self._dfreq

	@property
	def frc(self):
		"""frc commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_frc'):
			from .Frc import Frc
			self._frc = Frc(self._core, self._cmd_group)
		return self._frc

	@property
	def ghDisable(self):
		"""ghDisable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ghDisable'):
			from .GhDisable import GhDisable
			self._ghDisable = GhDisable(self._core, self._cmd_group)
		return self._ghDisable

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import Mode
			self._mode = Mode(self._core, self._cmd_group)
		return self._mode

	@property
	def npssim(self):
		"""npssim commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_npssim'):
			from .Npssim import Npssim
			self._npssim = Npssim(self._core, self._cmd_group)
		return self._npssim

	@property
	def ntransmiss(self):
		"""ntransmiss commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ntransmiss'):
			from .Ntransmiss import Ntransmiss
			self._ntransmiss = Ntransmiss(self._core, self._cmd_group)
		return self._ntransmiss

	@property
	def rbIndex(self):
		"""rbIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rbIndex'):
			from .RbIndex import RbIndex
			self._rbIndex = RbIndex(self._core, self._cmd_group)
		return self._rbIndex

	@property
	def scSpacing(self):
		"""scSpacing commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scSpacing'):
			from .ScSpacing import ScSpacing
			self._scSpacing = ScSpacing(self._core, self._cmd_group)
		return self._scSpacing

	@property
	def trans(self):
		"""trans commands group. 13 Sub-classes, 0 commands."""
		if not hasattr(self, '_trans'):
			from .Trans import Trans
			self._trans = Trans(self._core, self._cmd_group)
		return self._trans

	def clone(self) -> 'Niot':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Niot(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
