from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dc12:
	"""Dc12 commands group definition. 6 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dc12", core, parent)

	@property
	def td(self):
		"""td commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_td'):
			from .Td import Td
			self._td = Td(self._core, self._cmd_group)
		return self._td

	@property
	def tdaNum(self):
		"""tdaNum commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tdaNum'):
			from .TdaNum import TdaNum
			self._tdaNum = TdaNum(self._core, self._cmd_group)
		return self._tdaNum

	def clone(self) -> 'Dc12':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dc12(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
