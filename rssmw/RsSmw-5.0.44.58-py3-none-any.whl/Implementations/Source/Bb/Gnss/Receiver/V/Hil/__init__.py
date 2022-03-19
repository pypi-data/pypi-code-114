from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hil:
	"""Hil commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hil", core, parent)

	@property
	def itype(self):
		"""itype commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_itype'):
			from .Itype import Itype
			self._itype = Itype(self._core, self._cmd_group)
		return self._itype

	@property
	def port(self):
		"""port commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_port'):
			from .Port import Port
			self._port = Port(self._core, self._cmd_group)
		return self._port

	@property
	def slatency(self):
		"""slatency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_slatency'):
			from .Slatency import Slatency
			self._slatency = Slatency(self._core, self._cmd_group)
		return self._slatency

	def clone(self) -> 'Hil':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Hil(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
