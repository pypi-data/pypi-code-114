from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hsdpa:
	"""Hsdpa commands group definition. 5 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hsdpa", core, parent)

	@property
	def derror(self):
		"""derror commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_derror'):
			from .Derror import Derror
			self._derror = Derror(self._core, self._cmd_group)
		return self._derror

	def clone(self) -> 'Hsdpa':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Hsdpa(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
