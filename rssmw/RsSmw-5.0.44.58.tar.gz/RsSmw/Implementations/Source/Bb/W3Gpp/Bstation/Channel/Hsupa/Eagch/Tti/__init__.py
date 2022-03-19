from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal.RepeatedCapability import RepeatedCapability
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tti:
	"""Tti commands group definition. 3 total commands, 3 Subgroups, 0 group commands
	Repeated Capability: TransmTimeIntervalNull, default value after init: TransmTimeIntervalNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tti", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_transmTimeIntervalNull_get', 'repcap_transmTimeIntervalNull_set', repcap.TransmTimeIntervalNull.Nr0)

	def repcap_transmTimeIntervalNull_set(self, transmTimeIntervalNull: repcap.TransmTimeIntervalNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to TransmTimeIntervalNull.Default
		Default value after init: TransmTimeIntervalNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(transmTimeIntervalNull)

	def repcap_transmTimeIntervalNull_get(self) -> repcap.TransmTimeIntervalNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def agScope(self):
		"""agScope commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_agScope'):
			from .AgScope import AgScope
			self._agScope = AgScope(self._core, self._cmd_group)
		return self._agScope

	@property
	def agvIndex(self):
		"""agvIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_agvIndex'):
			from .AgvIndex import AgvIndex
			self._agvIndex = AgvIndex(self._core, self._cmd_group)
		return self._agvIndex

	@property
	def ueId(self):
		"""ueId commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ueId'):
			from .UeId import UeId
			self._ueId = UeId(self._core, self._cmd_group)
		return self._ueId

	def clone(self) -> 'Tti':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tti(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
