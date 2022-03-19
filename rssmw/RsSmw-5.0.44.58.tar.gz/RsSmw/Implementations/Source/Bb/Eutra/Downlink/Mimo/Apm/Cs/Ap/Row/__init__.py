from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal.RepeatedCapability import RepeatedCapability
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Row:
	"""Row commands group definition. 2 total commands, 2 Subgroups, 0 group commands
	Repeated Capability: Row, default value after init: Row.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("row", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_row_get', 'repcap_row_set', repcap.Row.Nr1)

	def repcap_row_set(self, row: repcap.Row) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Row.Default
		Default value after init: Row.Nr1"""
		self._cmd_group.set_repcap_enum_value(row)

	def repcap_row_get(self) -> repcap.Row:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def imaginary(self):
		"""imaginary commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_imaginary'):
			from .Imaginary import Imaginary
			self._imaginary = Imaginary(self._core, self._cmd_group)
		return self._imaginary

	@property
	def real(self):
		"""real commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_real'):
			from .Real import Real
			self._real = Real(self._core, self._cmd_group)
		return self._real

	def clone(self) -> 'Row':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Row(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
