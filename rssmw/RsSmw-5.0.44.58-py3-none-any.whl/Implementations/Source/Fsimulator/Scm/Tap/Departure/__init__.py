from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Departure:
	"""Departure commands group definition. 4 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("departure", core, parent)

	@property
	def angle(self):
		"""angle commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_angle'):
			from .Angle import Angle
			self._angle = Angle(self._core, self._cmd_group)
		return self._angle

	@property
	def spread(self):
		"""spread commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_spread'):
			from .Spread import Spread
			self._spread = Spread(self._core, self._cmd_group)
		return self._spread

	@property
	def zenith(self):
		"""zenith commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_zenith'):
			from .Zenith import Zenith
			self._zenith = Zenith(self._core, self._cmd_group)
		return self._zenith

	def clone(self) -> 'Departure':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Departure(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
