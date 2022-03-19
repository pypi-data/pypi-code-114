from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Refsig:
	"""Refsig commands group definition. 17 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("refsig", core, parent)

	@property
	def ansTx(self):
		"""ansTx commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ansTx'):
			from .AnsTx import AnsTx
			self._ansTx = AnsTx(self._core, self._cmd_group)
		return self._ansTx

	@property
	def drs(self):
		"""drs commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_drs'):
			from .Drs import Drs
			self._drs = Drs(self._core, self._cmd_group)
		return self._drs

	@property
	def srs(self):
		"""srs commands group. 14 Sub-classes, 0 commands."""
		if not hasattr(self, '_srs'):
			from .Srs import Srs
			self._srs = Srs(self._core, self._cmd_group)
		return self._srs

	def clone(self) -> 'Refsig':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Refsig(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
