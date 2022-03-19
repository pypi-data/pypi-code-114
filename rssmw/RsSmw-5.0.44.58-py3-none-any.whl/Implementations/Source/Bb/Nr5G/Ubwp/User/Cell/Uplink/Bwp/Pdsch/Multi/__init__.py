from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Multi:
	"""Multi commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("multi", core, parent)

	@property
	def plen(self):
		"""plen commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_plen'):
			from .Plen import Plen
			self._plen = Plen(self._core, self._cmd_group)
		return self._plen

	@property
	def tdaNum(self):
		"""tdaNum commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tdaNum'):
			from .TdaNum import TdaNum
			self._tdaNum = TdaNum(self._core, self._cmd_group)
		return self._tdaNum

	def clone(self) -> 'Multi':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Multi(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
