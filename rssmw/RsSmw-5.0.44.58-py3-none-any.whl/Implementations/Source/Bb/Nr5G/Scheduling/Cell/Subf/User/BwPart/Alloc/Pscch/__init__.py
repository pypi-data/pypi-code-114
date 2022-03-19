from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pscch:
	"""Pscch commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pscch", core, parent)

	@property
	def bdWidth(self):
		"""bdWidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bdWidth'):
			from .BdWidth import BdWidth
			self._bdWidth = BdWidth(self._core, self._cmd_group)
		return self._bdWidth

	@property
	def scrid(self):
		"""scrid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scrid'):
			from .Scrid import Scrid
			self._scrid = Scrid(self._core, self._cmd_group)
		return self._scrid

	@property
	def symLength(self):
		"""symLength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_symLength'):
			from .SymLength import SymLength
			self._symLength = SymLength(self._core, self._cmd_group)
		return self._symLength

	def clone(self) -> 'Pscch':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pscch(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
