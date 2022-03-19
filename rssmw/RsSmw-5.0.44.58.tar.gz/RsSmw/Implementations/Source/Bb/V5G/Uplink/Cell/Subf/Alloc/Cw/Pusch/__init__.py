from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pusch:
	"""Pusch commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pusch", core, parent)

	@property
	def ccoding(self):
		"""ccoding commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ccoding'):
			from .Ccoding import Ccoding
			self._ccoding = Ccoding(self._core, self._cmd_group)
		return self._ccoding

	@property
	def ri(self):
		"""ri commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ri'):
			from .Ri import Ri
			self._ri = Ri(self._core, self._cmd_group)
		return self._ri

	@property
	def ulsch(self):
		"""ulsch commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ulsch'):
			from .Ulsch import Ulsch
			self._ulsch = Ulsch(self._core, self._cmd_group)
		return self._ulsch

	def clone(self) -> 'Pusch':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pusch(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
