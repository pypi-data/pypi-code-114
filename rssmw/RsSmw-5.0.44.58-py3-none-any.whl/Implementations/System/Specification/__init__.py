from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Specification:
	"""Specification commands group definition. 5 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("specification", core, parent)

	@property
	def identification(self):
		"""identification commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_identification'):
			from .Identification import Identification
			self._identification = Identification(self._core, self._cmd_group)
		return self._identification

	@property
	def version(self):
		"""version commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_version'):
			from .Version import Version
			self._version = Version(self._core, self._cmd_group)
		return self._version

	def clone(self) -> 'Specification':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Specification(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
