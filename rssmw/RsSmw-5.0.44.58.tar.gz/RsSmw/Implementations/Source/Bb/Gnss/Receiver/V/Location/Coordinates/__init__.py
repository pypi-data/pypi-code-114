from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Coordinates:
	"""Coordinates commands group definition. 6 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("coordinates", core, parent)

	@property
	def decimal(self):
		"""decimal commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_decimal'):
			from .Decimal import Decimal
			self._decimal = Decimal(self._core, self._cmd_group)
		return self._decimal

	@property
	def dms(self):
		"""dms commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_dms'):
			from .Dms import Dms
			self._dms = Dms(self._core, self._cmd_group)
		return self._dms

	@property
	def formatPy(self):
		"""formatPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_formatPy'):
			from .FormatPy import FormatPy
			self._formatPy = FormatPy(self._core, self._cmd_group)
		return self._formatPy

	@property
	def rframe(self):
		"""rframe commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rframe'):
			from .Rframe import Rframe
			self._rframe = Rframe(self._core, self._cmd_group)
		return self._rframe

	def clone(self) -> 'Coordinates':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Coordinates(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
