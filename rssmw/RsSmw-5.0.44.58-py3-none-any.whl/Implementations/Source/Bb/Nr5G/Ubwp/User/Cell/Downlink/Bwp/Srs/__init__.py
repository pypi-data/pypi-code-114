from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Srs:
	"""Srs commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("srs", core, parent)

	@property
	def bd23(self):
		"""bd23 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bd23'):
			from .Bd23 import Bd23
			self._bd23 = Bd23(self._core, self._cmd_group)
		return self._bd23

	@property
	def gtype(self):
		"""gtype commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gtype'):
			from .Gtype import Gtype
			self._gtype = Gtype(self._core, self._cmd_group)
		return self._gtype

	@property
	def nb26(self):
		"""nb26 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nb26'):
			from .Nb26 import Nb26
			self._nb26 = Nb26(self._core, self._cmd_group)
		return self._nb26

	@property
	def nscg(self):
		"""nscg commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nscg'):
			from .Nscg import Nscg
			self._nscg = Nscg(self._core, self._cmd_group)
		return self._nscg

	def clone(self) -> 'Srs':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Srs(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
