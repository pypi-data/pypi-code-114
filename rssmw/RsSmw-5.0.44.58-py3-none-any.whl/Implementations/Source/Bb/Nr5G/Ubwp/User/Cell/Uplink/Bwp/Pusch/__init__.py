from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pusch:
	"""Pusch commands group definition. 78 total commands, 30 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pusch", core, parent)

	@property
	def accList(self):
		"""accList commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_accList'):
			from .AccList import AccList
			self._accList = AccList(self._core, self._cmd_group)
		return self._accList

	@property
	def apPresent(self):
		"""apPresent commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_apPresent'):
			from .ApPresent import ApPresent
			self._apPresent = ApPresent(self._core, self._cmd_group)
		return self._apPresent

	@property
	def bharq(self):
		"""bharq commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bharq'):
			from .Bharq import Bharq
			self._bharq = Bharq(self._core, self._cmd_group)
		return self._bharq

	@property
	def brv(self):
		"""brv commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_brv'):
			from .Brv import Brv
			self._brv = Brv(self._core, self._cmd_group)
		return self._brv

	@property
	def cbSubset(self):
		"""cbSubset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cbSubset'):
			from .CbSubset import CbSubset
			self._cbSubset = CbSubset(self._core, self._cmd_group)
		return self._cbSubset

	@property
	def dmta(self):
		"""dmta commands group. 9 Sub-classes, 0 commands."""
		if not hasattr(self, '_dmta'):
			from .Dmta import Dmta
			self._dmta = Dmta(self._core, self._cmd_group)
		return self._dmta

	@property
	def dmtb(self):
		"""dmtb commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_dmtb'):
			from .Dmtb import Dmtb
			self._dmtb = Dmtb(self._core, self._cmd_group)
		return self._dmtb

	@property
	def dsid(self):
		"""dsid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dsid'):
			from .Dsid import Dsid
			self._dsid = Dsid(self._core, self._cmd_group)
		return self._dsid

	@property
	def dsInit(self):
		"""dsInit commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dsInit'):
			from .DsInit import DsInit
			self._dsInit = DsInit(self._core, self._cmd_group)
		return self._dsInit

	@property
	def fhOffsets(self):
		"""fhOffsets commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fhOffsets'):
			from .FhOffsets import FhOffsets
			self._fhOffsets = FhOffsets(self._core, self._cmd_group)
		return self._fhOffsets

	@property
	def fhop(self):
		"""fhop commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fhop'):
			from .Fhop import Fhop
			self._fhop = Fhop(self._core, self._cmd_group)
		return self._fhop

	@property
	def fptr(self):
		"""fptr commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fptr'):
			from .Fptr import Fptr
			self._fptr = Fptr(self._core, self._cmd_group)
		return self._fptr

	@property
	def isin(self):
		"""isin commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_isin'):
			from .Isin import Isin
			self._isin = Isin(self._core, self._cmd_group)
		return self._isin

	@property
	def mcbGroups(self):
		"""mcbGroups commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcbGroups'):
			from .McbGroups import McbGroups
			self._mcbGroups = McbGroups(self._core, self._cmd_group)
		return self._mcbGroups

	@property
	def mcsTable(self):
		"""mcsTable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcsTable'):
			from .McsTable import McsTable
			self._mcsTable = McsTable(self._core, self._cmd_group)
		return self._mcsTable

	@property
	def mrank(self):
		"""mrank commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mrank'):
			from .Mrank import Mrank
			self._mrank = Mrank(self._core, self._cmd_group)
		return self._mrank

	@property
	def mttPrecoding(self):
		"""mttPrecoding commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mttPrecoding'):
			from .MttPrecoding import MttPrecoding
			self._mttPrecoding = MttPrecoding(self._core, self._cmd_group)
		return self._mttPrecoding

	@property
	def oi01(self):
		"""oi01 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_oi01'):
			from .Oi01 import Oi01
			self._oi01 = Oi01(self._core, self._cmd_group)
		return self._oi01

	@property
	def olpc(self):
		"""olpc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_olpc'):
			from .Olpc import Olpc
			self._olpc = Olpc(self._core, self._cmd_group)
		return self._olpc

	@property
	def pi01(self):
		"""pi01 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pi01'):
			from .Pi01 import Pi01
			self._pi01 = Pi01(self._core, self._cmd_group)
		return self._pi01

	@property
	def pi02(self):
		"""pi02 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pi02'):
			from .Pi02 import Pi02
			self._pi02 = Pi02(self._core, self._cmd_group)
		return self._pi02

	@property
	def ppsl(self):
		"""ppsl commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ppsl'):
			from .Ppsl import Ppsl
			self._ppsl = Ppsl(self._core, self._cmd_group)
		return self._ppsl

	@property
	def rbgSize(self):
		"""rbgSize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rbgSize'):
			from .RbgSize import RbgSize
			self._rbgSize = RbgSize(self._core, self._cmd_group)
		return self._rbgSize

	@property
	def resAlloc(self):
		"""resAlloc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_resAlloc'):
			from .ResAlloc import ResAlloc
			self._resAlloc = ResAlloc(self._core, self._cmd_group)
		return self._resAlloc

	@property
	def scrambling(self):
		"""scrambling commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_scrambling'):
			from .Scrambling import Scrambling
			self._scrambling = Scrambling(self._core, self._cmd_group)
		return self._scrambling

	@property
	def t1Gran(self):
		"""t1Gran commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_t1Gran'):
			from .T1Gran import T1Gran
			self._t1Gran = T1Gran(self._core, self._cmd_group)
		return self._t1Gran

	@property
	def tpState(self):
		"""tpState commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tpState'):
			from .TpState import TpState
			self._tpState = TpState(self._core, self._cmd_group)
		return self._tpState

	@property
	def txConfig(self):
		"""txConfig commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_txConfig'):
			from .TxConfig import TxConfig
			self._txConfig = TxConfig(self._core, self._cmd_group)
		return self._txConfig

	@property
	def uitl(self):
		"""uitl commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_uitl'):
			from .Uitl import Uitl
			self._uitl = Uitl(self._core, self._cmd_group)
		return self._uitl

	@property
	def xoverhead(self):
		"""xoverhead commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_xoverhead'):
			from .Xoverhead import Xoverhead
			self._xoverhead = Xoverhead(self._core, self._cmd_group)
		return self._xoverhead

	def clone(self) -> 'Pusch':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pusch(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
