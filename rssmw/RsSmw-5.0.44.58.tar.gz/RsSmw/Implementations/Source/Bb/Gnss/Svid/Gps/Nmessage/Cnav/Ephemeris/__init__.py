from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ephemeris:
	"""Ephemeris commands group definition. 53 total commands, 32 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ephemeris", core, parent)

	@property
	def adelta(self):
		"""adelta commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_adelta'):
			from .Adelta import Adelta
			self._adelta = Adelta(self._core, self._cmd_group)
		return self._adelta

	@property
	def adot(self):
		"""adot commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_adot'):
			from .Adot import Adot
			self._adot = Adot(self._core, self._cmd_group)
		return self._adot

	@property
	def alert(self):
		"""alert commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_alert'):
			from .Alert import Alert
			self._alert = Alert(self._core, self._cmd_group)
		return self._alert

	@property
	def cic(self):
		"""cic commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_cic'):
			from .Cic import Cic
			self._cic = Cic(self._core, self._cmd_group)
		return self._cic

	@property
	def cis(self):
		"""cis commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_cis'):
			from .Cis import Cis
			self._cis = Cis(self._core, self._cmd_group)
		return self._cis

	@property
	def crc(self):
		"""crc commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_crc'):
			from .Crc import Crc
			self._crc = Crc(self._core, self._cmd_group)
		return self._crc

	@property
	def crs(self):
		"""crs commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_crs'):
			from .Crs import Crs
			self._crs = Crs(self._core, self._cmd_group)
		return self._crs

	@property
	def cuc(self):
		"""cuc commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_cuc'):
			from .Cuc import Cuc
			self._cuc = Cuc(self._core, self._cmd_group)
		return self._cuc

	@property
	def cus(self):
		"""cus commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_cus'):
			from .Cus import Cus
			self._cus = Cus(self._core, self._cmd_group)
		return self._cus

	@property
	def dndot(self):
		"""dndot commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_dndot'):
			from .Dndot import Dndot
			self._dndot = Dndot(self._core, self._cmd_group)
		return self._dndot

	@property
	def dodot(self):
		"""dodot commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_dodot'):
			from .Dodot import Dodot
			self._dodot = Dodot(self._core, self._cmd_group)
		return self._dodot

	@property
	def eccentricity(self):
		"""eccentricity commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_eccentricity'):
			from .Eccentricity import Eccentricity
			self._eccentricity = Eccentricity(self._core, self._cmd_group)
		return self._eccentricity

	@property
	def idot(self):
		"""idot commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_idot'):
			from .Idot import Idot
			self._idot = Idot(self._core, self._cmd_group)
		return self._idot

	@property
	def isFlag(self):
		"""isFlag commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_isFlag'):
			from .IsFlag import IsFlag
			self._isFlag = IsFlag(self._core, self._cmd_group)
		return self._isFlag

	@property
	def izero(self):
		"""izero commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_izero'):
			from .Izero import Izero
			self._izero = Izero(self._core, self._cmd_group)
		return self._izero

	@property
	def l1Health(self):
		"""l1Health commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_l1Health'):
			from .L1Health import L1Health
			self._l1Health = L1Health(self._core, self._cmd_group)
		return self._l1Health

	@property
	def l2Cphasing(self):
		"""l2Cphasing commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_l2Cphasing'):
			from .L2Cphasing import L2Cphasing
			self._l2Cphasing = L2Cphasing(self._core, self._cmd_group)
		return self._l2Cphasing

	@property
	def l2Health(self):
		"""l2Health commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_l2Health'):
			from .L2Health import L2Health
			self._l2Health = L2Health(self._core, self._cmd_group)
		return self._l2Health

	@property
	def l5Health(self):
		"""l5Health commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_l5Health'):
			from .L5Health import L5Health
			self._l5Health = L5Health(self._core, self._cmd_group)
		return self._l5Health

	@property
	def mzero(self):
		"""mzero commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_mzero'):
			from .Mzero import Mzero
			self._mzero = Mzero(self._core, self._cmd_group)
		return self._mzero

	@property
	def ndelta(self):
		"""ndelta commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_ndelta'):
			from .Ndelta import Ndelta
			self._ndelta = Ndelta(self._core, self._cmd_group)
		return self._ndelta

	@property
	def ned0(self):
		"""ned0 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ned0'):
			from .Ned0 import Ned0
			self._ned0 = Ned0(self._core, self._cmd_group)
		return self._ned0

	@property
	def ned1(self):
		"""ned1 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ned1'):
			from .Ned1 import Ned1
			self._ned1 = Ned1(self._core, self._cmd_group)
		return self._ned1

	@property
	def ned2(self):
		"""ned2 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ned2'):
			from .Ned2 import Ned2
			self._ned2 = Ned2(self._core, self._cmd_group)
		return self._ned2

	@property
	def odot(self):
		"""odot commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_odot'):
			from .Odot import Odot
			self._odot = Odot(self._core, self._cmd_group)
		return self._odot

	@property
	def omega(self):
		"""omega commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_omega'):
			from .Omega import Omega
			self._omega = Omega(self._core, self._cmd_group)
		return self._omega

	@property
	def ozero(self):
		"""ozero commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_ozero'):
			from .Ozero import Ozero
			self._ozero = Ozero(self._core, self._cmd_group)
		return self._ozero

	@property
	def sqra(self):
		"""sqra commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_sqra'):
			from .Sqra import Sqra
			self._sqra = Sqra(self._core, self._cmd_group)
		return self._sqra

	@property
	def toe(self):
		"""toe commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_toe'):
			from .Toe import Toe
			self._toe = Toe(self._core, self._cmd_group)
		return self._toe

	@property
	def top(self):
		"""top commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_top'):
			from .Top import Top
			self._top = Top(self._core, self._cmd_group)
		return self._top

	@property
	def ura(self):
		"""ura commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ura'):
			from .Ura import Ura
			self._ura = Ura(self._core, self._cmd_group)
		return self._ura

	@property
	def wnop(self):
		"""wnop commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_wnop'):
			from .Wnop import Wnop
			self._wnop = Wnop(self._core, self._cmd_group)
		return self._wnop

	def clone(self) -> 'Ephemeris':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ephemeris(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
