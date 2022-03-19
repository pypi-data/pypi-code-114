from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Csi:
	"""Csi commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("csi", core, parent)

	@property
	def ident(self):
		"""ident commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ident'):
			from .Ident import Ident
			self._ident = Ident(self._core, self._cmd_group)
		return self._ident

	@property
	def use(self):
		"""use commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_use'):
			from .Use import Use
			self._use = Use(self._core, self._cmd_group)
		return self._use

	def clone(self) -> 'Csi':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Csi(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
