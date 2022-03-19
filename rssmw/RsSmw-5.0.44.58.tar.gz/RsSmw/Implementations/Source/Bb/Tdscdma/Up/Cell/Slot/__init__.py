from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Slot:
	"""Slot commands group definition. 47 total commands, 5 Subgroups, 0 group commands
	Repeated Capability: SlotNull, default value after init: SlotNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("slot", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_slotNull_get', 'repcap_slotNull_set', repcap.SlotNull.Nr0)

	def repcap_slotNull_set(self, slotNull: repcap.SlotNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to SlotNull.Default
		Default value after init: SlotNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(slotNull)

	def repcap_slotNull_get(self) -> repcap.SlotNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def channel(self):
		"""channel commands group. 11 Sub-classes, 0 commands."""
		if not hasattr(self, '_channel'):
			from .Channel import Channel
			self._channel = Channel(self._core, self._cmd_group)
		return self._channel

	@property
	def dconflict(self):
		"""dconflict commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dconflict'):
			from .Dconflict import Dconflict
			self._dconflict = Dconflict(self._core, self._cmd_group)
		return self._dconflict

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import Mode
			self._mode = Mode(self._core, self._cmd_group)
		return self._mode

	@property
	def prac(self):
		"""prac commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_prac'):
			from .Prac import Prac
			self._prac = Prac(self._core, self._cmd_group)
		return self._prac

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def clone(self) -> 'Slot':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Slot(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
