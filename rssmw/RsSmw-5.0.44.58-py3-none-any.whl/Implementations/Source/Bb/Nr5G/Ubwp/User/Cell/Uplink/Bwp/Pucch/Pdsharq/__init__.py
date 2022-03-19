from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pdsharq:
	"""Pdsharq commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pdsharq", core, parent)

	@property
	def ntmEntry(self):
		"""ntmEntry commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ntmEntry'):
			from .NtmEntry import NtmEntry
			self._ntmEntry = NtmEntry(self._core, self._cmd_group)
		return self._ntmEntry

	@property
	def tmiValue(self):
		"""tmiValue commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tmiValue'):
			from .TmiValue import TmiValue
			self._tmiValue = TmiValue(self._core, self._cmd_group)
		return self._tmiValue

	def clone(self) -> 'Pdsharq':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pdsharq(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
