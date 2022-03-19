from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DciConf:
	"""DciConf commands group definition. 42 total commands, 37 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dciConf", core, parent)

	@property
	def apLayer(self):
		"""apLayer commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_apLayer'):
			from .ApLayer import ApLayer
			self._apLayer = ApLayer(self._core, self._cmd_group)
		return self._apLayer

	@property
	def bitData(self):
		"""bitData commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bitData'):
			from .BitData import BitData
			self._bitData = BitData(self._core, self._cmd_group)
		return self._bitData

	@property
	def ciField(self):
		"""ciField commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ciField'):
			from .CiField import CiField
			self._ciField = CiField(self._core, self._cmd_group)
		return self._ciField

	@property
	def cqiRequest(self):
		"""cqiRequest commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cqiRequest'):
			from .CqiRequest import CqiRequest
			self._cqiRequest = CqiRequest(self._core, self._cmd_group)
		return self._cqiRequest

	@property
	def csDmrs(self):
		"""csDmrs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_csDmrs'):
			from .CsDmrs import CsDmrs
			self._csDmrs = CsDmrs(self._core, self._cmd_group)
		return self._csDmrs

	@property
	def csiRequest(self):
		"""csiRequest commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_csiRequest'):
			from .CsiRequest import CsiRequest
			self._csiRequest = CsiRequest(self._core, self._cmd_group)
		return self._csiRequest

	@property
	def dlaIndex(self):
		"""dlaIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dlaIndex'):
			from .DlaIndex import DlaIndex
			self._dlaIndex = DlaIndex(self._core, self._cmd_group)
		return self._dlaIndex

	@property
	def dpOffset(self):
		"""dpOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dpOffset'):
			from .DpOffset import DpOffset
			self._dpOffset = DpOffset(self._core, self._cmd_group)
		return self._dpOffset

	@property
	def f1Amode(self):
		"""f1Amode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_f1Amode'):
			from .F1Amode import F1Amode
			self._f1Amode = F1Amode(self._core, self._cmd_group)
		return self._f1Amode

	@property
	def gap(self):
		"""gap commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gap'):
			from .Gap import Gap
			self._gap = Gap(self._core, self._cmd_group)
		return self._gap

	@property
	def hack(self):
		"""hack commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hack'):
			from .Hack import Hack
			self._hack = Hack(self._core, self._cmd_group)
		return self._hack

	@property
	def hpn(self):
		"""hpn commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hpn'):
			from .Hpn import Hpn
			self._hpn = Hpn(self._core, self._cmd_group)
		return self._hpn

	@property
	def laaSubframe(self):
		"""laaSubframe commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_laaSubframe'):
			from .LaaSubframe import LaaSubframe
			self._laaSubframe = LaaSubframe(self._core, self._cmd_group)
		return self._laaSubframe

	@property
	def mcsr(self):
		"""mcsr commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcsr'):
			from .Mcsr import Mcsr
			self._mcsr = Mcsr(self._core, self._cmd_group)
		return self._mcsr

	@property
	def ndi(self):
		"""ndi commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ndi'):
			from .Ndi import Ndi
			self._ndi = Ndi(self._core, self._cmd_group)
		return self._ndi

	@property
	def pdre(self):
		"""pdre commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pdre'):
			from .Pdre import Pdre
			self._pdre = Pdre(self._core, self._cmd_group)
		return self._pdre

	@property
	def pfHopping(self):
		"""pfHopping commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pfHopping'):
			from .PfHopping import PfHopping
			self._pfHopping = PfHopping(self._core, self._cmd_group)
		return self._pfHopping

	@property
	def pmi(self):
		"""pmi commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pmi'):
			from .Pmi import Pmi
			self._pmi = Pmi(self._core, self._cmd_group)
		return self._pmi

	@property
	def prach(self):
		"""prach commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_prach'):
			from .Prach import Prach
			self._prach = Prach(self._core, self._cmd_group)
		return self._prach

	@property
	def precInfo(self):
		"""precInfo commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_precInfo'):
			from .PrecInfo import PrecInfo
			self._precInfo = PrecInfo(self._core, self._cmd_group)
		return self._precInfo

	@property
	def rah(self):
		"""rah commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rah'):
			from .Rah import Rah
			self._rah = Rah(self._core, self._cmd_group)
		return self._rah

	@property
	def rahr(self):
		"""rahr commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rahr'):
			from .Rahr import Rahr
			self._rahr = Rahr(self._core, self._cmd_group)
		return self._rahr

	@property
	def raType(self):
		"""raType commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_raType'):
			from .RaType import RaType
			self._raType = RaType(self._core, self._cmd_group)
		return self._raType

	@property
	def rba(self):
		"""rba commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rba'):
			from .Rba import Rba
			self._rba = Rba(self._core, self._cmd_group)
		return self._rba

	@property
	def rv(self):
		"""rv commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rv'):
			from .Rv import Rv
			self._rv = Rv(self._core, self._cmd_group)
		return self._rv

	@property
	def sid(self):
		"""sid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sid'):
			from .Sid import Sid
			self._sid = Sid(self._core, self._cmd_group)
		return self._sid

	@property
	def srsRequest(self):
		"""srsRequest commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_srsRequest'):
			from .SrsRequest import SrsRequest
			self._srsRequest = SrsRequest(self._core, self._cmd_group)
		return self._srsRequest

	@property
	def swapFlag(self):
		"""swapFlag commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_swapFlag'):
			from .SwapFlag import SwapFlag
			self._swapFlag = SwapFlag(self._core, self._cmd_group)
		return self._swapFlag

	@property
	def tb1(self):
		"""tb1 commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_tb1'):
			from .Tb1 import Tb1
			self._tb1 = Tb1(self._core, self._cmd_group)
		return self._tb1

	@property
	def tb2(self):
		"""tb2 commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_tb2'):
			from .Tb2 import Tb2
			self._tb2 = Tb2(self._core, self._cmd_group)
		return self._tb2

	@property
	def tbsi(self):
		"""tbsi commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tbsi'):
			from .Tbsi import Tbsi
			self._tbsi = Tbsi(self._core, self._cmd_group)
		return self._tbsi

	@property
	def tpcc(self):
		"""tpcc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tpcc'):
			from .Tpcc import Tpcc
			self._tpcc = Tpcc(self._core, self._cmd_group)
		return self._tpcc

	@property
	def tpcInstr(self):
		"""tpcInstr commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tpcInstr'):
			from .TpcInstr import TpcInstr
			self._tpcInstr = TpcInstr(self._core, self._cmd_group)
		return self._tpcInstr

	@property
	def tpmi(self):
		"""tpmi commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tpmi'):
			from .Tpmi import Tpmi
			self._tpmi = Tpmi(self._core, self._cmd_group)
		return self._tpmi

	@property
	def ulDlConf(self):
		"""ulDlConf commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ulDlConf'):
			from .UlDlConf import UlDlConf
			self._ulDlConf = UlDlConf(self._core, self._cmd_group)
		return self._ulDlConf

	@property
	def ulIndex(self):
		"""ulIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ulIndex'):
			from .UlIndex import UlIndex
			self._ulIndex = UlIndex(self._core, self._cmd_group)
		return self._ulIndex

	@property
	def vrba(self):
		"""vrba commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_vrba'):
			from .Vrba import Vrba
			self._vrba = Vrba(self._core, self._cmd_group)
		return self._vrba

	def clone(self) -> 'DciConf':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DciConf(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
