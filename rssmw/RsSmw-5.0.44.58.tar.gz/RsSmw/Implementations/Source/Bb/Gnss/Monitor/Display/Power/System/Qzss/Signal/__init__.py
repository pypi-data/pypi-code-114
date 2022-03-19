from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Signal:
	"""Signal commands group definition. 4 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("signal", core, parent)

	@property
	def l1Band(self):
		"""l1Band commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_l1Band'):
			from .L1Band import L1Band
			self._l1Band = L1Band(self._core, self._cmd_group)
		return self._l1Band

	@property
	def l2Band(self):
		"""l2Band commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_l2Band'):
			from .L2Band import L2Band
			self._l2Band = L2Band(self._core, self._cmd_group)
		return self._l2Band

	@property
	def l5Band(self):
		"""l5Band commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_l5Band'):
			from .L5Band import L5Band
			self._l5Band = L5Band(self._core, self._cmd_group)
		return self._l5Band

	def clone(self) -> 'Signal':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Signal(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
