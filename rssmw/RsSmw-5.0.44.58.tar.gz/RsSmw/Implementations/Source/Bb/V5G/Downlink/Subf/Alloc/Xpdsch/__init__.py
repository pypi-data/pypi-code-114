from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Xpdsch:
	"""Xpdsch commands group definition. 7 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("xpdsch", core, parent)

	@property
	def dmrs(self):
		"""dmrs commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_dmrs'):
			from .Dmrs import Dmrs
			self._dmrs = Dmrs(self._core, self._cmd_group)
		return self._dmrs

	@property
	def nscid(self):
		"""nscid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nscid'):
			from .Nscid import Nscid
			self._nscid = Nscid(self._core, self._cmd_group)
		return self._nscid

	@property
	def pcrs(self):
		"""pcrs commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_pcrs'):
			from .Pcrs import Pcrs
			self._pcrs = Pcrs(self._core, self._cmd_group)
		return self._pcrs

	def clone(self) -> 'Xpdsch':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Xpdsch(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
