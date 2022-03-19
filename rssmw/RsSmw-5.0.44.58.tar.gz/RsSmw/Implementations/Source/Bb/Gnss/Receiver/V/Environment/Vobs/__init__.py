from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Vobs:
	"""Vobs commands group definition. 7 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("vobs", core, parent)

	@property
	def file(self):
		"""file commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_file'):
			from .File import File
			self._file = File(self._core, self._cmd_group)
		return self._file

	@property
	def morientation(self):
		"""morientation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_morientation'):
			from .Morientation import Morientation
			self._morientation = Morientation(self._core, self._cmd_group)
		return self._morientation

	@property
	def pmodel(self):
		"""pmodel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pmodel'):
			from .Pmodel import Pmodel
			self._pmodel = Pmodel(self._core, self._cmd_group)
		return self._pmodel

	@property
	def predefined(self):
		"""predefined commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_predefined'):
			from .Predefined import Predefined
			self._predefined = Predefined(self._core, self._cmd_group)
		return self._predefined

	@property
	def roffset(self):
		"""roffset commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_roffset'):
			from .Roffset import Roffset
			self._roffset = Roffset(self._core, self._cmd_group)
		return self._roffset

	def clone(self) -> 'Vobs':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Vobs(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
