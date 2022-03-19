from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class User:
	"""User commands group definition. 39 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("user", core, parent)

	@property
	def profile(self):
		"""profile commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_profile'):
			from .Profile import Profile
			self._profile = Profile(self._core, self._cmd_group)
		return self._profile

	@property
	def rx(self):
		"""rx commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_rx'):
			from .Rx import Rx
			self._rx = Rx(self._core, self._cmd_group)
		return self._rx

	@property
	def tpa(self):
		"""tpa commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_tpa'):
			from .Tpa import Tpa
			self._tpa = Tpa(self._core, self._cmd_group)
		return self._tpa

	@property
	def tx(self):
		"""tx commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_tx'):
			from .Tx import Tx
			self._tx = Tx(self._core, self._cmd_group)
		return self._tx

	def clone(self) -> 'User':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = User(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
