from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class B:
	"""B commands group definition. 20 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("b", core, parent)

	@property
	def list1(self):
		"""list1 commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_list1'):
			from .List1 import List1
			self._list1 = List1(self._core, self._cmd_group)
		return self._list1

	@property
	def list2(self):
		"""list2 commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_list2'):
			from .List2 import List2
			self._list2 = List2(self._core, self._cmd_group)
		return self._list2

	@property
	def list3(self):
		"""list3 commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_list3'):
			from .List3 import List3
			self._list3 = List3(self._core, self._cmd_group)
		return self._list3

	@property
	def list4(self):
		"""list4 commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_list4'):
			from .List4 import List4
			self._list4 = List4(self._core, self._cmd_group)
		return self._list4

	@property
	def list5(self):
		"""list5 commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_list5'):
			from .List5 import List5
			self._list5 = List5(self._core, self._cmd_group)
		return self._list5

	def clone(self) -> 'B':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = B(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
