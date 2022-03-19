from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sci:
	"""Sci commands group definition. 22 total commands, 22 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sci", core, parent)

	@property
	def amcsInd(self):
		"""amcsInd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_amcsInd'):
			from .AmcsInd import AmcsInd
			self._amcsInd = AmcsInd(self._core, self._cmd_group)
		return self._amcsInd

	@property
	def boind(self):
		"""boind commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_boind'):
			from .Boind import Boind
			self._boind = Boind(self._core, self._cmd_group)
		return self._boind

	@property
	def correq(self):
		"""correq commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_correq'):
			from .Correq import Correq
			self._correq = Correq(self._core, self._cmd_group)
		return self._correq

	@property
	def csiReq(self):
		"""csiReq commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_csiReq'):
			from .CsiReq import CsiReq
			self._csiReq = CsiReq(self._core, self._cmd_group)
		return self._csiReq

	@property
	def ctInd(self):
		"""ctInd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ctInd'):
			from .CtInd import CtInd
			self._ctInd = CtInd(self._core, self._cmd_group)
		return self._ctInd

	@property
	def destId(self):
		"""destId commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_destId'):
			from .DestId import DestId
			self._destId = DestId(self._core, self._cmd_group)
		return self._destId

	@property
	def dpatterns(self):
		"""dpatterns commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dpatterns'):
			from .Dpatterns import Dpatterns
			self._dpatterns = Dpatterns(self._core, self._cmd_group)
		return self._dpatterns

	@property
	def dports(self):
		"""dports commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dports'):
			from .Dports import Dports
			self._dports = Dports(self._core, self._cmd_group)
		return self._dports

	@property
	def frdRes(self):
		"""frdRes commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frdRes'):
			from .FrdRes import FrdRes
			self._frdRes = FrdRes(self._core, self._cmd_group)
		return self._frdRes

	@property
	def harfb(self):
		"""harfb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_harfb'):
			from .Harfb import Harfb
			self._harfb = Harfb(self._core, self._cmd_group)
		return self._harfb

	@property
	def harProc(self):
		"""harProc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_harProc'):
			from .HarProc import HarProc
			self._harProc = HarProc(self._core, self._cmd_group)
		return self._harProc

	@property
	def mcs(self):
		"""mcs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcs'):
			from .Mcs import Mcs
			self._mcs = Mcs(self._core, self._cmd_group)
		return self._mcs

	@property
	def ndi(self):
		"""ndi commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ndi'):
			from .Ndi import Ndi
			self._ndi = Ndi(self._core, self._cmd_group)
		return self._ndi

	@property
	def pfOverhead(self):
		"""pfOverhead commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pfOverhead'):
			from .PfOverhead import PfOverhead
			self._pfOverhead = PfOverhead(self._core, self._cmd_group)
		return self._pfOverhead

	@property
	def prty(self):
		"""prty commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_prty'):
			from .Prty import Prty
			self._prty = Prty(self._core, self._cmd_group)
		return self._prty

	@property
	def redundancy(self):
		"""redundancy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_redundancy'):
			from .Redundancy import Redundancy
			self._redundancy = Redundancy(self._core, self._cmd_group)
		return self._redundancy

	@property
	def resved(self):
		"""resved commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_resved'):
			from .Resved import Resved
			self._resved = Resved(self._core, self._cmd_group)
		return self._resved

	@property
	def rrePeriod(self):
		"""rrePeriod commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rrePeriod'):
			from .RrePeriod import RrePeriod
			self._rrePeriod = RrePeriod(self._core, self._cmd_group)
		return self._rrePeriod

	@property
	def s2Fmt(self):
		"""s2Fmt commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_s2Fmt'):
			from .S2Fmt import S2Fmt
			self._s2Fmt = S2Fmt(self._core, self._cmd_group)
		return self._s2Fmt

	@property
	def sourId(self):
		"""sourId commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sourId'):
			from .SourId import SourId
			self._sourId = SourId(self._core, self._cmd_group)
		return self._sourId

	@property
	def tidRes(self):
		"""tidRes commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tidRes'):
			from .TidRes import TidRes
			self._tidRes = TidRes(self._core, self._cmd_group)
		return self._tidRes

	@property
	def zoneId(self):
		"""zoneId commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_zoneId'):
			from .ZoneId import ZoneId
			self._zoneId = ZoneId(self._core, self._cmd_group)
		return self._zoneId

	def clone(self) -> 'Sci':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sci(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
