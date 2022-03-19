from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tm:
	"""Tm commands group definition. 8 total commands, 4 Subgroups, 0 group commands
	Repeated Capability: TmConnector, default value after init: TmConnector.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tm", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_tmConnector_get', 'repcap_tmConnector_set', repcap.TmConnector.Nr1)

	def repcap_tmConnector_set(self, tmConnector: repcap.TmConnector) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to TmConnector.Default
		Default value after init: TmConnector.Nr1"""
		self._cmd_group.set_repcap_enum_value(tmConnector)

	def repcap_tmConnector_get(self) -> repcap.TmConnector:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def clock(self):
		"""clock commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_clock'):
			from .Clock import Clock
			self._clock = Clock(self._core, self._cmd_group)
		return self._clock

	@property
	def direction(self):
		"""direction commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_direction'):
			from .Direction import Direction
			self._direction = Direction(self._core, self._cmd_group)
		return self._direction

	@property
	def signal(self):
		"""signal commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_signal'):
			from .Signal import Signal
			self._signal = Signal(self._core, self._cmd_group)
		return self._signal

	@property
	def trigger(self):
		"""trigger commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_trigger'):
			from .Trigger import Trigger
			self._trigger = Trigger(self._core, self._cmd_group)
		return self._trigger

	def clone(self) -> 'Tm':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tm(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
