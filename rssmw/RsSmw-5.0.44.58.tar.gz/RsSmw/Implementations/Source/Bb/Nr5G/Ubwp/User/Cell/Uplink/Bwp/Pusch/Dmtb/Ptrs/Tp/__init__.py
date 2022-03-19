from ..............Internal.Core import Core
from ..............Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tp:
	"""Tp commands group definition. 8 total commands, 8 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tp", core, parent)

	@property
	def rb0(self):
		"""rb0 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rb0'):
			from .Rb0 import Rb0
			self._rb0 = Rb0(self._core, self._cmd_group)
		return self._rb0

	@property
	def rb1(self):
		"""rb1 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rb1'):
			from .Rb1 import Rb1
			self._rb1 = Rb1(self._core, self._cmd_group)
		return self._rb1

	@property
	def rb2(self):
		"""rb2 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rb2'):
			from .Rb2 import Rb2
			self._rb2 = Rb2(self._core, self._cmd_group)
		return self._rb2

	@property
	def rb3(self):
		"""rb3 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rb3'):
			from .Rb3 import Rb3
			self._rb3 = Rb3(self._core, self._cmd_group)
		return self._rb3

	@property
	def rb4(self):
		"""rb4 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rb4'):
			from .Rb4 import Rb4
			self._rb4 = Rb4(self._core, self._cmd_group)
		return self._rb4

	@property
	def scid(self):
		"""scid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scid'):
			from .Scid import Scid
			self._scid = Scid(self._core, self._cmd_group)
		return self._scid

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def tmDensity(self):
		"""tmDensity commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tmDensity'):
			from .TmDensity import TmDensity
			self._tmDensity = TmDensity(self._core, self._cmd_group)
		return self._tmDensity

	def clone(self) -> 'Tp':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tp(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
