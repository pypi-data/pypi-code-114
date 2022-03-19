from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ephemeris:
	"""Ephemeris commands group definition. 43 total commands, 27 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ephemeris", core, parent)

	@property
	def aodo(self):
		"""aodo commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aodo'):
			from .Aodo import Aodo
			self._aodo = Aodo(self._core, self._cmd_group)
		return self._aodo

	@property
	def asFlag(self):
		"""asFlag commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_asFlag'):
			from .AsFlag import AsFlag
			self._asFlag = AsFlag(self._core, self._cmd_group)
		return self._asFlag

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
	def cltMmode(self):
		"""cltMmode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cltMmode'):
			from .CltMmode import CltMmode
			self._cltMmode = CltMmode(self._core, self._cmd_group)
		return self._cltMmode

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
	def eccentricity(self):
		"""eccentricity commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_eccentricity'):
			from .Eccentricity import Eccentricity
			self._eccentricity = Eccentricity(self._core, self._cmd_group)
		return self._eccentricity

	@property
	def fiFlag(self):
		"""fiFlag commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fiFlag'):
			from .FiFlag import FiFlag
			self._fiFlag = FiFlag(self._core, self._cmd_group)
		return self._fiFlag

	@property
	def health(self):
		"""health commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_health'):
			from .Health import Health
			self._health = Health(self._core, self._cmd_group)
		return self._health

	@property
	def idot(self):
		"""idot commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_idot'):
			from .Idot import Idot
			self._idot = Idot(self._core, self._cmd_group)
		return self._idot

	@property
	def iodc(self):
		"""iodc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_iodc'):
			from .Iodc import Iodc
			self._iodc = Iodc(self._core, self._cmd_group)
		return self._iodc

	@property
	def iode(self):
		"""iode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_iode'):
			from .Iode import Iode
			self._iode = Iode(self._core, self._cmd_group)
		return self._iode

	@property
	def izero(self):
		"""izero commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_izero'):
			from .Izero import Izero
			self._izero = Izero(self._core, self._cmd_group)
		return self._izero

	@property
	def ltpData(self):
		"""ltpData commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ltpData'):
			from .LtpData import LtpData
			self._ltpData = LtpData(self._core, self._cmd_group)
		return self._ltpData

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
	def sf1Reserved(self):
		"""sf1Reserved commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sf1Reserved'):
			from .Sf1Reserved import Sf1Reserved
			self._sf1Reserved = Sf1Reserved(self._core, self._cmd_group)
		return self._sf1Reserved

	@property
	def sqra(self):
		"""sqra commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_sqra'):
			from .Sqra import Sqra
			self._sqra = Sqra(self._core, self._cmd_group)
		return self._sqra

	@property
	def svConfig(self):
		"""svConfig commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_svConfig'):
			from .SvConfig import SvConfig
			self._svConfig = SvConfig(self._core, self._cmd_group)
		return self._svConfig

	@property
	def toe(self):
		"""toe commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_toe'):
			from .Toe import Toe
			self._toe = Toe(self._core, self._cmd_group)
		return self._toe

	@property
	def ura(self):
		"""ura commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ura'):
			from .Ura import Ura
			self._ura = Ura(self._core, self._cmd_group)
		return self._ura

	def clone(self) -> 'Ephemeris':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ephemeris(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
