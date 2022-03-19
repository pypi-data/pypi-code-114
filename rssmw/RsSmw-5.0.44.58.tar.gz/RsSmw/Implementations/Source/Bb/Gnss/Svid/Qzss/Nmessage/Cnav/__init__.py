from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cnav:
	"""Cnav commands group definition. 64 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cnav", core, parent)

	@property
	def ccorrection(self):
		"""ccorrection commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_ccorrection'):
			from .Ccorrection import Ccorrection
			self._ccorrection = Ccorrection(self._core, self._cmd_group)
		return self._ccorrection

	@property
	def ephemeris(self):
		"""ephemeris commands group. 30 Sub-classes, 0 commands."""
		if not hasattr(self, '_ephemeris'):
			from .Ephemeris import Ephemeris
			self._ephemeris = Ephemeris(self._core, self._cmd_group)
		return self._ephemeris

	def clone(self) -> 'Cnav':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cnav(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
