from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pts:
	"""Pts commands group definition. 6 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pts", core, parent)

	@property
	def distance(self):
		"""distance commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_distance'):
			from .Distance import Distance
			self._distance = Distance(self._core, self._cmd_group)
		return self._distance

	@property
	def pcorrection(self):
		"""pcorrection commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pcorrection'):
			from .Pcorrection import Pcorrection
			self._pcorrection = Pcorrection(self._core, self._cmd_group)
		return self._pcorrection

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def pstep(self):
		"""pstep commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pstep'):
			from .Pstep import Pstep
			self._pstep = Pstep(self._core, self._cmd_group)
		return self._pstep

	@property
	def repetition(self):
		"""repetition commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_repetition'):
			from .Repetition import Repetition
			self._repetition = Repetition(self._core, self._cmd_group)
		return self._repetition

	@property
	def start(self):
		"""start commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_start'):
			from .Start import Start
			self._start = Start(self._core, self._cmd_group)
		return self._start

	def clone(self) -> 'Pts':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pts(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
