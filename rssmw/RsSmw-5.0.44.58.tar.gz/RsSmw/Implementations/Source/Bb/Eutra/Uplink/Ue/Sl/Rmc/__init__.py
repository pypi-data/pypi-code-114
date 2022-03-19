from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rmc:
	"""Rmc commands group definition. 6 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rmc", core, parent)

	@property
	def arBlocks(self):
		"""arBlocks commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_arBlocks'):
			from .ArBlocks import ArBlocks
			self._arBlocks = ArBlocks(self._core, self._cmd_group)
		return self._arBlocks

	@property
	def modulation(self):
		"""modulation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_modulation'):
			from .Modulation import Modulation
			self._modulation = Modulation(self._core, self._cmd_group)
		return self._modulation

	@property
	def paySize(self):
		"""paySize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_paySize'):
			from .PaySize import PaySize
			self._paySize = PaySize(self._core, self._cmd_group)
		return self._paySize

	@property
	def physBits(self):
		"""physBits commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_physBits'):
			from .PhysBits import PhysBits
			self._physBits = PhysBits(self._core, self._cmd_group)
		return self._physBits

	@property
	def rmc(self):
		"""rmc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rmc'):
			from .Rmc import Rmc
			self._rmc = Rmc(self._core, self._cmd_group)
		return self._rmc

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def clone(self) -> 'Rmc':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Rmc(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
