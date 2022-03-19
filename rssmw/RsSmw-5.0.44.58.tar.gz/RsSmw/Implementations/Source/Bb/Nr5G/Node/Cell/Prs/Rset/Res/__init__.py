from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal.RepeatedCapability import RepeatedCapability
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Res:
	"""Res commands group definition. 10 total commands, 7 Subgroups, 0 group commands
	Repeated Capability: ResourceNull, default value after init: ResourceNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("res", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_resourceNull_get', 'repcap_resourceNull_set', repcap.ResourceNull.Nr0)

	def repcap_resourceNull_set(self, resourceNull: repcap.ResourceNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to ResourceNull.Default
		Default value after init: ResourceNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(resourceNull)

	def repcap_resourceNull_get(self) -> repcap.ResourceNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def apMap(self):
		"""apMap commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_apMap'):
			from .ApMap import ApMap
			self._apMap = ApMap(self._core, self._cmd_group)
		return self._apMap

	@property
	def nsymbol(self):
		"""nsymbol commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nsymbol'):
			from .Nsymbol import Nsymbol
			self._nsymbol = Nsymbol(self._core, self._cmd_group)
		return self._nsymbol

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def reOffset(self):
		"""reOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_reOffset'):
			from .ReOffset import ReOffset
			self._reOffset = ReOffset(self._core, self._cmd_group)
		return self._reOffset

	@property
	def slOffset(self):
		"""slOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_slOffset'):
			from .SlOffset import SlOffset
			self._slOffset = SlOffset(self._core, self._cmd_group)
		return self._slOffset

	@property
	def sqid(self):
		"""sqid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sqid'):
			from .Sqid import Sqid
			self._sqid = Sqid(self._core, self._cmd_group)
		return self._sqid

	@property
	def syOffset(self):
		"""syOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_syOffset'):
			from .SyOffset import SyOffset
			self._syOffset = SyOffset(self._core, self._cmd_group)
		return self._syOffset

	def clone(self) -> 'Res':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Res(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
