from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dnav:
	"""Dnav commands group definition. 42 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dnav", core, parent)

	@property
	def ccorrection(self):
		"""ccorrection commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ccorrection'):
			from .Ccorrection import Ccorrection
			self._ccorrection = Ccorrection(self._core, self._cmd_group)
		return self._ccorrection

	@property
	def ephemeris(self):
		"""ephemeris commands group. 20 Sub-classes, 0 commands."""
		if not hasattr(self, '_ephemeris'):
			from .Ephemeris import Ephemeris
			self._ephemeris = Ephemeris(self._core, self._cmd_group)
		return self._ephemeris

	def clone(self) -> 'Dnav':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dnav(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
