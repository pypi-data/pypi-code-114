from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nmessage:
	"""Nmessage commands group definition. 116 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nmessage", core, parent)

	@property
	def cnav(self):
		"""cnav commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_cnav'):
			from .Cnav import Cnav
			self._cnav = Cnav(self._core, self._cmd_group)
		return self._cnav

	@property
	def lnav(self):
		"""lnav commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_lnav'):
			from .Lnav import Lnav
			self._lnav = Lnav(self._core, self._cmd_group)
		return self._lnav

	def clone(self) -> 'Nmessage':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Nmessage(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
