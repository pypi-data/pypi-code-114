from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Csirs:
	"""Csirs commands group definition. 44 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("csirs", core, parent)

	@property
	def azp(self):
		"""azp commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_azp'):
			from .Azp import Azp
			self._azp = Azp(self._core, self._cmd_group)
		return self._azp

	@property
	def nzp(self):
		"""nzp commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_nzp'):
			from .Nzp import Nzp
			self._nzp = Nzp(self._core, self._cmd_group)
		return self._nzp

	@property
	def zp(self):
		"""zp commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_zp'):
			from .Zp import Zp
			self._zp = Zp(self._core, self._cmd_group)
		return self._zp

	def clone(self) -> 'Csirs':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Csirs(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
