from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ccorrection:
	"""Ccorrection commands group definition. 7 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ccorrection", core, parent)

	@property
	def dtau(self):
		"""dtau commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_dtau'):
			from .Dtau import Dtau
			self._dtau = Dtau(self._core, self._cmd_group)
		return self._dtau

	@property
	def en(self):
		"""en commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_en'):
			from .En import En
			self._en = En(self._core, self._cmd_group)
		return self._en

	@property
	def gamn(self):
		"""gamn commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_gamn'):
			from .Gamn import Gamn
			self._gamn = Gamn(self._core, self._cmd_group)
		return self._gamn

	@property
	def taun(self):
		"""taun commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_taun'):
			from .Taun import Taun
			self._taun = Taun(self._core, self._cmd_group)
		return self._taun

	def clone(self) -> 'Ccorrection':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ccorrection(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
