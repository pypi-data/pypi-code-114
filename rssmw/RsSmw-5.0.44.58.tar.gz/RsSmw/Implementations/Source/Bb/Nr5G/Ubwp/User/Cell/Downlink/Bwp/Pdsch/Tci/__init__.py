from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tci:
	"""Tci commands group definition. 4 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tci", core, parent)

	@property
	def ntcp(self):
		"""ntcp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ntcp'):
			from .Ntcp import Ntcp
			self._ntcp = Ntcp(self._core, self._cmd_group)
		return self._ntcp

	@property
	def tcv(self):
		"""tcv commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_tcv'):
			from .Tcv import Tcv
			self._tcv = Tcv(self._core, self._cmd_group)
		return self._tcv

	def clone(self) -> 'Tci':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tci(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
