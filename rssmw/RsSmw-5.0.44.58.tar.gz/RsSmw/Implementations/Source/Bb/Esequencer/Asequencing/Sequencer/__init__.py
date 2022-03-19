from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sequencer:
	"""Sequencer commands group definition. 12 total commands, 3 Subgroups, 0 group commands
	Repeated Capability: Sequencer, default value after init: Sequencer.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sequencer", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_sequencer_get', 'repcap_sequencer_set', repcap.Sequencer.Nr1)

	def repcap_sequencer_set(self, sequencer: repcap.Sequencer) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Sequencer.Default
		Default value after init: Sequencer.Nr1"""
		self._cmd_group.set_repcap_enum_value(sequencer)

	def repcap_sequencer_get(self) -> repcap.Sequencer:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def stream(self):
		"""stream commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_stream'):
			from .Stream import Stream
			self._stream = Stream(self._core, self._cmd_group)
		return self._stream

	@property
	def wave(self):
		"""wave commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_wave'):
			from .Wave import Wave
			self._wave = Wave(self._core, self._cmd_group)
		return self._wave

	@property
	def wlist(self):
		"""wlist commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_wlist'):
			from .Wlist import Wlist
			self._wlist = Wlist(self._core, self._cmd_group)
		return self._wlist

	def clone(self) -> 'Sequencer':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sequencer(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
