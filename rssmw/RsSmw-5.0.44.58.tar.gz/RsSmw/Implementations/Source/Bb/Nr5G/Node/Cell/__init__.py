from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cell:
	"""Cell commands group definition. 129 total commands, 24 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cell", core, parent)
		
		self._cmd_group.multi_repcap_types = "CellNull,Cell"

	@property
	def afState(self):
		"""afState commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_afState'):
			from .AfState import AfState
			self._afState = AfState(self._core, self._cmd_group)
		return self._afState

	@property
	def cardeply(self):
		"""cardeply commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cardeply'):
			from .Cardeply import Cardeply
			self._cardeply = Cardeply(self._core, self._cmd_group)
		return self._cardeply

	@property
	def cbw(self):
		"""cbw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cbw'):
			from .Cbw import Cbw
			self._cbw = Cbw(self._core, self._cmd_group)
		return self._cbw

	@property
	def cellId(self):
		"""cellId commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cellId'):
			from .CellId import CellId
			self._cellId = CellId(self._core, self._cmd_group)
		return self._cellId

	@property
	def cif(self):
		"""cif commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cif'):
			from .Cif import Cif
			self._cif = Cif(self._core, self._cmd_group)
		return self._cif

	@property
	def cifPresent(self):
		"""cifPresent commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cifPresent'):
			from .CifPresent import CifPresent
			self._cifPresent = CifPresent(self._core, self._cmd_group)
		return self._cifPresent

	@property
	def dfreq(self):
		"""dfreq commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dfreq'):
			from .Dfreq import Dfreq
			self._dfreq = Dfreq(self._core, self._cmd_group)
		return self._dfreq

	@property
	def dumRes(self):
		"""dumRes commands group. 12 Sub-classes, 0 commands."""
		if not hasattr(self, '_dumRes'):
			from .DumRes import DumRes
			self._dumRes = DumRes(self._core, self._cmd_group)
		return self._dumRes

	@property
	def lte(self):
		"""lte commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_lte'):
			from .Lte import Lte
			self._lte = Lte(self._core, self._cmd_group)
		return self._lte

	@property
	def mapped(self):
		"""mapped commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mapped'):
			from .Mapped import Mapped
			self._mapped = Mapped(self._core, self._cmd_group)
		return self._mapped

	@property
	def n1Id(self):
		"""n1Id commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_n1Id'):
			from .N1Id import N1Id
			self._n1Id = N1Id(self._core, self._cmd_group)
		return self._n1Id

	@property
	def n2Id(self):
		"""n2Id commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_n2Id'):
			from .N2Id import N2Id
			self._n2Id = N2Id(self._core, self._cmd_group)
		return self._n2Id

	@property
	def nsspbch(self):
		"""nsspbch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nsspbch'):
			from .Nsspbch import Nsspbch
			self._nsspbch = Nsspbch(self._core, self._cmd_group)
		return self._nsspbch

	@property
	def offset(self):
		"""offset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_offset'):
			from .Offset import Offset
			self._offset = Offset(self._core, self._cmd_group)
		return self._offset

	@property
	def pcFreq(self):
		"""pcFreq commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pcFreq'):
			from .PcFreq import PcFreq
			self._pcFreq = PcFreq(self._core, self._cmd_group)
		return self._pcFreq

	@property
	def prs(self):
		"""prs commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_prs'):
			from .Prs import Prs
			self._prs = Prs(self._core, self._cmd_group)
		return self._prs

	@property
	def rpow(self):
		"""rpow commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rpow'):
			from .Rpow import Rpow
			self._rpow = Rpow(self._core, self._cmd_group)
		return self._rpow

	@property
	def schby(self):
		"""schby commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_schby'):
			from .Schby import Schby
			self._schby = Schby(self._core, self._cmd_group)
		return self._schby

	@property
	def shSpec(self):
		"""shSpec commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_shSpec'):
			from .ShSpec import ShSpec
			self._shSpec = ShSpec(self._core, self._cmd_group)
		return self._shSpec

	@property
	def sspbch(self):
		"""sspbch commands group. 16 Sub-classes, 0 commands."""
		if not hasattr(self, '_sspbch'):
			from .Sspbch import Sspbch
			self._sspbch = Sspbch(self._core, self._cmd_group)
		return self._sspbch

	@property
	def syInfo(self):
		"""syInfo commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_syInfo'):
			from .SyInfo import SyInfo
			self._syInfo = SyInfo(self._core, self._cmd_group)
		return self._syInfo

	@property
	def tapos(self):
		"""tapos commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tapos'):
			from .Tapos import Tapos
			self._tapos = Tapos(self._core, self._cmd_group)
		return self._tapos

	@property
	def tmph(self):
		"""tmph commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_tmph'):
			from .Tmph import Tmph
			self._tmph = Tmph(self._core, self._cmd_group)
		return self._tmph

	@property
	def txbw(self):
		"""txbw commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_txbw'):
			from .Txbw import Txbw
			self._txbw = Txbw(self._core, self._cmd_group)
		return self._txbw

	def clone(self) -> 'Cell':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cell(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
