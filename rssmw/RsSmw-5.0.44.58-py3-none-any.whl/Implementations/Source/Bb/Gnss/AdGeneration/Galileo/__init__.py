from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Galileo:
	"""Galileo commands group definition. 16 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("galileo", core, parent)

	@property
	def coordinates(self):
		"""coordinates commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_coordinates'):
			from .Coordinates import Coordinates
			self._coordinates = Coordinates(self._core, self._cmd_group)
		return self._coordinates

	@property
	def location(self):
		"""location commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_location'):
			from .Location import Location
			self._location = Location(self._core, self._cmd_group)
		return self._location

	@property
	def svid(self):
		"""svid commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_svid'):
			from .Svid import Svid
			self._svid = Svid(self._core, self._cmd_group)
		return self._svid

	@property
	def synchronize(self):
		"""synchronize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_synchronize'):
			from .Synchronize import Synchronize
			self._synchronize = Synchronize(self._core, self._cmd_group)
		return self._synchronize

	@property
	def toaData(self):
		"""toaData commands group. 2 Sub-classes, 5 commands."""
		if not hasattr(self, '_toaData'):
			from .ToaData import ToaData
			self._toaData = ToaData(self._core, self._cmd_group)
		return self._toaData

	def clone(self) -> 'Galileo':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Galileo(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
