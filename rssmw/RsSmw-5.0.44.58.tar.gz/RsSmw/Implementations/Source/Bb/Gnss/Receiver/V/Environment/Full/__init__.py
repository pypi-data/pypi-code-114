from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Full:
	"""Full commands group definition. 11 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("full", core, parent)

	@property
	def area(self):
		"""area commands group. 5 Sub-classes, 1 commands."""
		if not hasattr(self, '_area'):
			from .Area import Area
			self._area = Area(self._core, self._cmd_group)
		return self._area

	@property
	def predefined(self):
		"""predefined commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_predefined'):
			from .Predefined import Predefined
			self._predefined = Predefined(self._core, self._cmd_group)
		return self._predefined

	@property
	def rwindow(self):
		"""rwindow commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_rwindow'):
			from .Rwindow import Rwindow
			self._rwindow = Rwindow(self._core, self._cmd_group)
		return self._rwindow

	@property
	def scale(self):
		"""scale commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scale'):
			from .Scale import Scale
			self._scale = Scale(self._core, self._cmd_group)
		return self._scale

	def clone(self) -> 'Full':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Full(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
