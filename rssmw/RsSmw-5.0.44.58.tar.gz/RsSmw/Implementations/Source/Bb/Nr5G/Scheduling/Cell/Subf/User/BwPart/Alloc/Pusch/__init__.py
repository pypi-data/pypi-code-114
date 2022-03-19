from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pusch:
	"""Pusch commands group definition. 45 total commands, 14 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pusch", core, parent)

	@property
	def bmaid(self):
		"""bmaid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bmaid'):
			from .Bmaid import Bmaid
			self._bmaid = Bmaid(self._core, self._cmd_group)
		return self._bmaid

	@property
	def dmr(self):
		"""dmr commands group. 1 Sub-classes, 1 commands."""
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
	def fhOi(self):
		"""fhOi commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fhOi'):
			from .FhOi import FhOi
			self._fhOi = FhOi(self._core, self._cmd_group)
		return self._fhOi

	@property
	def fhop(self):
		"""fhop commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fhop'):
			from .Fhop import Fhop
			self._fhop = Fhop(self._core, self._cmd_group)
		return self._fhop

	@property
	def hprNumber(self):
		"""hprNumber commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hprNumber'):
			from .HprNumber import HprNumber
			self._hprNumber = HprNumber(self._core, self._cmd_group)
		return self._hprNumber

	@property
	def int(self):
		"""int commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_int'):
			from .Int import Int
			self._int = Int(self._core, self._cmd_group)
		return self._int

	@property
	def nint(self):
		"""nint commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nint'):
			from .Nint import Nint
			self._nint = Nint(self._core, self._cmd_group)
		return self._nint

	@property
	def ptrs(self):
		"""ptrs commands group. 9 Sub-classes, 0 commands."""
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
	def sint(self):
		"""sint commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sint'):
			from .Sint import Sint
			self._sint = Sint(self._core, self._cmd_group)
		return self._sint

	@property
	def txScheme(self):
		"""txScheme commands group. 4 Sub-classes, 0 commands."""
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

	@property
	def uci(self):
		"""uci commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_uci'):
			from .Uci import Uci
			self._uci = Uci(self._core, self._cmd_group)
		return self._uci

	def clone(self) -> 'Pusch':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pusch(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
