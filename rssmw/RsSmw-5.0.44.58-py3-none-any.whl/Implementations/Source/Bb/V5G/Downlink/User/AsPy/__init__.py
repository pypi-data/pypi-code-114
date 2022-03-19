from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AsPy:
	"""AsPy commands group definition. 51 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("asPy", core, parent)

	@property
	def apply(self):
		"""apply commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_apply'):
			from .Apply import Apply
			self._apply = Apply(self._core, self._cmd_group)
		return self._apply

	@property
	def arbLen(self):
		"""arbLen commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_arbLen'):
			from .ArbLen import ArbLen
			self._arbLen = ArbLen(self._core, self._cmd_group)
		return self._arbLen

	@property
	def asLength(self):
		"""asLength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_asLength'):
			from .AsLength import AsLength
			self._asLength = AsLength(self._core, self._cmd_group)
		return self._asLength

	@property
	def downlink(self):
		"""downlink commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_downlink'):
			from .Downlink import Downlink
			self._downlink = Downlink(self._core, self._cmd_group)
		return self._downlink

	@property
	def uplink(self):
		"""uplink commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_uplink'):
			from .Uplink import Uplink
			self._uplink = Uplink(self._core, self._cmd_group)
		return self._uplink

	def clone(self) -> 'AsPy':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AsPy(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
