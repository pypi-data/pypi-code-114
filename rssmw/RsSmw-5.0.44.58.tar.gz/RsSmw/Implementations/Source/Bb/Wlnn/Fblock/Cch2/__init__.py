from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cch2:
	"""Cch2 commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cch2", core, parent)

	@property
	def muNum(self):
		"""muNum commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_muNum'):
			from .MuNum import MuNum
			self._muNum = MuNum(self._core, self._cmd_group)
		return self._muNum

	@property
	def ruAllocation(self):
		"""ruAllocation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ruAllocation'):
			from .RuAllocation import RuAllocation
			self._ruAllocation = RuAllocation(self._core, self._cmd_group)
		return self._ruAllocation

	@property
	def ruSelection(self):
		"""ruSelection commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ruSelection'):
			from .RuSelection import RuSelection
			self._ruSelection = RuSelection(self._core, self._cmd_group)
		return self._ruSelection

	def clone(self) -> 'Cch2':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cch2(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
