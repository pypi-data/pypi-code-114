from .............Internal.Core import Core
from .............Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ptrs:
	"""Ptrs commands group definition. 14 total commands, 9 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ptrs", core, parent)

	@property
	def frqDen(self):
		"""frqDen commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frqDen'):
			from .FrqDen import FrqDen
			self._frqDen = FrqDen(self._core, self._cmd_group)
		return self._frqDen

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import Mode
			self._mode = Mode(self._core, self._cmd_group)
		return self._mode

	@property
	def port(self):
		"""port commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_port'):
			from .Port import Port
			self._port = Port(self._core, self._cmd_group)
		return self._port

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def ptdmrs(self):
		"""ptdmrs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ptdmrs'):
			from .Ptdmrs import Ptdmrs
			self._ptdmrs = Ptdmrs(self._core, self._cmd_group)
		return self._ptdmrs

	@property
	def reof(self):
		"""reof commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_reof'):
			from .Reof import Reof
			self._reof = Reof(self._core, self._cmd_group)
		return self._reof

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def tmDen(self):
		"""tmDen commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tmDen'):
			from .TmDen import TmDen
			self._tmDen = TmDen(self._core, self._cmd_group)
		return self._tmDen

	@property
	def tp(self):
		"""tp commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_tp'):
			from .Tp import Tp
			self._tp = Tp(self._core, self._cmd_group)
		return self._tp

	def clone(self) -> 'Ptrs':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ptrs(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
