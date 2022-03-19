from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class User:
	"""User commands group definition. 469 total commands, 2 Subgroups, 0 group commands
	Repeated Capability: UserNull, default value after init: UserNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("user", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_userNull_get', 'repcap_userNull_set', repcap.UserNull.Nr0)

	def repcap_userNull_set(self, userNull: repcap.UserNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to UserNull.Default
		Default value after init: UserNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(userNull)

	def repcap_userNull_get(self) -> repcap.UserNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def bwPart(self):
		"""bwPart commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_bwPart'):
			from .BwPart import BwPart
			self._bwPart = BwPart(self._core, self._cmd_group)
		return self._bwPart

	@property
	def nbwParts(self):
		"""nbwParts commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nbwParts'):
			from .NbwParts import NbwParts
			self._nbwParts = NbwParts(self._core, self._cmd_group)
		return self._nbwParts

	def clone(self) -> 'User':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = User(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
