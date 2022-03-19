from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tmph:
	"""Tmph commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tmph", core, parent)

	@property
	def ctOffset(self):
		"""ctOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ctOffset'):
			from .CtOffset import CtOffset
			self._ctOffset = CtOffset(self._core, self._cmd_group)
		return self._ctOffset

	@property
	def phOffset(self):
		"""phOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_phOffset'):
			from .PhOffset import PhOffset
			self._phOffset = PhOffset(self._core, self._cmd_group)
		return self._phOffset

	@property
	def sfOffset(self):
		"""sfOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sfOffset'):
			from .SfOffset import SfOffset
			self._sfOffset = SfOffset(self._core, self._cmd_group)
		return self._sfOffset

	@property
	def syfnOffset(self):
		"""syfnOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_syfnOffset'):
			from .SyfnOffset import SyfnOffset
			self._syfnOffset = SyfnOffset(self._core, self._cmd_group)
		return self._syfnOffset

	@property
	def taOffset(self):
		"""taOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_taOffset'):
			from .TaOffset import TaOffset
			self._taOffset = TaOffset(self._core, self._cmd_group)
		return self._taOffset

	def clone(self) -> 'Tmph':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tmph(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
