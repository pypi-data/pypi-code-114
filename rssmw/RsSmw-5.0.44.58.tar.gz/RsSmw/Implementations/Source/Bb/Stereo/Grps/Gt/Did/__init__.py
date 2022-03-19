from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Did:
	"""Did commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("did", core, parent)

	@property
	def artHead(self):
		"""artHead commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_artHead'):
			from .ArtHead import ArtHead
			self._artHead = ArtHead(self._core, self._cmd_group)
		return self._artHead

	@property
	def compressed(self):
		"""compressed commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_compressed'):
			from .Compressed import Compressed
			self._compressed = Compressed(self._core, self._cmd_group)
		return self._compressed

	@property
	def data(self):
		"""data commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_data'):
			from .Data import Data
			self._data = Data(self._core, self._cmd_group)
		return self._data

	@property
	def dpty(self):
		"""dpty commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dpty'):
			from .Dpty import Dpty
			self._dpty = Dpty(self._core, self._cmd_group)
		return self._dpty

	@property
	def stereo(self):
		"""stereo commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stereo'):
			from .Stereo import Stereo
			self._stereo = Stereo(self._core, self._cmd_group)
		return self._stereo

	def clone(self) -> 'Did':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Did(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
