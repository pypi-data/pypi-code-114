from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pcrs:
	"""Pcrs commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pcrs", core, parent)

	@property
	def nid(self):
		"""nid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nid'):
			from .Nid import Nid
			self._nid = Nid(self._core, self._cmd_group)
		return self._nid

	@property
	def nidpcrs(self):
		"""nidpcrs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nidpcrs'):
			from .Nidpcrs import Nidpcrs
			self._nidpcrs = Nidpcrs(self._core, self._cmd_group)
		return self._nidpcrs

	@property
	def rpower(self):
		"""rpower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rpower'):
			from .Rpower import Rpower
			self._rpower = Rpower(self._core, self._cmd_group)
		return self._rpower

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def clone(self) -> 'Pcrs':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pcrs(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
