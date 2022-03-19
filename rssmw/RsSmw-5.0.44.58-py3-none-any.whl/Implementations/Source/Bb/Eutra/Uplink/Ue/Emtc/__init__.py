from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Emtc:
	"""Emtc commands group definition. 36 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("emtc", core, parent)

	@property
	def arb(self):
		"""arb commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_arb'):
			from .Arb import Arb
			self._arb = Arb(self._core, self._cmd_group)
		return self._arb

	@property
	def ceLevel(self):
		"""ceLevel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ceLevel'):
			from .CeLevel import CeLevel
			self._ceLevel = CeLevel(self._core, self._cmd_group)
		return self._ceLevel

	@property
	def hopp(self):
		"""hopp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hopp'):
			from .Hopp import Hopp
			self._hopp = Hopp(self._core, self._cmd_group)
		return self._hopp

	@property
	def ntransmiss(self):
		"""ntransmiss commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ntransmiss'):
			from .Ntransmiss import Ntransmiss
			self._ntransmiss = Ntransmiss(self._core, self._cmd_group)
		return self._ntransmiss

	@property
	def trans(self):
		"""trans commands group. 23 Sub-classes, 0 commands."""
		if not hasattr(self, '_trans'):
			from .Trans import Trans
			self._trans = Trans(self._core, self._cmd_group)
		return self._trans

	def clone(self) -> 'Emtc':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Emtc(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
