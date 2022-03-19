from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class User:
	"""User commands group definition. 8 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("user", core, parent)

	@property
	def aoTime(self):
		"""aoTime commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_aoTime'):
			from .AoTime import AoTime
			self._aoTime = AoTime(self._core, self._cmd_group)
		return self._aoTime

	@property
	def hoTime(self):
		"""hoTime commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_hoTime'):
			from .HoTime import HoTime
			self._hoTime = HoTime(self._core, self._cmd_group)
		return self._hoTime

	@property
	def sequence(self):
		"""sequence commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sequence'):
			from .Sequence import Sequence
			self._sequence = Sequence(self._core, self._cmd_group)
		return self._sequence

	@property
	def bb(self):
		"""bb commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_bb'):
			from .Bb import Bb
			self._bb = Bb(self._core, self._cmd_group)
		return self._bb

	def clone(self) -> 'User':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = User(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
