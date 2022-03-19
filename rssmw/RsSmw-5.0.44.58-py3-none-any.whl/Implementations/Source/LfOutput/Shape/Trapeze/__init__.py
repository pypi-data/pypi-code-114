from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trapeze:
	"""Trapeze commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trapeze", core, parent)

	@property
	def fall(self):
		"""fall commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fall'):
			from .Fall import Fall
			self._fall = Fall(self._core, self._cmd_group)
		return self._fall

	@property
	def high(self):
		"""high commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_high'):
			from .High import High
			self._high = High(self._core, self._cmd_group)
		return self._high

	@property
	def period(self):
		"""period commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_period'):
			from .Period import Period
			self._period = Period(self._core, self._cmd_group)
		return self._period

	@property
	def rise(self):
		"""rise commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rise'):
			from .Rise import Rise
			self._rise = Rise(self._core, self._cmd_group)
		return self._rise

	def clone(self) -> 'Trapeze':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Trapeze(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
