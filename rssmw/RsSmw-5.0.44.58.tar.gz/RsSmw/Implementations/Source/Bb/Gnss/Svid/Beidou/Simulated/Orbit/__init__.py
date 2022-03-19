from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Orbit:
	"""Orbit commands group definition. 17 total commands, 17 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("orbit", core, parent)

	@property
	def cic(self):
		"""cic commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cic'):
			from .Cic import Cic
			self._cic = Cic(self._core, self._cmd_group)
		return self._cic

	@property
	def cis(self):
		"""cis commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cis'):
			from .Cis import Cis
			self._cis = Cis(self._core, self._cmd_group)
		return self._cis

	@property
	def crc(self):
		"""crc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_crc'):
			from .Crc import Crc
			self._crc = Crc(self._core, self._cmd_group)
		return self._crc

	@property
	def crs(self):
		"""crs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_crs'):
			from .Crs import Crs
			self._crs = Crs(self._core, self._cmd_group)
		return self._crs

	@property
	def cuc(self):
		"""cuc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cuc'):
			from .Cuc import Cuc
			self._cuc = Cuc(self._core, self._cmd_group)
		return self._cuc

	@property
	def cus(self):
		"""cus commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cus'):
			from .Cus import Cus
			self._cus = Cus(self._core, self._cmd_group)
		return self._cus

	@property
	def eccentricity(self):
		"""eccentricity commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_eccentricity'):
			from .Eccentricity import Eccentricity
			self._eccentricity = Eccentricity(self._core, self._cmd_group)
		return self._eccentricity

	@property
	def idot(self):
		"""idot commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_idot'):
			from .Idot import Idot
			self._idot = Idot(self._core, self._cmd_group)
		return self._idot

	@property
	def izero(self):
		"""izero commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_izero'):
			from .Izero import Izero
			self._izero = Izero(self._core, self._cmd_group)
		return self._izero

	@property
	def mzero(self):
		"""mzero commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mzero'):
			from .Mzero import Mzero
			self._mzero = Mzero(self._core, self._cmd_group)
		return self._mzero

	@property
	def ndelta(self):
		"""ndelta commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ndelta'):
			from .Ndelta import Ndelta
			self._ndelta = Ndelta(self._core, self._cmd_group)
		return self._ndelta

	@property
	def odot(self):
		"""odot commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_odot'):
			from .Odot import Odot
			self._odot = Odot(self._core, self._cmd_group)
		return self._odot

	@property
	def omega(self):
		"""omega commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_omega'):
			from .Omega import Omega
			self._omega = Omega(self._core, self._cmd_group)
		return self._omega

	@property
	def ozero(self):
		"""ozero commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ozero'):
			from .Ozero import Ozero
			self._ozero = Ozero(self._core, self._cmd_group)
		return self._ozero

	@property
	def sqra(self):
		"""sqra commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sqra'):
			from .Sqra import Sqra
			self._sqra = Sqra(self._core, self._cmd_group)
		return self._sqra

	@property
	def toe(self):
		"""toe commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_toe'):
			from .Toe import Toe
			self._toe = Toe(self._core, self._cmd_group)
		return self._toe

	@property
	def wnoe(self):
		"""wnoe commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_wnoe'):
			from .Wnoe import Wnoe
			self._wnoe = Wnoe(self._core, self._cmd_group)
		return self._wnoe

	def clone(self) -> 'Orbit':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Orbit(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
