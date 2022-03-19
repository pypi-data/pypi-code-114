from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fcorrection:
	"""Fcorrection commands group definition. 2 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fcorrection", core, parent)

	@property
	def fixed(self):
		"""fixed commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_fixed'):
			from .Fixed import Fixed
			self._fixed = Fixed(self._core, self._cmd_group)
		return self._fixed

	def clone(self) -> 'Fcorrection':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Fcorrection(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
