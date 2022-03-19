from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Azp:
	"""Azp commands group definition. 12 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("azp", core, parent)

	@property
	def nsets(self):
		"""nsets commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nsets'):
			from .Nsets import Nsets
			self._nsets = Nsets(self._core, self._cmd_group)
		return self._nsets

	@property
	def set(self):
		"""set commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_set'):
			from .Set import Set
			self._set = Set(self._core, self._cmd_group)
		return self._set

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def clone(self) -> 'Azp':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Azp(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
