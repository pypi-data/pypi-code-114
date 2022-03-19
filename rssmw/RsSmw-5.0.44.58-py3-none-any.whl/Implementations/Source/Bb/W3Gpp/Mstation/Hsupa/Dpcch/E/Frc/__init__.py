from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frc:
	"""Frc commands group definition. 33 total commands, 17 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frc", core, parent)

	@property
	def channel(self):
		"""channel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_channel'):
			from .Channel import Channel
			self._channel = Channel(self._core, self._cmd_group)
		return self._channel

	@property
	def crate(self):
		"""crate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_crate'):
			from .Crate import Crate
			self._crate = Crate(self._core, self._cmd_group)
		return self._crate

	@property
	def data(self):
		"""data commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_data'):
			from .Data import Data
			self._data = Data(self._core, self._cmd_group)
		return self._data

	@property
	def derror(self):
		"""derror commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_derror'):
			from .Derror import Derror
			self._derror = Derror(self._core, self._cmd_group)
		return self._derror

	@property
	def dtx(self):
		"""dtx commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_dtx'):
			from .Dtx import Dtx
			self._dtx = Dtx(self._core, self._cmd_group)
		return self._dtx

	@property
	def harq(self):
		"""harq commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_harq'):
			from .Harq import Harq
			self._harq = Harq(self._core, self._cmd_group)
		return self._harq

	@property
	def hprocesses(self):
		"""hprocesses commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hprocesses'):
			from .Hprocesses import Hprocesses
			self._hprocesses = Hprocesses(self._core, self._cmd_group)
		return self._hprocesses

	@property
	def mibRate(self):
		"""mibRate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mibRate'):
			from .MibRate import MibRate
			self._mibRate = MibRate(self._core, self._cmd_group)
		return self._mibRate

	@property
	def modulation(self):
		"""modulation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_modulation'):
			from .Modulation import Modulation
			self._modulation = Modulation(self._core, self._cmd_group)
		return self._modulation

	@property
	def orate(self):
		"""orate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_orate'):
			from .Orate import Orate
			self._orate = Orate(self._core, self._cmd_group)
		return self._orate

	@property
	def paybits(self):
		"""paybits commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_paybits'):
			from .Paybits import Paybits
			self._paybits = Paybits(self._core, self._cmd_group)
		return self._paybits

	@property
	def pcCodes(self):
		"""pcCodes commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pcCodes'):
			from .PcCodes import PcCodes
			self._pcCodes = PcCodes(self._core, self._cmd_group)
		return self._pcCodes

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def tbs(self):
		"""tbs commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_tbs'):
			from .Tbs import Tbs
			self._tbs = Tbs(self._core, self._cmd_group)
		return self._tbs

	@property
	def ttiBits(self):
		"""ttiBits commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ttiBits'):
			from .TtiBits import TtiBits
			self._ttiBits = TtiBits(self._core, self._cmd_group)
		return self._ttiBits

	@property
	def ttiedch(self):
		"""ttiedch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ttiedch'):
			from .Ttiedch import Ttiedch
			self._ttiedch = Ttiedch(self._core, self._cmd_group)
		return self._ttiedch

	@property
	def ueCategory(self):
		"""ueCategory commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ueCategory'):
			from .UeCategory import UeCategory
			self._ueCategory = UeCategory(self._core, self._cmd_group)
		return self._ueCategory

	def clone(self) -> 'Frc':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Frc(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
