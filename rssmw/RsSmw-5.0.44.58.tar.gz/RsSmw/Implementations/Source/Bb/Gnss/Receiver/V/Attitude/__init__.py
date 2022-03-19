from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Attitude:
	"""Attitude commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("attitude", core, parent)

	@property
	def pitch(self):
		"""pitch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pitch'):
			from .Pitch import Pitch
			self._pitch = Pitch(self._core, self._cmd_group)
		return self._pitch

	@property
	def roll(self):
		"""roll commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_roll'):
			from .Roll import Roll
			self._roll = Roll(self._core, self._cmd_group)
		return self._roll

	@property
	def spin(self):
		"""spin commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_spin'):
			from .Spin import Spin
			self._spin = Spin(self._core, self._cmd_group)
		return self._spin

	@property
	def yaw(self):
		"""yaw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_yaw'):
			from .Yaw import Yaw
			self._yaw = Yaw(self._core, self._cmd_group)
		return self._yaw

	@property
	def behaviour(self):
		"""behaviour commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_behaviour'):
			from .Behaviour import Behaviour
			self._behaviour = Behaviour(self._core, self._cmd_group)
		return self._behaviour

	def clone(self) -> 'Attitude':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Attitude(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
