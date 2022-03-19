from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Csi:
	"""Csi commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("csi", core, parent)

	@property
	def of10(self):
		"""of10 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_of10'):
			from .Of10 import Of10
			self._of10 = Of10(self._core, self._cmd_group)
		return self._of10

	@property
	def of11(self):
		"""of11 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_of11'):
			from .Of11 import Of11
			self._of11 = Of11(self._core, self._cmd_group)
		return self._of11

	@property
	def of20(self):
		"""of20 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_of20'):
			from .Of20 import Of20
			self._of20 = Of20(self._core, self._cmd_group)
		return self._of20

	@property
	def of21(self):
		"""of21 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_of21'):
			from .Of21 import Of21
			self._of21 = Of21(self._core, self._cmd_group)
		return self._of21

	def clone(self) -> 'Csi':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Csi(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
