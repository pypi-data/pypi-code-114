from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaOffset:
	"""MaOffset commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maOffset", core, parent)

	@property
	def nmOffset(self):
		"""nmOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nmOffset'):
			from .NmOffset import NmOffset
			self._nmOffset = NmOffset(self._core, self._cmd_group)
		return self._nmOffset

	@property
	def val(self):
		"""val commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_val'):
			from .Val import Val
			self._val = Val(self._core, self._cmd_group)
		return self._val

	def clone(self) -> 'MaOffset':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MaOffset(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
