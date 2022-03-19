from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pdsch:
	"""Pdsch commands group definition. 70 total commands, 25 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pdsch", core, parent)

	@property
	def ag12(self):
		"""ag12 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ag12'):
			from .Ag12 import Ag12
			self._ag12 = Ag12(self._core, self._cmd_group)
		return self._ag12

	@property
	def ap12(self):
		"""ap12 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ap12'):
			from .Ap12 import Ap12
			self._ap12 = Ap12(self._core, self._cmd_group)
		return self._ap12

	@property
	def cbgf(self):
		"""cbgf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cbgf'):
			from .Cbgf import Cbgf
			self._cbgf = Cbgf(self._core, self._cmd_group)
		return self._cbgf

	@property
	def dc12(self):
		"""dc12 commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_dc12'):
			from .Dc12 import Dc12
			self._dc12 = Dc12(self._core, self._cmd_group)
		return self._dc12

	@property
	def di12(self):
		"""di12 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_di12'):
			from .Di12 import Di12
			self._di12 = Di12(self._core, self._cmd_group)
		return self._di12

	@property
	def dmta(self):
		"""dmta commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_dmta'):
			from .Dmta import Dmta
			self._dmta = Dmta(self._core, self._cmd_group)
		return self._dmta

	@property
	def dmtb(self):
		"""dmtb commands group. 7 Sub-classes, 0 commands."""
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
	def ha12(self):
		"""ha12 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ha12'):
			from .Ha12 import Ha12
			self._ha12 = Ha12(self._core, self._cmd_group)
		return self._ha12

	@property
	def maOffset(self):
		"""maOffset commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_maOffset'):
			from .MaOffset import MaOffset
			self._maOffset = MaOffset(self._core, self._cmd_group)
		return self._maOffset

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
	def mcwdci(self):
		"""mcwdci commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcwdci'):
			from .Mcwdci import Mcwdci
			self._mcwdci = Mcwdci(self._core, self._cmd_group)
		return self._mcwdci

	@property
	def pi11(self):
		"""pi11 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pi11'):
			from .Pi11 import Pi11
			self._pi11 = Pi11(self._core, self._cmd_group)
		return self._pi11

	@property
	def pi12(self):
		"""pi12 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pi12'):
			from .Pi12 import Pi12
			self._pi12 = Pi12(self._core, self._cmd_group)
		return self._pi12

	@property
	def prec(self):
		"""prec commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_prec'):
			from .Prec import Prec
			self._prec = Prec(self._core, self._cmd_group)
		return self._prec

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
	def rv12(self):
		"""rv12 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rv12'):
			from .Rv12 import Rv12
			self._rv12 = Rv12(self._core, self._cmd_group)
		return self._rv12

	@property
	def scrambling(self):
		"""scrambling commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_scrambling'):
			from .Scrambling import Scrambling
			self._scrambling = Scrambling(self._core, self._cmd_group)
		return self._scrambling

	@property
	def tci(self):
		"""tci commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_tci'):
			from .Tci import Tci
			self._tci = Tci(self._core, self._cmd_group)
		return self._tci

	@property
	def td(self):
		"""td commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_td'):
			from .Td import Td
			self._td = Td(self._core, self._cmd_group)
		return self._td

	@property
	def tdaNum(self):
		"""tdaNum commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tdaNum'):
			from .TdaNum import TdaNum
			self._tdaNum = TdaNum(self._core, self._cmd_group)
		return self._tdaNum

	@property
	def vpInter(self):
		"""vpInter commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_vpInter'):
			from .VpInter import VpInter
			self._vpInter = VpInter(self._core, self._cmd_group)
		return self._vpInter

	@property
	def xoverhead(self):
		"""xoverhead commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_xoverhead'):
			from .Xoverhead import Xoverhead
			self._xoverhead = Xoverhead(self._core, self._cmd_group)
		return self._xoverhead

	def clone(self) -> 'Pdsch':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pdsch(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
