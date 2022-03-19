from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sync:
	"""Sync commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sync", core, parent)

	@property
	def inCoverage(self):
		"""inCoverage commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_inCoverage'):
			from .InCoverage import InCoverage
			self._inCoverage = InCoverage(self._core, self._cmd_group)
		return self._inCoverage

	@property
	def offsetInd(self):
		"""offsetInd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_offsetInd'):
			from .OffsetInd import OffsetInd
			self._offsetInd = OffsetInd(self._core, self._cmd_group)
		return self._offsetInd

	@property
	def slssId(self):
		"""slssId commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_slssId'):
			from .SlssId import SlssId
			self._slssId = SlssId(self._core, self._cmd_group)
		return self._slssId

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def clone(self) -> 'Sync':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sync(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
