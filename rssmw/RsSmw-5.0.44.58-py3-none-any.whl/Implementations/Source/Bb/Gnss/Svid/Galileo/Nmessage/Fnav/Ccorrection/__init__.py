from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ccorrection:
	"""Ccorrection commands group definition. 8 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ccorrection", core, parent)

	@property
	def af(self):
		"""af commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_af'):
			from .Af import Af
			self._af = Af(self._core, self._cmd_group)
		return self._af

	@property
	def bgda(self):
		"""bgda commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_bgda'):
			from .Bgda import Bgda
			self._bgda = Bgda(self._core, self._cmd_group)
		return self._bgda

	@property
	def bgdb(self):
		"""bgdb commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_bgdb'):
			from .Bgdb import Bgdb
			self._bgdb = Bgdb(self._core, self._cmd_group)
		return self._bgdb

	@property
	def toc(self):
		"""toc commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_toc'):
			from .Toc import Toc
			self._toc = Toc(self._core, self._cmd_group)
		return self._toc

	def clone(self) -> 'Ccorrection':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ccorrection(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
