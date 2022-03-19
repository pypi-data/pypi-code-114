from .............Internal.Core import Core
from .............Internal.CommandsGroup import CommandsGroup
from .............Internal.RepeatedCapability import RepeatedCapability
from ............. import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Col:
	"""Col commands group definition. 4 total commands, 1 Subgroups, 0 group commands
	Repeated Capability: ColumnNull, default value after init: ColumnNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("col", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_columnNull_get', 'repcap_columnNull_set', repcap.ColumnNull.Nr0)

	def repcap_columnNull_set(self, columnNull: repcap.ColumnNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to ColumnNull.Default
		Default value after init: ColumnNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(columnNull)

	def repcap_columnNull_get(self) -> repcap.ColumnNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def row(self):
		"""row commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_row'):
			from .Row import Row
			self._row = Row(self._core, self._cmd_group)
		return self._row

	def clone(self) -> 'Col':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Col(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
