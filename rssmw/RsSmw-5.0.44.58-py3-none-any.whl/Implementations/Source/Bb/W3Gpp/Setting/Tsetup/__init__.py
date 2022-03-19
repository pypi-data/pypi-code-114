from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tsetup:
	"""Tsetup commands group definition. 8 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tsetup", core, parent)

	@property
	def performance(self):
		"""performance commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_performance'):
			from .Performance import Performance
			self._performance = Performance(self._core, self._cmd_group)
		return self._performance

	@property
	def receiver(self):
		"""receiver commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_receiver'):
			from .Receiver import Receiver
			self._receiver = Receiver(self._core, self._cmd_group)
		return self._receiver

	def clone(self) -> 'Tsetup':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tsetup(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
