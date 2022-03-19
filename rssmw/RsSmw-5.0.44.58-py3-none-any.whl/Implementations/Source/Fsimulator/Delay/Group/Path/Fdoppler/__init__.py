from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fdoppler:
	"""Fdoppler commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fdoppler", core, parent)

	@property
	def actual(self):
		"""actual commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_actual'):
			from .Actual import Actual
			self._actual = Actual(self._core, self._cmd_group)
		return self._actual

	@property
	def resulting(self):
		"""resulting commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_resulting'):
			from .Resulting import Resulting
			self._resulting = Resulting(self._core, self._cmd_group)
		return self._resulting

	def clone(self) -> 'Fdoppler':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Fdoppler(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
