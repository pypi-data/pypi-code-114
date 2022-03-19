from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Isc:
	"""Isc commands group definition. 8 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("isc", core, parent)

	@property
	def l1Ca(self):
		"""l1Ca commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_l1Ca'):
			from .L1Ca import L1Ca
			self._l1Ca = L1Ca(self._core, self._cmd_group)
		return self._l1Ca

	@property
	def l2C(self):
		"""l2C commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_l2C'):
			from .L2C import L2C
			self._l2C = L2C(self._core, self._cmd_group)
		return self._l2C

	@property
	def l5I(self):
		"""l5I commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_l5I'):
			from .L5I import L5I
			self._l5I = L5I(self._core, self._cmd_group)
		return self._l5I

	@property
	def l5Q(self):
		"""l5Q commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_l5Q'):
			from .L5Q import L5Q
			self._l5Q = L5Q(self._core, self._cmd_group)
		return self._l5Q

	def clone(self) -> 'Isc':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Isc(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
