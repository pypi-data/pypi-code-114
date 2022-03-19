from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Info:
	"""Info commands group definition. 17 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("info", core, parent)

	@property
	def bootstrap(self):
		"""bootstrap commands group. 7 Sub-classes, 5 commands."""
		if not hasattr(self, '_bootstrap'):
			from .Bootstrap import Bootstrap
			self._bootstrap = Bootstrap(self._core, self._cmd_group)
		return self._bootstrap

	@property
	def frame(self):
		"""frame commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frame'):
			from .Frame import Frame
			self._frame = Frame(self._core, self._cmd_group)
		return self._frame

	@property
	def lpy(self):
		"""lpy commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_lpy'):
			from .Lpy import Lpy
			self._lpy = Lpy(self._core, self._cmd_group)
		return self._lpy

	def clone(self) -> 'Info':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Info(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
