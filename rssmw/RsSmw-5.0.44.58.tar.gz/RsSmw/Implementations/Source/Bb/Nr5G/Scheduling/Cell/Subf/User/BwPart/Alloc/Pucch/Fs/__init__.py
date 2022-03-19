from .............Internal.Core import Core
from .............Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fs:
	"""Fs commands group definition. 6 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fs", core, parent)

	@property
	def cycShift(self):
		"""cycShift commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cycShift'):
			from .CycShift import CycShift
			self._cycShift = CycShift(self._core, self._cmd_group)
		return self._cycShift

	@property
	def fmt2(self):
		"""fmt2 commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fmt2'):
			from .Fmt2 import Fmt2
			self._fmt2 = Fmt2(self._core, self._cmd_group)
		return self._fmt2

	@property
	def fmt3(self):
		"""fmt3 commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fmt3'):
			from .Fmt3 import Fmt3
			self._fmt3 = Fmt3(self._core, self._cmd_group)
		return self._fmt3

	@property
	def occLength(self):
		"""occLength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_occLength'):
			from .OccLength import OccLength
			self._occLength = OccLength(self._core, self._cmd_group)
		return self._occLength

	@property
	def occIndex(self):
		"""occIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_occIndex'):
			from .OccIndex import OccIndex
			self._occIndex = OccIndex(self._core, self._cmd_group)
		return self._occIndex

	@property
	def tdocc(self):
		"""tdocc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tdocc'):
			from .Tdocc import Tdocc
			self._tdocc = Tdocc(self._core, self._cmd_group)
		return self._tdocc

	def clone(self) -> 'Fs':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Fs(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
