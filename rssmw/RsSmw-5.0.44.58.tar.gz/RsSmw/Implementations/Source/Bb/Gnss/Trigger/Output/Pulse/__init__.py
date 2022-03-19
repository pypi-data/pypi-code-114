from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pulse:
	"""Pulse commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pulse", core, parent)

	@property
	def divider(self):
		"""divider commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_divider'):
			from .Divider import Divider
			self._divider = Divider(self._core, self._cmd_group)
		return self._divider

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	@property
	def width(self):
		"""width commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_width'):
			from .Width import Width
			self._width = Width(self._core, self._cmd_group)
		return self._width

	def clone(self) -> 'Pulse':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pulse(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
