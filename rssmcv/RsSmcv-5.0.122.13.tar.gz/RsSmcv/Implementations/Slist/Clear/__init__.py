from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Clear:
	"""Clear commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("clear", core, parent)

	@property
	def lan(self):
		"""lan commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lan'):
			from .Lan import Lan
			self._lan = Lan(self._core, self._cmd_group)
		return self._lan

	@property
	def usb(self):
		"""usb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_usb'):
			from .Usb import Usb
			self._usb = Usb(self._core, self._cmd_group)
		return self._usb

	def clone(self) -> 'Clear':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Clear(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
