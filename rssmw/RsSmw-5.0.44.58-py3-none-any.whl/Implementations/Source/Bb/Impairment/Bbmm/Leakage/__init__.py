from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Leakage:
	"""Leakage commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("leakage", core, parent)

	@property
	def icomponent(self):
		"""icomponent commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_icomponent'):
			from .Icomponent import Icomponent
			self._icomponent = Icomponent(self._core, self._cmd_group)
		return self._icomponent

	@property
	def qcomponent(self):
		"""qcomponent commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_qcomponent'):
			from .Qcomponent import Qcomponent
			self._qcomponent = Qcomponent(self._core, self._cmd_group)
		return self._qcomponent

	def clone(self) -> 'Leakage':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Leakage(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
