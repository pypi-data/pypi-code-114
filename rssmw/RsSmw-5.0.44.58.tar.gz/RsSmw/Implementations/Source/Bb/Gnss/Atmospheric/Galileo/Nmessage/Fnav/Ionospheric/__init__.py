from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ionospheric:
	"""Ionospheric commands group definition. 3 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ionospheric", core, parent)

	@property
	def ai(self):
		"""ai commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_ai'):
			from .Ai import Ai
			self._ai = Ai(self._core, self._cmd_group)
		return self._ai

	@property
	def sf(self):
		"""sf commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sf'):
			from .Sf import Sf
			self._sf = Sf(self._core, self._cmd_group)
		return self._sf

	def clone(self) -> 'Ionospheric':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ionospheric(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
