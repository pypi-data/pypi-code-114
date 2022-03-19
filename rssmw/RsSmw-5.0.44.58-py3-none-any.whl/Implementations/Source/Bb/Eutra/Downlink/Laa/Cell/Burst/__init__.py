from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Burst:
	"""Burst commands group definition. 7 total commands, 7 Subgroups, 0 group commands
	Repeated Capability: BurstNull, default value after init: BurstNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("burst", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_burstNull_get', 'repcap_burstNull_set', repcap.BurstNull.Nr0)

	def repcap_burstNull_set(self, burstNull: repcap.BurstNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to BurstNull.Default
		Default value after init: BurstNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(burstNull)

	def repcap_burstNull_get(self) -> repcap.BurstNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def c1Mode(self):
		"""c1Mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_c1Mode'):
			from .C1Mode import C1Mode
			self._c1Mode = C1Mode(self._core, self._cmd_group)
		return self._c1Mode

	@property
	def duration(self):
		"""duration commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_duration'):
			from .Duration import Duration
			self._duration = Duration(self._core, self._cmd_group)
		return self._duration

	@property
	def ensFrame(self):
		"""ensFrame commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ensFrame'):
			from .EnsFrame import EnsFrame
			self._ensFrame = EnsFrame(self._core, self._cmd_group)
		return self._ensFrame

	@property
	def epdcch(self):
		"""epdcch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_epdcch'):
			from .Epdcch import Epdcch
			self._epdcch = Epdcch(self._core, self._cmd_group)
		return self._epdcch

	@property
	def lsfSymbols(self):
		"""lsfSymbols commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lsfSymbols'):
			from .LsfSymbols import LsfSymbols
			self._lsfSymbols = LsfSymbols(self._core, self._cmd_group)
		return self._lsfSymbols

	@property
	def stsFrame(self):
		"""stsFrame commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stsFrame'):
			from .StsFrame import StsFrame
			self._stsFrame = StsFrame(self._core, self._cmd_group)
		return self._stsFrame

	@property
	def stslot(self):
		"""stslot commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stslot'):
			from .Stslot import Stslot
			self._stslot = Stslot(self._core, self._cmd_group)
		return self._stslot

	def clone(self) -> 'Burst':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Burst(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
