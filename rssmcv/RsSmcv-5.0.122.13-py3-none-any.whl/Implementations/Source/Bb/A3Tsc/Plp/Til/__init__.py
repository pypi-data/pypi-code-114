from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Til:
	"""Til commands group definition. 8 total commands, 8 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("til", core, parent)

	@property
	def blocks(self):
		"""blocks commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_blocks'):
			from .Blocks import Blocks
			self._blocks = Blocks(self._core, self._cmd_group)
		return self._blocks

	@property
	def cil(self):
		"""cil commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cil'):
			from .Cil import Cil
			self._cil = Cil(self._core, self._cmd_group)
		return self._cil

	@property
	def depth(self):
		"""depth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_depth'):
			from .Depth import Depth
			self._depth = Depth(self._core, self._cmd_group)
		return self._depth

	@property
	def extended(self):
		"""extended commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_extended'):
			from .Extended import Extended
			self._extended = Extended(self._core, self._cmd_group)
		return self._extended

	@property
	def inter(self):
		"""inter commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_inter'):
			from .Inter import Inter
			self._inter = Inter(self._core, self._cmd_group)
		return self._inter

	@property
	def maxBlocks(self):
		"""maxBlocks commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_maxBlocks'):
			from .MaxBlocks import MaxBlocks
			self._maxBlocks = MaxBlocks(self._core, self._cmd_group)
		return self._maxBlocks

	@property
	def ntiBlocks(self):
		"""ntiBlocks commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ntiBlocks'):
			from .NtiBlocks import NtiBlocks
			self._ntiBlocks = NtiBlocks(self._core, self._cmd_group)
		return self._ntiBlocks

	@property
	def til(self):
		"""til commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_til'):
			from .Til import Til
			self._til = Til(self._core, self._cmd_group)
		return self._til

	def clone(self) -> 'Til':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Til(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
