from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 1 total commands, 1 Subgroups, 0 group commands
	Repeated Capability: DataNull, default value after init: DataNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_dataNull_get', 'repcap_dataNull_set', repcap.DataNull.Nr0)

	def repcap_dataNull_set(self, dataNull: repcap.DataNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to DataNull.Default
		Default value after init: DataNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(dataNull)

	def repcap_dataNull_get(self) -> repcap.DataNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def block(self):
		"""block commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_block'):
			from .Block import Block
			self._block = Block(self._core, self._cmd_group)
		return self._block

	def clone(self) -> 'Data':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Data(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
