from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Eucc:
	"""Eucc commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("eucc", core, parent)

	@property
	def ccount(self):
		"""ccount commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ccount'):
			from .Ccount import Ccount
			self._ccount = Ccount(self._core, self._cmd_group)
		return self._ccount

	@property
	def hpid(self):
		"""hpid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hpid'):
			from .Hpid import Hpid
			self._hpid = Hpid(self._core, self._cmd_group)
		return self._hpid

	@property
	def rsNumber(self):
		"""rsNumber commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rsNumber'):
			from .RsNumber import RsNumber
			self._rsNumber = RsNumber(self._core, self._cmd_group)
		return self._rsNumber

	@property
	def tfci(self):
		"""tfci commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tfci'):
			from .Tfci import Tfci
			self._tfci = Tfci(self._core, self._cmd_group)
		return self._tfci

	def clone(self) -> 'Eucc':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Eucc(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
