from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dpch:
	"""Dpch commands group definition. 37 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dpch", core, parent)

	@property
	def ccoding(self):
		"""ccoding commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_ccoding'):
			from .Ccoding import Ccoding
			self._ccoding = Ccoding(self._core, self._cmd_group)
		return self._ccoding

	@property
	def derror(self):
		"""derror commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_derror'):
			from .Derror import Derror
			self._derror = Derror(self._core, self._cmd_group)
		return self._derror

	@property
	def dpControl(self):
		"""dpControl commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_dpControl'):
			from .DpControl import DpControl
			self._dpControl = DpControl(self._core, self._cmd_group)
		return self._dpControl

	@property
	def interleaver2(self):
		"""interleaver2 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_interleaver2'):
			from .Interleaver2 import Interleaver2
			self._interleaver2 = Interleaver2(self._core, self._cmd_group)
		return self._interleaver2

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def tchannel(self):
		"""tchannel commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_tchannel'):
			from .Tchannel import Tchannel
			self._tchannel = Tchannel(self._core, self._cmd_group)
		return self._tchannel

	def clone(self) -> 'Dpch':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dpch(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
