from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HilPosition:
	"""HilPosition commands group definition. 2 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hilPosition", core, parent)

	@property
	def latency(self):
		"""latency commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_latency'):
			from .Latency import Latency
			self._latency = Latency(self._core, self._cmd_group)
		return self._latency

	def clone(self) -> 'HilPosition':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = HilPosition(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
