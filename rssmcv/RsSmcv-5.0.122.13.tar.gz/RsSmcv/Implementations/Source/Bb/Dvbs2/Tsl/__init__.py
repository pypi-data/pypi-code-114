from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tsl:
	"""Tsl commands group definition. 6 total commands, 1 Subgroups, 0 group commands
	Repeated Capability: TimeSlice, default value after init: TimeSlice.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tsl", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_timeSlice_get', 'repcap_timeSlice_set', repcap.TimeSlice.Nr1)

	def repcap_timeSlice_set(self, timeSlice: repcap.TimeSlice) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to TimeSlice.Default
		Default value after init: TimeSlice.Nr1"""
		self._cmd_group.set_repcap_enum_value(timeSlice)

	def repcap_timeSlice_get(self) -> repcap.TimeSlice:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def isPy(self):
		"""isPy commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_isPy'):
			from .IsPy import IsPy
			self._isPy = IsPy(self._core, self._cmd_group)
		return self._isPy

	def clone(self) -> 'Tsl':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tsl(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
