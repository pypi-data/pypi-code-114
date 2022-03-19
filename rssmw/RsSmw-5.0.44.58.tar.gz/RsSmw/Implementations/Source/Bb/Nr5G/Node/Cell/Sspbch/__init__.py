from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sspbch:
	"""Sspbch commands group definition. 38 total commands, 16 Subgroups, 0 group commands
	Repeated Capability: SsPbchNull, default value after init: SsPbchNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sspbch", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_ssPbchNull_get', 'repcap_ssPbchNull_set', repcap.SsPbchNull.Nr0)

	def repcap_ssPbchNull_set(self, ssPbchNull: repcap.SsPbchNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to SsPbchNull.Default
		Default value after init: SsPbchNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(ssPbchNull)

	def repcap_ssPbchNull_get(self) -> repcap.SsPbchNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def bsPeriodicty(self):
		"""bsPeriodicty commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bsPeriodicty'):
			from .BsPeriodicty import BsPeriodicty
			self._bsPeriodicty = BsPeriodicty(self._core, self._cmd_group)
		return self._bsPeriodicty

	@property
	def case(self):
		"""case commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_case'):
			from .Case import Case
			self._case = Case(self._core, self._cmd_group)
		return self._case

	@property
	def ccoding(self):
		"""ccoding commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_ccoding'):
			from .Ccoding import Ccoding
			self._ccoding = Ccoding(self._core, self._cmd_group)
		return self._ccoding

	@property
	def dfreq(self):
		"""dfreq commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dfreq'):
			from .Dfreq import Dfreq
			self._dfreq = Dfreq(self._core, self._cmd_group)
		return self._dfreq

	@property
	def hfrmIdx(self):
		"""hfrmIdx commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hfrmIdx'):
			from .HfrmIdx import HfrmIdx
			self._hfrmIdx = HfrmIdx(self._core, self._cmd_group)
		return self._hfrmIdx

	@property
	def lpy(self):
		"""lpy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lpy'):
			from .Lpy import Lpy
			self._lpy = Lpy(self._core, self._cmd_group)
		return self._lpy

	@property
	def mib(self):
		"""mib commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_mib'):
			from .Mib import Mib
			self._mib = Mib(self._core, self._cmd_group)
		return self._mib

	@property
	def position(self):
		"""position commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_position'):
			from .Position import Position
			self._position = Position(self._core, self._cmd_group)
		return self._position

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def pssPow(self):
		"""pssPow commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pssPow'):
			from .PssPow import PssPow
			self._pssPow = PssPow(self._core, self._cmd_group)
		return self._pssPow

	@property
	def rbOffset(self):
		"""rbOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rbOffset'):
			from .RbOffset import RbOffset
			self._rbOffset = RbOffset(self._core, self._cmd_group)
		return self._rbOffset

	@property
	def scOffset(self):
		"""scOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scOffset'):
			from .ScOffset import ScOffset
			self._scOffset = ScOffset(self._core, self._cmd_group)
		return self._scOffset

	@property
	def scSpacing(self):
		"""scSpacing commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scSpacing'):
			from .ScSpacing import ScSpacing
			self._scSpacing = ScSpacing(self._core, self._cmd_group)
		return self._scSpacing

	@property
	def sl(self):
		"""sl commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_sl'):
			from .Sl import Sl
			self._sl = Sl(self._core, self._cmd_group)
		return self._sl

	@property
	def ssspow(self):
		"""ssspow commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ssspow'):
			from .Ssspow import Ssspow
			self._ssspow = Ssspow(self._core, self._cmd_group)
		return self._ssspow

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def clone(self) -> 'Sspbch':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sspbch(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
