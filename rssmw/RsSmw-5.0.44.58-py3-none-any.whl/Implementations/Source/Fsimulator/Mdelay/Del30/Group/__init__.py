from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Group:
	"""Group commands group definition. 11 total commands, 1 Subgroups, 0 group commands
	Repeated Capability: FadingGroup, default value after init: FadingGroup.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("group", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_fadingGroup_get', 'repcap_fadingGroup_set', repcap.FadingGroup.Nr1)

	def repcap_fadingGroup_set(self, fadingGroup: repcap.FadingGroup) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to FadingGroup.Default
		Default value after init: FadingGroup.Nr1"""
		self._cmd_group.set_repcap_enum_value(fadingGroup)

	def repcap_fadingGroup_get(self) -> repcap.FadingGroup:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def path(self):
		"""path commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_path'):
			from .Path import Path
			self._path = Path(self._core, self._cmd_group)
		return self._path

	def clone(self) -> 'Group':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Group(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
