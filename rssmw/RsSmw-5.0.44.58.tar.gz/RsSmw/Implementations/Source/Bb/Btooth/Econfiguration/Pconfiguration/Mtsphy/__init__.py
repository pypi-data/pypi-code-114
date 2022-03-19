from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mtsphy:
	"""Mtsphy commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mtsphy", core, parent)

	@property
	def l1M(self):
		"""l1M commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_l1M'):
			from .L1M import L1M
			self._l1M = L1M(self._core, self._cmd_group)
		return self._l1M

	@property
	def l2M(self):
		"""l2M commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_l2M'):
			from .L2M import L2M
			self._l2M = L2M(self._core, self._cmd_group)
		return self._l2M

	@property
	def lcod(self):
		"""lcod commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lcod'):
			from .Lcod import Lcod
			self._lcod = Lcod(self._core, self._cmd_group)
		return self._lcod

	def clone(self) -> 'Mtsphy':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mtsphy(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
