from .............Internal.Core import Core
from .............Internal.CommandsGroup import CommandsGroup
from .............Internal.RepeatedCapability import RepeatedCapability
from ............. import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tcv:
	"""Tcv commands group definition. 3 total commands, 3 Subgroups, 0 group commands
	Repeated Capability: TciCodepoint, default value after init: TciCodepoint.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tcv", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_tciCodepoint_get', 'repcap_tciCodepoint_set', repcap.TciCodepoint.Nr0)

	def repcap_tciCodepoint_set(self, tciCodepoint: repcap.TciCodepoint) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to TciCodepoint.Default
		Default value after init: TciCodepoint.Nr0"""
		self._cmd_group.set_repcap_enum_value(tciCodepoint)

	def repcap_tciCodepoint_get(self) -> repcap.TciCodepoint:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def id1(self):
		"""id1 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_id1'):
			from .Id1 import Id1
			self._id1 = Id1(self._core, self._cmd_group)
		return self._id1

	@property
	def id2(self):
		"""id2 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_id2'):
			from .Id2 import Id2
			self._id2 = Id2(self._core, self._cmd_group)
		return self._id2

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def clone(self) -> 'Tcv':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tcv(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
