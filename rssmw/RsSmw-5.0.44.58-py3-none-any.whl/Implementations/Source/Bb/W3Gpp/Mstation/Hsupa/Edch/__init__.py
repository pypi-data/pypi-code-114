from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Edch:
	"""Edch commands group definition. 5 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("edch", core, parent)

	@property
	def repeat(self):
		"""repeat commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_repeat'):
			from .Repeat import Repeat
			self._repeat = Repeat(self._core, self._cmd_group)
		return self._repeat

	@property
	def row(self):
		"""row commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_row'):
			from .Row import Row
			self._row = Row(self._core, self._cmd_group)
		return self._row

	@property
	def rowCount(self):
		"""rowCount commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rowCount'):
			from .RowCount import RowCount
			self._rowCount = RowCount(self._core, self._cmd_group)
		return self._rowCount

	@property
	def ttiedch(self):
		"""ttiedch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ttiedch'):
			from .Ttiedch import Ttiedch
			self._ttiedch = Ttiedch(self._core, self._cmd_group)
		return self._ttiedch

	def clone(self) -> 'Edch':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Edch(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
