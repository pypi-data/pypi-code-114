from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class L1Band:
	"""L1Band commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("l1Band", core, parent)

	@property
	def b1C(self):
		"""b1C commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_b1C'):
			from .B1C import B1C
			self._b1C = B1C(self._core, self._cmd_group)
		return self._b1C

	@property
	def b1I(self):
		"""b1I commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_b1I'):
			from .B1I import B1I
			self._b1I = B1I(self._core, self._cmd_group)
		return self._b1I

	def clone(self) -> 'L1Band':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = L1Band(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
