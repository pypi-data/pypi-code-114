from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pdsch:
	"""Pdsch commands group definition. 4 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pdsch", core, parent)

	@property
	def dc02(self):
		"""dc02 commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_dc02'):
			from .Dc02 import Dc02
			self._dc02 = Dc02(self._core, self._cmd_group)
		return self._dc02

	@property
	def multi(self):
		"""multi commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_multi'):
			from .Multi import Multi
			self._multi = Multi(self._core, self._cmd_group)
		return self._multi

	@property
	def tdaNum(self):
		"""tdaNum commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tdaNum'):
			from .TdaNum import TdaNum
			self._tdaNum = TdaNum(self._core, self._cmd_group)
		return self._tdaNum

	def clone(self) -> 'Pdsch':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pdsch(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
