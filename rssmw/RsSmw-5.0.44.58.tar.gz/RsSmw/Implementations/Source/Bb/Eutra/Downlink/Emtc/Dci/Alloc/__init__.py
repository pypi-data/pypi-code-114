from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Alloc:
	"""Alloc commands group definition. 42 total commands, 42 Subgroups, 0 group commands
	Repeated Capability: AllocationNull, default value after init: AllocationNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("alloc", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_allocationNull_get', 'repcap_allocationNull_set', repcap.AllocationNull.Nr0)

	def repcap_allocationNull_set(self, allocationNull: repcap.AllocationNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to AllocationNull.Default
		Default value after init: AllocationNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(allocationNull)

	def repcap_allocationNull_get(self) -> repcap.AllocationNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def apsi(self):
		"""apsi commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_apsi'):
			from .Apsi import Apsi
			self._apsi = Apsi(self._core, self._cmd_group)
		return self._apsi

	@property
	def bits(self):
		"""bits commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bits'):
			from .Bits import Bits
			self._bits = Bits(self._core, self._cmd_group)
		return self._bits

	@property
	def cces(self):
		"""cces commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cces'):
			from .Cces import Cces
			self._cces = Cces(self._core, self._cmd_group)
		return self._cces

	@property
	def conflict(self):
		"""conflict commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_conflict'):
			from .Conflict import Conflict
			self._conflict = Conflict(self._core, self._cmd_group)
		return self._conflict

	@property
	def csiRequest(self):
		"""csiRequest commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_csiRequest'):
			from .CsiRequest import CsiRequest
			self._csiRequest = CsiRequest(self._core, self._cmd_group)
		return self._csiRequest

	@property
	def daIndex(self):
		"""daIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_daIndex'):
			from .DaIndex import DaIndex
			self._daIndex = DaIndex(self._core, self._cmd_group)
		return self._daIndex

	@property
	def diInfo(self):
		"""diInfo commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_diInfo'):
			from .DiInfo import DiInfo
			self._diInfo = DiInfo(self._core, self._cmd_group)
		return self._diInfo

	@property
	def fmt(self):
		"""fmt commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fmt'):
			from .Fmt import Fmt
			self._fmt = Fmt(self._core, self._cmd_group)
		return self._fmt

	@property
	def harq(self):
		"""harq commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_harq'):
			from .Harq import Harq
			self._harq = Harq(self._core, self._cmd_group)
		return self._harq

	@property
	def hresOffset(self):
		"""hresOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hresOffset'):
			from .HresOffset import HresOffset
			self._hresOffset = HresOffset(self._core, self._cmd_group)
		return self._hresOffset

	@property
	def idcce(self):
		"""idcce commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_idcce'):
			from .Idcce import Idcce
			self._idcce = Idcce(self._core, self._cmd_group)
		return self._idcce

	@property
	def mcs(self):
		"""mcs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcs'):
			from .Mcs import Mcs
			self._mcs = Mcs(self._core, self._cmd_group)
		return self._mcs

	@property
	def mpdcchset(self):
		"""mpdcchset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mpdcchset'):
			from .Mpdcchset import Mpdcchset
			self._mpdcchset = Mpdcchset(self._core, self._cmd_group)
		return self._mpdcchset

	@property
	def ndcces(self):
		"""ndcces commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ndcces'):
			from .Ndcces import Ndcces
			self._ndcces = Ndcces(self._core, self._cmd_group)
		return self._ndcces

	@property
	def ndind(self):
		"""ndind commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ndind'):
			from .Ndind import Ndind
			self._ndind = Ndind(self._core, self._cmd_group)
		return self._ndind

	@property
	def nrep(self):
		"""nrep commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nrep'):
			from .Nrep import Nrep
			self._nrep = Nrep(self._core, self._cmd_group)
		return self._nrep

	@property
	def pagng(self):
		"""pagng commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pagng'):
			from .Pagng import Pagng
			self._pagng = Pagng(self._core, self._cmd_group)
		return self._pagng

	@property
	def pdcch(self):
		"""pdcch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pdcch'):
			from .Pdcch import Pdcch
			self._pdcch = Pdcch(self._core, self._cmd_group)
		return self._pdcch

	@property
	def pdsHopping(self):
		"""pdsHopping commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pdsHopping'):
			from .PdsHopping import PdsHopping
			self._pdsHopping = PdsHopping(self._core, self._cmd_group)
		return self._pdsHopping

	@property
	def pfrHopp(self):
		"""pfrHopp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pfrHopp'):
			from .PfrHopp import PfrHopp
			self._pfrHopp = PfrHopp(self._core, self._cmd_group)
		return self._pfrHopp

	@property
	def pmiConfirm(self):
		"""pmiConfirm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pmiConfirm'):
			from .PmiConfirm import PmiConfirm
			self._pmiConfirm = PmiConfirm(self._core, self._cmd_group)
		return self._pmiConfirm

	@property
	def praMask(self):
		"""praMask commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_praMask'):
			from .PraMask import PraMask
			self._praMask = PraMask(self._core, self._cmd_group)
		return self._praMask

	@property
	def praPreamble(self):
		"""praPreamble commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_praPreamble'):
			from .PraPreamble import PraPreamble
			self._praPreamble = PraPreamble(self._core, self._cmd_group)
		return self._praPreamble

	@property
	def praStart(self):
		"""praStart commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_praStart'):
			from .PraStart import PraStart
			self._praStart = PraStart(self._core, self._cmd_group)
		return self._praStart

	@property
	def rba(self):
		"""rba commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rba'):
			from .Rba import Rba
			self._rba = Rba(self._core, self._cmd_group)
		return self._rba

	@property
	def rbaf(self):
		"""rbaf commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rbaf'):
			from .Rbaf import Rbaf
			self._rbaf = Rbaf(self._core, self._cmd_group)
		return self._rbaf

	@property
	def repmpdcch(self):
		"""repmpdcch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_repmpdcch'):
			from .Repmpdcch import Repmpdcch
			self._repmpdcch = Repmpdcch(self._core, self._cmd_group)
		return self._repmpdcch

	@property
	def reppdsch(self):
		"""reppdsch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_reppdsch'):
			from .Reppdsch import Reppdsch
			self._reppdsch = Reppdsch(self._core, self._cmd_group)
		return self._reppdsch

	@property
	def rver(self):
		"""rver commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rver'):
			from .Rver import Rver
			self._rver = Rver(self._core, self._cmd_group)
		return self._rver

	@property
	def sfrNumber(self):
		"""sfrNumber commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sfrNumber'):
			from .SfrNumber import SfrNumber
			self._sfrNumber = SfrNumber(self._core, self._cmd_group)
		return self._sfrNumber

	@property
	def srsRequest(self):
		"""srsRequest commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_srsRequest'):
			from .SrsRequest import SrsRequest
			self._srsRequest = SrsRequest(self._core, self._cmd_group)
		return self._srsRequest

	@property
	def ssp(self):
		"""ssp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ssp'):
			from .Ssp import Ssp
			self._ssp = Ssp(self._core, self._cmd_group)
		return self._ssp

	@property
	def strv(self):
		"""strv commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_strv'):
			from .Strv import Strv
			self._strv = Strv(self._core, self._cmd_group)
		return self._strv

	@property
	def stsFrame(self):
		"""stsFrame commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stsFrame'):
			from .StsFrame import StsFrame
			self._stsFrame = StsFrame(self._core, self._cmd_group)
		return self._stsFrame

	@property
	def tbs(self):
		"""tbs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tbs'):
			from .Tbs import Tbs
			self._tbs = Tbs(self._core, self._cmd_group)
		return self._tbs

	@property
	def tcmd(self):
		"""tcmd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tcmd'):
			from .Tcmd import Tcmd
			self._tcmd = Tcmd(self._core, self._cmd_group)
		return self._tcmd

	@property
	def tpcPusch(self):
		"""tpcPusch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tpcPusch'):
			from .TpcPusch import TpcPusch
			self._tpcPusch = TpcPusch(self._core, self._cmd_group)
		return self._tpcPusch

	@property
	def tpmprec(self):
		"""tpmprec commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tpmprec'):
			from .Tpmprec import Tpmprec
			self._tpmprec = Tpmprec(self._core, self._cmd_group)
		return self._tpmprec

	@property
	def ueId(self):
		"""ueId commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ueId'):
			from .UeId import UeId
			self._ueId = UeId(self._core, self._cmd_group)
		return self._ueId

	@property
	def ueMode(self):
		"""ueMode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ueMode'):
			from .UeMode import UeMode
			self._ueMode = UeMode(self._core, self._cmd_group)
		return self._ueMode

	@property
	def ulIndex(self):
		"""ulIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ulIndex'):
			from .UlIndex import UlIndex
			self._ulIndex = UlIndex(self._core, self._cmd_group)
		return self._ulIndex

	@property
	def user(self):
		"""user commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_user'):
			from .User import User
			self._user = User(self._core, self._cmd_group)
		return self._user

	def clone(self) -> 'Alloc':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Alloc(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
