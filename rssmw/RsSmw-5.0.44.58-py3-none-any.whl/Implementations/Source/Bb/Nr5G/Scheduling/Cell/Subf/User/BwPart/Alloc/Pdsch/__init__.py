from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pdsch:
	"""Pdsch commands group definition. 34 total commands, 11 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pdsch", core, parent)

	@property
	def bmaid(self):
		"""bmaid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bmaid'):
			from .Bmaid import Bmaid
			self._bmaid = Bmaid(self._core, self._cmd_group)
		return self._bmaid

	@property
	def dmr(self):
		"""dmr commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dmr'):
			from .Dmr import Dmr
			self._dmr = Dmr(self._core, self._cmd_group)
		return self._dmr

	@property
	def dmrs(self):
		"""dmrs commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_dmrs'):
			from .Dmrs import Dmrs
			self._dmrs = Dmrs(self._core, self._cmd_group)
		return self._dmrs

	@property
	def ncw(self):
		"""ncw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ncw'):
			from .Ncw import Ncw
			self._ncw = Ncw(self._core, self._cmd_group)
		return self._ncw

	@property
	def patgrp(self):
		"""patgrp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_patgrp'):
			from .Patgrp import Patgrp
			self._patgrp = Patgrp(self._core, self._cmd_group)
		return self._patgrp

	@property
	def precg(self):
		"""precg commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_precg'):
			from .Precg import Precg
			self._precg = Precg(self._core, self._cmd_group)
		return self._precg

	@property
	def ptrs(self):
		"""ptrs commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_ptrs'):
			from .Ptrs import Ptrs
			self._ptrs = Ptrs(self._core, self._cmd_group)
		return self._ptrs

	@property
	def resAlloc(self):
		"""resAlloc commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_resAlloc'):
			from .ResAlloc import ResAlloc
			self._resAlloc = ResAlloc(self._core, self._cmd_group)
		return self._resAlloc

	@property
	def sbcZero(self):
		"""sbcZero commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sbcZero'):
			from .SbcZero import SbcZero
			self._sbcZero = SbcZero(self._core, self._cmd_group)
		return self._sbcZero

	@property
	def txScheme(self):
		"""txScheme commands group. 9 Sub-classes, 0 commands."""
		if not hasattr(self, '_txScheme'):
			from .TxScheme import TxScheme
			self._txScheme = TxScheme(self._core, self._cmd_group)
		return self._txScheme

	@property
	def typePy(self):
		"""typePy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_typePy'):
			from .TypePy import TypePy
			self._typePy = TypePy(self._core, self._cmd_group)
		return self._typePy

	def clone(self) -> 'Pdsch':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pdsch(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
