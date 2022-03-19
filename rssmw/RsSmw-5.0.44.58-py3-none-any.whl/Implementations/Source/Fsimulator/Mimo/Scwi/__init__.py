from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scwi:
	"""Scwi commands group definition. 11 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scwi", core, parent)

	@property
	def cluster(self):
		"""cluster commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_cluster'):
			from .Cluster import Cluster
			self._cluster = Cluster(self._core, self._cmd_group)
		return self._cluster

	@property
	def tap(self):
		"""tap commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_tap'):
			from .Tap import Tap
			self._tap = Tap(self._core, self._cmd_group)
		return self._tap

	def clone(self) -> 'Scwi':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Scwi(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
