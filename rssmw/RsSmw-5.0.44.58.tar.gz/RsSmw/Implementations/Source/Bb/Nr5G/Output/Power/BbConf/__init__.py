from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BbConf:
	"""BbConf commands group definition. 1 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bbConf", core, parent)

	@property
	def row(self):
		"""row commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_row'):
			from .Row import Row
			self._row = Row(self._core, self._cmd_group)
		return self._row

	def clone(self) -> 'BbConf':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = BbConf(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
