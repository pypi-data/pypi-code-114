from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Niot:
	"""Niot commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("niot", core, parent)

	@property
	def rmax(self):
		"""rmax commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rmax'):
			from .Rmax import Rmax
			self._rmax = Rmax(self._core, self._cmd_group)
		return self._rmax

	@property
	def ssOffset(self):
		"""ssOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ssOffset'):
			from .SsOffset import SsOffset
			self._ssOffset = SsOffset(self._core, self._cmd_group)
		return self._ssOffset

	@property
	def stsFrame(self):
		"""stsFrame commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stsFrame'):
			from .StsFrame import StsFrame
			self._stsFrame = StsFrame(self._core, self._cmd_group)
		return self._stsFrame

	def clone(self) -> 'Niot':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Niot(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
