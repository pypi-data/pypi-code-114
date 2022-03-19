from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sch:
	"""Sch commands group definition. 20 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sch", core, parent)

	@property
	def m11T(self):
		"""m11T commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_m11T'):
			from .M11T import M11T
			self._m11T = M11T(self._core, self._cmd_group)
		return self._m11T

	@property
	def m1T(self):
		"""m1T commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_m1T'):
			from .M1T import M1T
			self._m1T = M1T(self._core, self._cmd_group)
		return self._m1T

	@property
	def m2T(self):
		"""m2T commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_m2T'):
			from .M2T import M2T
			self._m2T = M2T(self._core, self._cmd_group)
		return self._m2T

	@property
	def m4T(self):
		"""m4T commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_m4T'):
			from .M4T import M4T
			self._m4T = M4T(self._core, self._cmd_group)
		return self._m4T

	@property
	def ts(self):
		"""ts commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ts'):
			from .Ts import Ts
			self._ts = Ts(self._core, self._cmd_group)
		return self._ts

	def clone(self) -> 'Sch':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sch(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
