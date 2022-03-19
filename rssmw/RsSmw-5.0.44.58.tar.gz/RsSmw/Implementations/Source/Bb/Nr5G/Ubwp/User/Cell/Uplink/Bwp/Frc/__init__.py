from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frc:
	"""Frc commands group definition. 11 total commands, 11 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frc", core, parent)

	@property
	def abw(self):
		"""abw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_abw'):
			from .Abw import Abw
			self._abw = Abw(self._core, self._cmd_group)
		return self._abw

	@property
	def alrb(self):
		"""alrb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_alrb'):
			from .Alrb import Alrb
			self._alrb = Alrb(self._core, self._cmd_group)
		return self._alrb

	@property
	def bw(self):
		"""bw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bw'):
			from .Bw import Bw
			self._bw = Bw(self._core, self._cmd_group)
		return self._bw

	@property
	def mapType(self):
		"""mapType commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mapType'):
			from .MapType import MapType
			self._mapType = MapType(self._core, self._cmd_group)
		return self._mapType

	@property
	def modulation(self):
		"""modulation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_modulation'):
			from .Modulation import Modulation
			self._modulation = Modulation(self._core, self._cmd_group)
		return self._modulation

	@property
	def paSize(self):
		"""paSize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_paSize'):
			from .PaSize import PaSize
			self._paSize = PaSize(self._core, self._cmd_group)
		return self._paSize

	@property
	def ptrs(self):
		"""ptrs commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ptrs'):
			from .Ptrs import Ptrs
			self._ptrs = Ptrs(self._core, self._cmd_group)
		return self._ptrs

	@property
	def rbOffset(self):
		"""rbOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rbOffset'):
			from .RbOffset import RbOffset
			self._rbOffset = RbOffset(self._core, self._cmd_group)
		return self._rbOffset

	@property
	def scs(self):
		"""scs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scs'):
			from .Scs import Scs
			self._scs = Scs(self._core, self._cmd_group)
		return self._scs

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def typePy(self):
		"""typePy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_typePy'):
			from .TypePy import TypePy
			self._typePy = TypePy(self._core, self._cmd_group)
		return self._typePy

	def clone(self) -> 'Frc':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Frc(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
