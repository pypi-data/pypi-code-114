from .............Internal.Core import Core
from .............Internal.CommandsGroup import CommandsGroup
from .............Internal.RepeatedCapability import RepeatedCapability
from ............. import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Set:
	"""Set commands group definition. 10 total commands, 2 Subgroups, 0 group commands
	Repeated Capability: ResourceSetNull, default value after init: ResourceSetNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("set", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_resourceSetNull_get', 'repcap_resourceSetNull_set', repcap.ResourceSetNull.Nr0)

	def repcap_resourceSetNull_set(self, resourceSetNull: repcap.ResourceSetNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to ResourceSetNull.Default
		Default value after init: ResourceSetNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(resourceSetNull)

	def repcap_resourceSetNull_get(self) -> repcap.ResourceSetNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def nresources(self):
		"""nresources commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nresources'):
			from .Nresources import Nresources
			self._nresources = Nresources(self._core, self._cmd_group)
		return self._nresources

	@property
	def res(self):
		"""res commands group. 9 Sub-classes, 0 commands."""
		if not hasattr(self, '_res'):
			from .Res import Res
			self._res = Res(self._core, self._cmd_group)
		return self._res

	def clone(self) -> 'Set':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Set(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
