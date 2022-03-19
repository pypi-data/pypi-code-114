from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Subf:
	"""Subf commands group definition. 495 total commands, 6 Subgroups, 0 group commands
	Repeated Capability: SubframeNull, default value after init: SubframeNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("subf", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_subframeNull_get', 'repcap_subframeNull_set', repcap.SubframeNull.Nr0)

	def repcap_subframeNull_set(self, subframeNull: repcap.SubframeNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to SubframeNull.Default
		Default value after init: SubframeNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(subframeNull)

	def repcap_subframeNull_get(self) -> repcap.SubframeNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def alloc(self):
		"""alloc commands group. 11 Sub-classes, 0 commands."""
		if not hasattr(self, '_alloc'):
			from .Alloc import Alloc
			self._alloc = Alloc(self._core, self._cmd_group)
		return self._alloc

	@property
	def common(self):
		"""common commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_common'):
			from .Common import Common
			self._common = Common(self._core, self._cmd_group)
		return self._common

	@property
	def nalloc(self):
		"""nalloc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nalloc'):
			from .Nalloc import Nalloc
			self._nalloc = Nalloc(self._core, self._cmd_group)
		return self._nalloc

	@property
	def nuser(self):
		"""nuser commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nuser'):
			from .Nuser import Nuser
			self._nuser = Nuser(self._core, self._cmd_group)
		return self._nuser

	@property
	def resulting(self):
		"""resulting commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_resulting'):
			from .Resulting import Resulting
			self._resulting = Resulting(self._core, self._cmd_group)
		return self._resulting

	@property
	def user(self):
		"""user commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_user'):
			from .User import User
			self._user = User(self._core, self._cmd_group)
		return self._user

	def clone(self) -> 'Subf':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Subf(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
