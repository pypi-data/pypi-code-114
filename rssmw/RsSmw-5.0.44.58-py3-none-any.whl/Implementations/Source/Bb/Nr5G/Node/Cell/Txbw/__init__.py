from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Txbw:
	"""Txbw commands group definition. 22 total commands, 10 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("txbw", core, parent)

	@property
	def conflict(self):
		"""conflict commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_conflict'):
			from .Conflict import Conflict
			self._conflict = Conflict(self._core, self._cmd_group)
		return self._conflict

	@property
	def pointA(self):
		"""pointA commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pointA'):
			from .PointA import PointA
			self._pointA = PointA(self._core, self._cmd_group)
		return self._pointA

	@property
	def resolve(self):
		"""resolve commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_resolve'):
			from .Resolve import Resolve
			self._resolve = Resolve(self._core, self._cmd_group)
		return self._resolve

	@property
	def s120K(self):
		"""s120K commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_s120K'):
			from .S120K import S120K
			self._s120K = S120K(self._core, self._cmd_group)
		return self._s120K

	@property
	def s15K(self):
		"""s15K commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_s15K'):
			from .S15K import S15K
			self._s15K = S15K(self._core, self._cmd_group)
		return self._s15K

	@property
	def s240K(self):
		"""s240K commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_s240K'):
			from .S240K import S240K
			self._s240K = S240K(self._core, self._cmd_group)
		return self._s240K

	@property
	def s30K(self):
		"""s30K commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_s30K'):
			from .S30K import S30K
			self._s30K = S30K(self._core, self._cmd_group)
		return self._s30K

	@property
	def s480K(self):
		"""s480K commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_s480K'):
			from .S480K import S480K
			self._s480K = S480K(self._core, self._cmd_group)
		return self._s480K

	@property
	def s60K(self):
		"""s60K commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_s60K'):
			from .S60K import S60K
			self._s60K = S60K(self._core, self._cmd_group)
		return self._s60K

	@property
	def s960K(self):
		"""s960K commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_s960K'):
			from .S960K import S960K
			self._s960K = S960K(self._core, self._cmd_group)
		return self._s960K

	def clone(self) -> 'Txbw':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Txbw(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
