from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Npdcch:
	"""Npdcch commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("npdcch", core, parent)

	@property
	def fmt(self):
		"""fmt commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fmt'):
			from .Fmt import Fmt
			self._fmt = Fmt(self._core, self._cmd_group)
		return self._fmt

	@property
	def oind(self):
		"""oind commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_oind'):
			from .Oind import Oind
			self._oind = Oind(self._core, self._cmd_group)
		return self._oind

	@property
	def rep(self):
		"""rep commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rep'):
			from .Rep import Rep
			self._rep = Rep(self._core, self._cmd_group)
		return self._rep

	def clone(self) -> 'Npdcch':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Npdcch(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
