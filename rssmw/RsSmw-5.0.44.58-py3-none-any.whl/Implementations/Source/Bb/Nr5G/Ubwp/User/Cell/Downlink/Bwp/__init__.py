from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal.RepeatedCapability import RepeatedCapability
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bwp:
	"""Bwp commands group definition. 156 total commands, 19 Subgroups, 0 group commands
	Repeated Capability: BwPartNull, default value after init: BwPartNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bwp", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_bwPartNull_get', 'repcap_bwPartNull_set', repcap.BwPartNull.Nr0)

	def repcap_bwPartNull_set(self, bwPartNull: repcap.BwPartNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to BwPartNull.Default
		Default value after init: BwPartNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(bwPartNull)

	def repcap_bwPartNull_get(self) -> repcap.BwPartNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def ciLength(self):
		"""ciLength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ciLength'):
			from .CiLength import CiLength
			self._ciLength = CiLength(self._core, self._cmd_group)
		return self._ciLength

	@property
	def csi(self):
		"""csi commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_csi'):
			from .Csi import Csi
			self._csi = Csi(self._core, self._cmd_group)
		return self._csi

	@property
	def csirs(self):
		"""csirs commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_csirs'):
			from .Csirs import Csirs
			self._csirs = Csirs(self._core, self._cmd_group)
		return self._csirs

	@property
	def dfreq(self):
		"""dfreq commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dfreq'):
			from .Dfreq import Dfreq
			self._dfreq = Dfreq(self._core, self._cmd_group)
		return self._dfreq

	@property
	def indicator(self):
		"""indicator commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_indicator'):
			from .Indicator import Indicator
			self._indicator = Indicator(self._core, self._cmd_group)
		return self._indicator

	@property
	def naInd(self):
		"""naInd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_naInd'):
			from .NaInd import NaInd
			self._naInd = NaInd(self._core, self._cmd_group)
		return self._naInd

	@property
	def ncind(self):
		"""ncind commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ncind'):
			from .Ncind import Ncind
			self._ncind = Ncind(self._core, self._cmd_group)
		return self._ncind

	@property
	def pdcch(self):
		"""pdcch commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pdcch'):
			from .Pdcch import Pdcch
			self._pdcch = Pdcch(self._core, self._cmd_group)
		return self._pdcch

	@property
	def pdsch(self):
		"""pdsch commands group. 25 Sub-classes, 0 commands."""
		if not hasattr(self, '_pdsch'):
			from .Pdsch import Pdsch
			self._pdsch = Pdsch(self._core, self._cmd_group)
		return self._pdsch

	@property
	def prbOffset(self):
		"""prbOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_prbOffset'):
			from .PrbOffset import PrbOffset
			self._prbOffset = PrbOffset(self._core, self._cmd_group)
		return self._prbOffset

	@property
	def pucch(self):
		"""pucch commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pucch'):
			from .Pucch import Pucch
			self._pucch = Pucch(self._core, self._cmd_group)
		return self._pucch

	@property
	def pusch(self):
		"""pusch commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pusch'):
			from .Pusch import Pusch
			self._pusch = Pusch(self._core, self._cmd_group)
		return self._pusch

	@property
	def ratm(self):
		"""ratm commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_ratm'):
			from .Ratm import Ratm
			self._ratm = Ratm(self._core, self._cmd_group)
		return self._ratm

	@property
	def rbNumber(self):
		"""rbNumber commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rbNumber'):
			from .RbNumber import RbNumber
			self._rbNumber = RbNumber(self._core, self._cmd_group)
		return self._rbNumber

	@property
	def rbOffset(self):
		"""rbOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rbOffset'):
			from .RbOffset import RbOffset
			self._rbOffset = RbOffset(self._core, self._cmd_group)
		return self._rbOffset

	@property
	def rmc(self):
		"""rmc commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_rmc'):
			from .Rmc import Rmc
			self._rmc = Rmc(self._core, self._cmd_group)
		return self._rmc

	@property
	def rnti(self):
		"""rnti commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_rnti'):
			from .Rnti import Rnti
			self._rnti = Rnti(self._core, self._cmd_group)
		return self._rnti

	@property
	def scSpacing(self):
		"""scSpacing commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scSpacing'):
			from .ScSpacing import ScSpacing
			self._scSpacing = ScSpacing(self._core, self._cmd_group)
		return self._scSpacing

	@property
	def srs(self):
		"""srs commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_srs'):
			from .Srs import Srs
			self._srs = Srs(self._core, self._cmd_group)
		return self._srs

	def clone(self) -> 'Bwp':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Bwp(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
