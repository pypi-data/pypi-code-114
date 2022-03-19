from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cgroup:
	"""Cgroup commands group definition. 32 total commands, 2 Subgroups, 0 group commands
	Repeated Capability: GroupNull, default value after init: GroupNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cgroup", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_groupNull_get', 'repcap_groupNull_set', repcap.GroupNull.Nr0)

	def repcap_groupNull_set(self, groupNull: repcap.GroupNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to GroupNull.Default
		Default value after init: GroupNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(groupNull)

	def repcap_groupNull_get(self) -> repcap.GroupNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def coffset(self):
		"""coffset commands group. 13 Sub-classes, 0 commands."""
		if not hasattr(self, '_coffset'):
			from .Coffset import Coffset
			self._coffset = Coffset(self._core, self._cmd_group)
		return self._coffset

	@property
	def rconfiguration(self):
		"""rconfiguration commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rconfiguration'):
			from .Rconfiguration import Rconfiguration
			self._rconfiguration = Rconfiguration(self._core, self._cmd_group)
		return self._rconfiguration

	def clone(self) -> 'Cgroup':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cgroup(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
