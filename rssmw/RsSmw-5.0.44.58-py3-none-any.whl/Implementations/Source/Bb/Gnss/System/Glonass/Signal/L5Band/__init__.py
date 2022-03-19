from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class L5Band:
	"""L5Band commands group definition. 1 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("l5Band", core, parent)

	@property
	def l3Cdma(self):
		"""l3Cdma commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_l3Cdma'):
			from .L3Cdma import L3Cdma
			self._l3Cdma = L3Cdma(self._core, self._cmd_group)
		return self._l3Cdma

	def clone(self) -> 'L5Band':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = L5Band(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
