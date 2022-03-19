from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Harq:
	"""Harq commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("harq", core, parent)

	@property
	def off0(self):
		"""off0 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_off0'):
			from .Off0 import Off0
			self._off0 = Off0(self._core, self._cmd_group)
		return self._off0

	@property
	def off1(self):
		"""off1 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_off1'):
			from .Off1 import Off1
			self._off1 = Off1(self._core, self._cmd_group)
		return self._off1

	@property
	def off2(self):
		"""off2 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_off2'):
			from .Off2 import Off2
			self._off2 = Off2(self._core, self._cmd_group)
		return self._off2

	def clone(self) -> 'Harq':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Harq(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
