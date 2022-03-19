from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PdChannel:
	"""PdChannel commands group definition. 8 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pdChannel", core, parent)

	@property
	def pinterval(self):
		"""pinterval commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pinterval'):
			from .Pinterval import Pinterval
			self._pinterval = Pinterval(self._core, self._cmd_group)
		return self._pinterval

	@property
	def psetup(self):
		"""psetup commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_psetup'):
			from .Psetup import Psetup
			self._psetup = Psetup(self._core, self._cmd_group)
		return self._psetup

	@property
	def subPacket(self):
		"""subPacket commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_subPacket'):
			from .SubPacket import SubPacket
			self._subPacket = SubPacket(self._core, self._cmd_group)
		return self._subPacket

	@property
	def windex(self):
		"""windex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_windex'):
			from .Windex import Windex
			self._windex = Windex(self._core, self._cmd_group)
		return self._windex

	def clone(self) -> 'PdChannel':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PdChannel(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
