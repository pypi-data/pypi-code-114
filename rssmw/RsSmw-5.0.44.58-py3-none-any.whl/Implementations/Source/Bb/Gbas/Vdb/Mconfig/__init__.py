from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mconfig:
	"""Mconfig commands group definition. 101 total commands, 54 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mconfig", core, parent)

	@property
	def adb1(self):
		"""adb1 commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_adb1'):
			from .Adb1 import Adb1
			self._adb1 = Adb1(self._core, self._cmd_group)
		return self._adb1

	@property
	def adb3(self):
		"""adb3 commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_adb3'):
			from .Adb3 import Adb3
			self._adb3 = Adb3(self._core, self._cmd_group)
		return self._adb3

	@property
	def adb4(self):
		"""adb4 commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_adb4'):
			from .Adb4 import Adb4
			self._adb4 = Adb4(self._core, self._cmd_group)
		return self._adb4

	@property
	def aid(self):
		"""aid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aid'):
			from .Aid import Aid
			self._aid = Aid(self._core, self._cmd_group)
		return self._aid

	@property
	def apDesignator(self):
		"""apDesignator commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_apDesignator'):
			from .ApDesignator import ApDesignator
			self._apDesignator = ApDesignator(self._core, self._cmd_group)
		return self._apDesignator

	@property
	def atcHeight(self):
		"""atcHeight commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_atcHeight'):
			from .AtcHeight import AtcHeight
			self._atcHeight = AtcHeight(self._core, self._cmd_group)
		return self._atcHeight

	@property
	def atuSelector(self):
		"""atuSelector commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_atuSelector'):
			from .AtuSelector import AtuSelector
			self._atuSelector = AtuSelector(self._core, self._cmd_group)
		return self._atuSelector

	@property
	def cwaThreshold(self):
		"""cwaThreshold commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cwaThreshold'):
			from .CwaThreshold import CwaThreshold
			self._cwaThreshold = CwaThreshold(self._core, self._cmd_group)
		return self._cwaThreshold

	@property
	def dfLocation(self):
		"""dfLocation commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_dfLocation'):
			from .DfLocation import DfLocation
			self._dfLocation = DfLocation(self._core, self._cmd_group)
		return self._dfLocation

	@property
	def dg(self):
		"""dg commands group. 12 Sub-classes, 0 commands."""
		if not hasattr(self, '_dg'):
			from .Dg import Dg
			self._dg = Dg(self._core, self._cmd_group)
		return self._dg

	@property
	def dlOffset(self):
		"""dlOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dlOffset'):
			from .DlOffset import DlOffset
			self._dlOffset = DlOffset(self._core, self._cmd_group)
		return self._dlOffset

	@property
	def fdb(self):
		"""fdb commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_fdb'):
			from .Fdb import Fdb
			self._fdb = Fdb(self._core, self._cmd_group)
		return self._fdb

	@property
	def fdBlock(self):
		"""fdBlock commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fdBlock'):
			from .FdBlock import FdBlock
			self._fdBlock = FdBlock(self._core, self._cmd_group)
		return self._fdBlock

	@property
	def fdsState(self):
		"""fdsState commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fdsState'):
			from .FdsState import FdsState
			self._fdsState = FdsState(self._core, self._cmd_group)
		return self._fdsState

	@property
	def flaa(self):
		"""flaa commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_flaa'):
			from .Flaa import Flaa
			self._flaa = Flaa(self._core, self._cmd_group)
		return self._flaa

	@property
	def frcLink(self):
		"""frcLink commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frcLink'):
			from .FrcLink import FrcLink
			self._frcLink = FrcLink(self._core, self._cmd_group)
		return self._frcLink

	@property
	def fvaa(self):
		"""fvaa commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fvaa'):
			from .Fvaa import Fvaa
			self._fvaa = Fvaa(self._core, self._cmd_group)
		return self._fvaa

	@property
	def gcid(self):
		"""gcid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gcid'):
			from .Gcid import Gcid
			self._gcid = Gcid(self._core, self._cmd_group)
		return self._gcid

	@property
	def gpAngle(self):
		"""gpAngle commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gpAngle'):
			from .GpAngle import GpAngle
			self._gpAngle = GpAngle(self._core, self._cmd_group)
		return self._gpAngle

	@property
	def gsaDesignator(self):
		"""gsaDesignator commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gsaDesignator'):
			from .GsaDesignator import GsaDesignator
			self._gsaDesignator = GsaDesignator(self._core, self._cmd_group)
		return self._gsaDesignator

	@property
	def gsrReceivers(self):
		"""gsrReceivers commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gsrReceivers'):
			from .GsrReceivers import GsrReceivers
			self._gsrReceivers = GsrReceivers(self._core, self._cmd_group)
		return self._gsrReceivers

	@property
	def kcGlonass(self):
		"""kcGlonass commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_kcGlonass'):
			from .KcGlonass import KcGlonass
			self._kcGlonass = KcGlonass(self._core, self._cmd_group)
		return self._kcGlonass

	@property
	def kcGps(self):
		"""kcGps commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_kcGps'):
			from .KcGps import KcGps
			self._kcGps = KcGps(self._core, self._cmd_group)
		return self._kcGps

	@property
	def kdGlonass(self):
		"""kdGlonass commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_kdGlonass'):
			from .KdGlonass import KdGlonass
			self._kdGlonass = KdGlonass(self._core, self._cmd_group)
		return self._kdGlonass

	@property
	def kdGps(self):
		"""kdGps commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_kdGps'):
			from .KdGps import KdGps
			self._kdGps = KdGps(self._core, self._cmd_group)
		return self._kdGps

	@property
	def kpGlonass(self):
		"""kpGlonass commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_kpGlonass'):
			from .KpGlonass import KpGlonass
			self._kpGlonass = KpGlonass(self._core, self._cmd_group)
		return self._kpGlonass

	@property
	def kpGps(self):
		"""kpGps commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_kpGps'):
			from .KpGps import KpGps
			self._kpGps = KpGps(self._core, self._cmd_group)
		return self._kpGps

	@property
	def lfLocation(self):
		"""lfLocation commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_lfLocation'):
			from .LfLocation import LfLocation
			self._lfLocation = LfLocation(self._core, self._cmd_group)
		return self._lfLocation

	@property
	def lmVariation(self):
		"""lmVariation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lmVariation'):
			from .LmVariation import LmVariation
			self._lmVariation = LmVariation(self._core, self._cmd_group)
		return self._lmVariation

	@property
	def location(self):
		"""location commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_location'):
			from .Location import Location
			self._location = Location(self._core, self._cmd_group)
		return self._location

	@property
	def mt2State(self):
		"""mt2State commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mt2State'):
			from .Mt2State import Mt2State
			self._mt2State = Mt2State(self._core, self._cmd_group)
		return self._mt2State

	@property
	def mt4State(self):
		"""mt4State commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mt4State'):
			from .Mt4State import Mt4State
			self._mt4State = Mt4State(self._core, self._cmd_group)
		return self._mt4State

	@property
	def muDistance(self):
		"""muDistance commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_muDistance'):
			from .MuDistance import MuDistance
			self._muDistance = MuDistance(self._core, self._cmd_group)
		return self._muDistance

	@property
	def nfdBlocks(self):
		"""nfdBlocks commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nfdBlocks'):
			from .NfdBlocks import NfdBlocks
			self._nfdBlocks = NfdBlocks(self._core, self._cmd_group)
		return self._nfdBlocks

	@property
	def nopPoint(self):
		"""nopPoint commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nopPoint'):
			from .NopPoint import NopPoint
			self._nopPoint = NopPoint(self._core, self._cmd_group)
		return self._nopPoint

	@property
	def pservice(self):
		"""pservice commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pservice'):
			from .Pservice import Pservice
			self._pservice = Pservice(self._core, self._cmd_group)
		return self._pservice

	@property
	def rfIndex(self):
		"""rfIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rfIndex'):
			from .RfIndex import RfIndex
			self._rfIndex = RfIndex(self._core, self._cmd_group)
		return self._rfIndex

	@property
	def rletter(self):
		"""rletter commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rletter'):
			from .Rletter import Rletter
			self._rletter = Rletter(self._core, self._cmd_group)
		return self._rletter

	@property
	def rnumber(self):
		"""rnumber commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rnumber'):
			from .Rnumber import Rnumber
			self._rnumber = Rnumber(self._core, self._cmd_group)
		return self._rnumber

	@property
	def rpdf(self):
		"""rpdf commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rpdf'):
			from .Rpdf import Rpdf
			self._rpdf = Rpdf(self._core, self._cmd_group)
		return self._rpdf

	@property
	def rpdt(self):
		"""rpdt commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rpdt'):
			from .Rpdt import Rpdt
			self._rpdt = Rpdt(self._core, self._cmd_group)
		return self._rpdt

	@property
	def rpif(self):
		"""rpif commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rpif'):
			from .Rpif import Rpif
			self._rpif = Rpif(self._core, self._cmd_group)
		return self._rpif

	@property
	def rpit(self):
		"""rpit commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rpit'):
			from .Rpit import Rpit
			self._rpit = Rpit(self._core, self._cmd_group)
		return self._rpit

	@property
	def rsdSelector(self):
		"""rsdSelector commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rsdSelector'):
			from .RsdSelector import RsdSelector
			self._rsdSelector = RsdSelector(self._core, self._cmd_group)
		return self._rsdSelector

	@property
	def ruIndicator(self):
		"""ruIndicator commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ruIndicator'):
			from .RuIndicator import RuIndicator
			self._ruIndicator = RuIndicator(self._core, self._cmd_group)
		return self._ruIndicator

	@property
	def runcertainty(self):
		"""runcertainty commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_runcertainty'):
			from .Runcertainty import Runcertainty
			self._runcertainty = Runcertainty(self._core, self._cmd_group)
		return self._runcertainty

	@property
	def sgDefinition(self):
		"""sgDefinition commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_sgDefinition'):
			from .SgDefinition import SgDefinition
			self._sgDefinition = SgDefinition(self._core, self._cmd_group)
		return self._sgDefinition

	@property
	def sheight(self):
		"""sheight commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sheight'):
			from .Sheight import Sheight
			self._sheight = Sheight(self._core, self._cmd_group)
		return self._sheight

	@property
	def svid(self):
		"""svid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_svid'):
			from .Svid import Svid
			self._svid = Svid(self._core, self._cmd_group)
		return self._svid

	@property
	def sviGradient(self):
		"""sviGradient commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sviGradient'):
			from .SviGradient import SviGradient
			self._sviGradient = SviGradient(self._core, self._cmd_group)
		return self._sviGradient

	@property
	def tdsState(self):
		"""tdsState commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tdsState'):
			from .TdsState import TdsState
			self._tdsState = TdsState(self._core, self._cmd_group)
		return self._tdsState

	@property
	def tlas(self):
		"""tlas commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tlas'):
			from .Tlas import Tlas
			self._tlas = Tlas(self._core, self._cmd_group)
		return self._tlas

	@property
	def tvas(self):
		"""tvas commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tvas'):
			from .Tvas import Tvas
			self._tvas = Tvas(self._core, self._cmd_group)
		return self._tvas

	@property
	def waypoint(self):
		"""waypoint commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_waypoint'):
			from .Waypoint import Waypoint
			self._waypoint = Waypoint(self._core, self._cmd_group)
		return self._waypoint

	def clone(self) -> 'Mconfig':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mconfig(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
