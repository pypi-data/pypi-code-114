from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Conversion:
	"""Conversion commands group definition. 7 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("conversion", core, parent)

	@property
	def utc(self):
		"""utc commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_utc'):
			from .Utc import Utc
			self._utc = Utc(self._core, self._cmd_group)
		return self._utc

	def clone(self) -> 'Conversion':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Conversion(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
