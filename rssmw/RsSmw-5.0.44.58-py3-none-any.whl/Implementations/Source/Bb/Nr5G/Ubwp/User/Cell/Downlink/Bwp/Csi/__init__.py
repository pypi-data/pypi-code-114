from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Csi:
	"""Csi commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("csi", core, parent)

	@property
	def lresponse(self):
		"""lresponse commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lresponse'):
			from .Lresponse import Lresponse
			self._lresponse = Lresponse(self._core, self._cmd_group)
		return self._lresponse

	@property
	def rtSize(self):
		"""rtSize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rtSize'):
			from .RtSize import RtSize
			self._rtSize = RtSize(self._core, self._cmd_group)
		return self._rtSize

	def clone(self) -> 'Csi':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Csi(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
