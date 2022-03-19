from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal.RepeatedCapability import RepeatedCapability
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Alloc:
	"""Alloc commands group definition. 448 total commands, 34 Subgroups, 0 group commands
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
	def agft(self):
		"""agft commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_agft'):
			from .Agft import Agft
			self._agft = Agft(self._core, self._cmd_group)
		return self._agft

	@property
	def agOffset(self):
		"""agOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_agOffset'):
			from .AgOffset import AgOffset
			self._agOffset = AgOffset(self._core, self._cmd_group)
		return self._agOffset

	@property
	def apMap(self):
		"""apMap commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_apMap'):
			from .ApMap import ApMap
			self._apMap = ApMap(self._core, self._cmd_group)
		return self._apMap

	@property
	def conflict(self):
		"""conflict commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_conflict'):
			from .Conflict import Conflict
			self._conflict = Conflict(self._core, self._cmd_group)
		return self._conflict

	@property
	def content(self):
		"""content commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_content'):
			from .Content import Content
			self._content = Content(self._core, self._cmd_group)
		return self._content

	@property
	def copyTo(self):
		"""copyTo commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_copyTo'):
			from .CopyTo import CopyTo
			self._copyTo = CopyTo(self._core, self._cmd_group)
		return self._copyTo

	@property
	def cpext(self):
		"""cpext commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cpext'):
			from .Cpext import Cpext
			self._cpext = Cpext(self._core, self._cmd_group)
		return self._cpext

	@property
	def cs(self):
		"""cs commands group. 12 Sub-classes, 0 commands."""
		if not hasattr(self, '_cs'):
			from .Cs import Cs
			self._cs = Cs(self._core, self._cmd_group)
		return self._cs

	@property
	def duration(self):
		"""duration commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_duration'):
			from .Duration import Duration
			self._duration = Duration(self._core, self._cmd_group)
		return self._duration

	@property
	def fmt(self):
		"""fmt commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fmt'):
			from .Fmt import Fmt
			self._fmt = Fmt(self._core, self._cmd_group)
		return self._fmt

	@property
	def info(self):
		"""info commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_info'):
			from .Info import Info
			self._info = Info(self._core, self._cmd_group)
		return self._info

	@property
	def mapType(self):
		"""mapType commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mapType'):
			from .MapType import MapType
			self._mapType = MapType(self._core, self._cmd_group)
		return self._mapType

	@property
	def nap(self):
		"""nap commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nap'):
			from .Nap import Nap
			self._nap = Nap(self._core, self._cmd_group)
		return self._nap

	@property
	def pdsch(self):
		"""pdsch commands group. 11 Sub-classes, 0 commands."""
		if not hasattr(self, '_pdsch'):
			from .Pdsch import Pdsch
			self._pdsch = Pdsch(self._core, self._cmd_group)
		return self._pdsch

	@property
	def period(self):
		"""period commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_period'):
			from .Period import Period
			self._period = Period(self._core, self._cmd_group)
		return self._period

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def prach(self):
		"""prach commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_prach'):
			from .Prach import Prach
			self._prach = Prach(self._core, self._cmd_group)
		return self._prach

	@property
	def pscch(self):
		"""pscch commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_pscch'):
			from .Pscch import Pscch
			self._pscch = Pscch(self._core, self._cmd_group)
		return self._pscch

	@property
	def pssch(self):
		"""pssch commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_pssch'):
			from .Pssch import Pssch
			self._pssch = Pssch(self._core, self._cmd_group)
		return self._pssch

	@property
	def pucch(self):
		"""pucch commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_pucch'):
			from .Pucch import Pucch
			self._pucch = Pucch(self._core, self._cmd_group)
		return self._pucch

	@property
	def pusch(self):
		"""pusch commands group. 14 Sub-classes, 0 commands."""
		if not hasattr(self, '_pusch'):
			from .Pusch import Pusch
			self._pusch = Pusch(self._core, self._cmd_group)
		return self._pusch

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
	def repetitions(self):
		"""repetitions commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_repetitions'):
			from .Repetitions import Repetitions
			self._repetitions = Repetitions(self._core, self._cmd_group)
		return self._repetitions

	@property
	def sci(self):
		"""sci commands group. 22 Sub-classes, 0 commands."""
		if not hasattr(self, '_sci'):
			from .Sci import Sci
			self._sci = Sci(self._core, self._cmd_group)
		return self._sci

	@property
	def seqLength(self):
		"""seqLength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_seqLength'):
			from .SeqLength import SeqLength
			self._seqLength = SeqLength(self._core, self._cmd_group)
		return self._seqLength

	@property
	def sl(self):
		"""sl commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sl'):
			from .Sl import Sl
			self._sl = Sl(self._core, self._cmd_group)
		return self._sl

	@property
	def slot(self):
		"""slot commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_slot'):
			from .Slot import Slot
			self._slot = Slot(self._core, self._cmd_group)
		return self._slot

	@property
	def sltFmt(self):
		"""sltFmt commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sltFmt'):
			from .SltFmt import SltFmt
			self._sltFmt = SltFmt(self._core, self._cmd_group)
		return self._sltFmt

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def symNumber(self):
		"""symNumber commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_symNumber'):
			from .SymNumber import SymNumber
			self._symNumber = SymNumber(self._core, self._cmd_group)
		return self._symNumber

	@property
	def symOffset(self):
		"""symOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_symOffset'):
			from .SymOffset import SymOffset
			self._symOffset = SymOffset(self._core, self._cmd_group)
		return self._symOffset

	@property
	def toffset(self):
		"""toffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_toffset'):
			from .Toffset import Toffset
			self._toffset = Toffset(self._core, self._cmd_group)
		return self._toffset

	@property
	def cw(self):
		"""cw commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_cw'):
			from .Cw import Cw
			self._cw = Cw(self._core, self._cmd_group)
		return self._cw

	def clone(self) -> 'Alloc':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Alloc(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
