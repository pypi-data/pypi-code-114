from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bb:
	"""Bb commands group definition. 5 total commands, 3 Subgroups, 0 group commands
	Repeated Capability: Baseband, default value after init: Baseband.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bb", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_baseband_get', 'repcap_baseband_set', repcap.Baseband.Nr1)

	def repcap_baseband_set(self, baseband: repcap.Baseband) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Baseband.Default
		Default value after init: Baseband.Nr1"""
		self._cmd_group.set_repcap_enum_value(baseband)

	def repcap_baseband_get(self) -> repcap.Baseband:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def aoTime(self):
		"""aoTime commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_aoTime'):
			from .AoTime import AoTime
			self._aoTime = AoTime(self._core, self._cmd_group)
		return self._aoTime

	@property
	def hoTime(self):
		"""hoTime commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_hoTime'):
			from .HoTime import HoTime
			self._hoTime = HoTime(self._core, self._cmd_group)
		return self._hoTime

	@property
	def sequence(self):
		"""sequence commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sequence'):
			from .Sequence import Sequence
			self._sequence = Sequence(self._core, self._cmd_group)
		return self._sequence

	def clone(self) -> 'Bb':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Bb(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
