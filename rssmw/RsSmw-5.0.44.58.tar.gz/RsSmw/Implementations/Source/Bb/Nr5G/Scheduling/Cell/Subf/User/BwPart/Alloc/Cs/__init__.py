from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cs:
	"""Cs commands group definition. 257 total commands, 12 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cs", core, parent)

	@property
	def aulBwp(self):
		"""aulBwp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aulBwp'):
			from .AulBwp import AulBwp
			self._aulBwp = AulBwp(self._core, self._cmd_group)
		return self._aulBwp

	@property
	def dcces(self):
		"""dcces commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_dcces'):
			from .Dcces import Dcces
			self._dcces = Dcces(self._core, self._cmd_group)
		return self._dcces

	@property
	def dci(self):
		"""dci commands group. 232 Sub-classes, 0 commands."""
		if not hasattr(self, '_dci'):
			from .Dci import Dci
			self._dci = Dci(self._core, self._cmd_group)
		return self._dci

	@property
	def dmrs(self):
		"""dmrs commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_dmrs'):
			from .Dmrs import Dmrs
			self._dmrs = Dmrs(self._core, self._cmd_group)
		return self._dmrs

	@property
	def id(self):
		"""id commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_id'):
			from .Id import Id
			self._id = Id(self._core, self._cmd_group)
		return self._id

	@property
	def il(self):
		"""il commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_il'):
			from .Il import Il
			self._il = Il(self._core, self._cmd_group)
		return self._il

	@property
	def ndci(self):
		"""ndci commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ndci'):
			from .Ndci import Ndci
			self._ndci = Ndci(self._core, self._cmd_group)
		return self._ndci

	@property
	def nsci(self):
		"""nsci commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nsci'):
			from .Nsci import Nsci
			self._nsci = Nsci(self._core, self._cmd_group)
		return self._nsci

	@property
	def preGran(self):
		"""preGran commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_preGran'):
			from .PreGran import PreGran
			self._preGran = PreGran(self._core, self._cmd_group)
		return self._preGran

	@property
	def resAlloc(self):
		"""resAlloc commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_resAlloc'):
			from .ResAlloc import ResAlloc
			self._resAlloc = ResAlloc(self._core, self._cmd_group)
		return self._resAlloc

	@property
	def tci(self):
		"""tci commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tci'):
			from .Tci import Tci
			self._tci = Tci(self._core, self._cmd_group)
		return self._tci

	@property
	def ts12(self):
		"""ts12 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ts12'):
			from .Ts12 import Ts12
			self._ts12 = Ts12(self._core, self._cmd_group)
		return self._ts12

	def clone(self) -> 'Cs':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cs(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
