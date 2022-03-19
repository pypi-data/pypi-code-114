from ..............Internal.Core import Core
from ..............Internal.CommandsGroup import CommandsGroup
from ..............Internal.RepeatedCapability import RepeatedCapability
from .............. import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Space:
	"""Space commands group definition. 2 total commands, 2 Subgroups, 0 group commands
	Repeated Capability: IndexNull, default value after init: IndexNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("space", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_indexNull_get', 'repcap_indexNull_set', repcap.IndexNull.Nr0)

	def repcap_indexNull_set(self, indexNull: repcap.IndexNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to IndexNull.Default
		Default value after init: IndexNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(indexNull)

	def repcap_indexNull_get(self) -> repcap.IndexNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def aggLevel(self):
		"""aggLevel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aggLevel'):
			from .AggLevel import AggLevel
			self._aggLevel = AggLevel(self._core, self._cmd_group)
		return self._aggLevel

	@property
	def maxCandidate(self):
		"""maxCandidate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_maxCandidate'):
			from .MaxCandidate import MaxCandidate
			self._maxCandidate = MaxCandidate(self._core, self._cmd_group)
		return self._maxCandidate

	def clone(self) -> 'Space':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Space(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
