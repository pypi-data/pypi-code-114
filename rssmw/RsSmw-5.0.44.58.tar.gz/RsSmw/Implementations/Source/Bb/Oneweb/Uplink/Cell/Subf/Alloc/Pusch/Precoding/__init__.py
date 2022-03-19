from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Precoding:
	"""Precoding commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("precoding", core, parent)

	@property
	def cbIndex(self):
		"""cbIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cbIndex'):
			from .CbIndex import CbIndex
			self._cbIndex = CbIndex(self._core, self._cmd_group)
		return self._cbIndex

	@property
	def napUsed(self):
		"""napUsed commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_napUsed'):
			from .NapUsed import NapUsed
			self._napUsed = NapUsed(self._core, self._cmd_group)
		return self._napUsed

	@property
	def noLayers(self):
		"""noLayers commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_noLayers'):
			from .NoLayers import NoLayers
			self._noLayers = NoLayers(self._core, self._cmd_group)
		return self._noLayers

	@property
	def scheme(self):
		"""scheme commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scheme'):
			from .Scheme import Scheme
			self._scheme = Scheme(self._core, self._cmd_group)
		return self._scheme

	def clone(self) -> 'Precoding':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Precoding(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
