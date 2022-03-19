from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DciConf:
	"""DciConf commands group definition. 31 total commands, 31 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dciConf", core, parent)

	@property
	def apnLayer(self):
		"""apnLayer commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_apnLayer'):
			from .ApnLayer import ApnLayer
			self._apnLayer = ApnLayer(self._core, self._cmd_group)
		return self._apnLayer

	@property
	def bitData(self):
		"""bitData commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bitData'):
			from .BitData import BitData
			self._bitData = BitData(self._core, self._cmd_group)
		return self._bitData

	@property
	def bmi(self):
		"""bmi commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bmi'):
			from .Bmi import Bmi
			self._bmi = Bmi(self._core, self._cmd_group)
		return self._bmi

	@property
	def bsi(self):
		"""bsi commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bsi'):
			from .Bsi import Bsi
			self._bsi = Bsi(self._core, self._cmd_group)
		return self._bsi

	@property
	def cbbRequest(self):
		"""cbbRequest commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cbbRequest'):
			from .CbbRequest import CbbRequest
			self._cbbRequest = CbbRequest(self._core, self._cmd_group)
		return self._cbbRequest

	@property
	def cbProcess(self):
		"""cbProcess commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cbProcess'):
			from .CbProcess import CbProcess
			self._cbProcess = CbProcess(self._core, self._cmd_group)
		return self._cbProcess

	@property
	def cbSymbol(self):
		"""cbSymbol commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cbSymbol'):
			from .CbSymbol import CbSymbol
			self._cbSymbol = CbSymbol(self._core, self._cmd_group)
		return self._cbSymbol

	@property
	def ctrTiming(self):
		"""ctrTiming commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ctrTiming'):
			from .CtrTiming import CtrTiming
			self._ctrTiming = CtrTiming(self._core, self._cmd_group)
		return self._ctrTiming

	@property
	def cycShift(self):
		"""cycShift commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cycShift'):
			from .CycShift import CycShift
			self._cycShift = CycShift(self._core, self._cmd_group)
		return self._cycShift

	@property
	def dlPcrs(self):
		"""dlPcrs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dlPcrs'):
			from .DlPcrs import DlPcrs
			self._dlPcrs = DlPcrs(self._core, self._cmd_group)
		return self._dlPcrs

	@property
	def fbi(self):
		"""fbi commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fbi'):
			from .Fbi import Fbi
			self._fbi = Fbi(self._core, self._cmd_group)
		return self._fbi

	@property
	def hpn(self):
		"""hpn commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hpn'):
			from .Hpn import Hpn
			self._hpn = Hpn(self._core, self._cmd_group)
		return self._hpn

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
	def nscid(self):
		"""nscid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nscid'):
			from .Nscid import Nscid
			self._nscid = Nscid(self._core, self._cmd_group)
		return self._nscid

	@property
	def occIndicator(self):
		"""occIndicator commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_occIndicator'):
			from .OccIndicator import OccIndicator
			self._occIndicator = OccIndicator(self._core, self._cmd_group)
		return self._occIndicator

	@property
	def pmi(self):
		"""pmi commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pmi'):
			from .Pmi import Pmi
			self._pmi = Pmi(self._core, self._cmd_group)
		return self._pmi

	@property
	def rba(self):
		"""rba commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rba'):
			from .Rba import Rba
			self._rba = Rba(self._core, self._cmd_group)
		return self._rba

	@property
	def remap(self):
		"""remap commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_remap'):
			from .Remap import Remap
			self._remap = Remap(self._core, self._cmd_group)
		return self._remap

	@property
	def rv(self):
		"""rv commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rv'):
			from .Rv import Rv
			self._rv = Rv(self._core, self._cmd_group)
		return self._rv

	@property
	def srsRequest(self):
		"""srsRequest commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_srsRequest'):
			from .SrsRequest import SrsRequest
			self._srsRequest = SrsRequest(self._core, self._cmd_group)
		return self._srsRequest

	@property
	def srsSymbol(self):
		"""srsSymbol commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_srsSymbol'):
			from .SrsSymbol import SrsSymbol
			self._srsSymbol = SrsSymbol(self._core, self._cmd_group)
		return self._srsSymbol

	@property
	def tpc(self):
		"""tpc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tpc'):
			from .Tpc import Tpc
			self._tpc = Tpc(self._core, self._cmd_group)
		return self._tpc

	@property
	def trtiming(self):
		"""trtiming commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_trtiming'):
			from .Trtiming import Trtiming
			self._trtiming = Trtiming(self._core, self._cmd_group)
		return self._trtiming

	@property
	def uciInd(self):
		"""uciInd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_uciInd'):
			from .UciInd import UciInd
			self._uciInd = UciInd(self._core, self._cmd_group)
		return self._uciInd

	@property
	def ufri(self):
		"""ufri commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ufri'):
			from .Ufri import Ufri
			self._ufri = Ufri(self._core, self._cmd_group)
		return self._ufri

	@property
	def ulPcrs(self):
		"""ulPcrs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ulPcrs'):
			from .UlPcrs import UlPcrs
			self._ulPcrs = UlPcrs(self._core, self._cmd_group)
		return self._ulPcrs

	@property
	def utrTiming(self):
		"""utrTiming commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_utrTiming'):
			from .UtrTiming import UtrTiming
			self._utrTiming = UtrTiming(self._core, self._cmd_group)
		return self._utrTiming

	@property
	def xpend(self):
		"""xpend commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_xpend'):
			from .Xpend import Xpend
			self._xpend = Xpend(self._core, self._cmd_group)
		return self._xpend

	@property
	def xpRange(self):
		"""xpRange commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_xpRange'):
			from .XpRange import XpRange
			self._xpRange = XpRange(self._core, self._cmd_group)
		return self._xpRange

	@property
	def xpStart(self):
		"""xpStart commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_xpStart'):
			from .XpStart import XpStart
			self._xpStart = XpStart(self._core, self._cmd_group)
		return self._xpStart

	def clone(self) -> 'DciConf':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DciConf(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
