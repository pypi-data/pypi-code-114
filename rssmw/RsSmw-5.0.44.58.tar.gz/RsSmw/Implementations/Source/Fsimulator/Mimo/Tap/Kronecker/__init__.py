from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Kronecker:
	"""Kronecker commands group definition. 232 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("kronecker", core, parent)

	@property
	def correlation(self):
		"""correlation commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_correlation'):
			from .Correlation import Correlation
			self._correlation = Correlation(self._core, self._cmd_group)
		return self._correlation

	def clone(self) -> 'Kronecker':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Kronecker(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
