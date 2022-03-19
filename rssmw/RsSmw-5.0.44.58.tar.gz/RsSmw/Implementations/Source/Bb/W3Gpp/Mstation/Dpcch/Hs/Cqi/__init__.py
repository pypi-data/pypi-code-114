from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cqi:
	"""Cqi commands group definition. 2 total commands, 2 Subgroups, 0 group commands
	Repeated Capability: ChannelQualId, default value after init: ChannelQualId.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cqi", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_channelQualId_get', 'repcap_channelQualId_set', repcap.ChannelQualId.Nr1)

	def repcap_channelQualId_set(self, channelQualId: repcap.ChannelQualId) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to ChannelQualId.Default
		Default value after init: ChannelQualId.Nr1"""
		self._cmd_group.set_repcap_enum_value(channelQualId)

	def repcap_channelQualId_get(self) -> repcap.ChannelQualId:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def plength(self):
		"""plength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_plength'):
			from .Plength import Plength
			self._plength = Plength(self._core, self._cmd_group)
		return self._plength

	@property
	def values(self):
		"""values commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_values'):
			from .Values import Values
			self._values = Values(self._core, self._cmd_group)
		return self._values

	def clone(self) -> 'Cqi':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cqi(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
