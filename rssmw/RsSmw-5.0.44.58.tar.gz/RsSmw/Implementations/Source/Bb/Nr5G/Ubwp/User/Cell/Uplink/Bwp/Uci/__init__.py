from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Uci:
	"""Uci commands group definition. 12 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uci", core, parent)

	@property
	def alpha(self):
		"""alpha commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_alpha'):
			from .Alpha import Alpha
			self._alpha = Alpha(self._core, self._cmd_group)
		return self._alpha

	@property
	def cguci(self):
		"""cguci commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_cguci'):
			from .Cguci import Cguci
			self._cguci = Cguci(self._core, self._cmd_group)
		return self._cguci

	@property
	def csi(self):
		"""csi commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_csi'):
			from .Csi import Csi
			self._csi = Csi(self._core, self._cmd_group)
		return self._csi

	@property
	def harq(self):
		"""harq commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_harq'):
			from .Harq import Harq
			self._harq = Harq(self._core, self._cmd_group)
		return self._harq

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import Mode
			self._mode = Mode(self._core, self._cmd_group)
		return self._mode

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def clone(self) -> 'Uci':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Uci(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
