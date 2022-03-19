from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Receiver:
	"""Receiver commands group definition. 4 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("receiver", core, parent)

	@property
	def bstation(self):
		"""bstation commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_bstation'):
			from .Bstation import Bstation
			self._bstation = Bstation(self._core, self._cmd_group)
		return self._bstation

	@property
	def mstation(self):
		"""mstation commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_mstation'):
			from .Mstation import Mstation
			self._mstation = Mstation(self._core, self._cmd_group)
		return self._mstation

	def clone(self) -> 'Receiver':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Receiver(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
