from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class L5Band:
	"""L5Band commands group definition. 8 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("l5Band", core, parent)

	@property
	def el5S(self):
		"""el5S commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_el5S'):
			from .El5S import El5S
			self._el5S = El5S(self._core, self._cmd_group)
		return self._el5S

	def clone(self) -> 'L5Band':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = L5Band(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
