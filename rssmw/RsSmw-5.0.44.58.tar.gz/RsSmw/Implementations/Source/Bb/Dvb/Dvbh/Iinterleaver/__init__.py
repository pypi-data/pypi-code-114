from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Iinterleaver:
	"""Iinterleaver commands group definition. 4 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iinterleaver", core, parent)

	@property
	def bit(self):
		"""bit commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bit'):
			from .Bit import Bit
			self._bit = Bit(self._core, self._cmd_group)
		return self._bit

	@property
	def symbol(self):
		"""symbol commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_symbol'):
			from .Symbol import Symbol
			self._symbol = Symbol(self._core, self._cmd_group)
		return self._symbol

	def clone(self) -> 'Iinterleaver':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Iinterleaver(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
