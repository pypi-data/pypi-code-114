from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fnav:
	"""Fnav commands group definition. 3 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fnav", core, parent)

	@property
	def ionospheric(self):
		"""ionospheric commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ionospheric'):
			from .Ionospheric import Ionospheric
			self._ionospheric = Ionospheric(self._core, self._cmd_group)
		return self._ionospheric

	def clone(self) -> 'Fnav':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Fnav(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
