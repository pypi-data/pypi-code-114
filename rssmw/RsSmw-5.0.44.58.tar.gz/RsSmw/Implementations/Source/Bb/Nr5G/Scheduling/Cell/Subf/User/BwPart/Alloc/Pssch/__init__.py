from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pssch:
	"""Pssch commands group definition. 6 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pssch", core, parent)

	@property
	def dmrs(self):
		"""dmrs commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_dmrs'):
			from .Dmrs import Dmrs
			self._dmrs = Dmrs(self._core, self._cmd_group)
		return self._dmrs

	@property
	def mod(self):
		"""mod commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mod'):
			from .Mod import Mod
			self._mod = Mod(self._core, self._cmd_group)
		return self._mod

	@property
	def ndmrs(self):
		"""ndmrs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ndmrs'):
			from .Ndmrs import Ndmrs
			self._ndmrs = Ndmrs(self._core, self._cmd_group)
		return self._ndmrs

	@property
	def nsubchan(self):
		"""nsubchan commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nsubchan'):
			from .Nsubchan import Nsubchan
			self._nsubchan = Nsubchan(self._core, self._cmd_group)
		return self._nsubchan

	@property
	def pool(self):
		"""pool commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pool'):
			from .Pool import Pool
			self._pool = Pool(self._core, self._cmd_group)
		return self._pool

	@property
	def txScheme(self):
		"""txScheme commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_txScheme'):
			from .TxScheme import TxScheme
			self._txScheme = TxScheme(self._core, self._cmd_group)
		return self._txScheme

	def clone(self) -> 'Pssch':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pssch(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
