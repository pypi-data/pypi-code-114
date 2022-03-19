from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal.RepeatedCapability import RepeatedCapability
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Item:
	"""Item commands group definition. 1 total commands, 1 Subgroups, 0 group commands
	Repeated Capability: ItemNull, default value after init: ItemNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("item", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_itemNull_get', 'repcap_itemNull_set', repcap.ItemNull.Nr0)

	def repcap_itemNull_set(self, itemNull: repcap.ItemNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to ItemNull.Default
		Default value after init: ItemNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(itemNull)

	def repcap_itemNull_get(self) -> repcap.ItemNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def pow(self):
		"""pow commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pow'):
			from .Pow import Pow
			self._pow = Pow(self._core, self._cmd_group)
		return self._pow

	def clone(self) -> 'Item':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Item(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
