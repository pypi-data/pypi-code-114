from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rpc:
	"""Rpc commands group definition. 5 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rpc", core, parent)

	@property
	def inject(self):
		"""inject commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_inject'):
			from .Inject import Inject
			self._inject = Inject(self._core, self._cmd_group)
		return self._inject

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import Mode
			self._mode = Mode(self._core, self._cmd_group)
		return self._mode

	@property
	def range(self):
		"""range commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_range'):
			from .Range import Range
			self._range = Range(self._core, self._cmd_group)
		return self._range

	@property
	def zone(self):
		"""zone commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_zone'):
			from .Zone import Zone
			self._zone = Zone(self._core, self._cmd_group)
		return self._zone

	def clone(self) -> 'Rpc':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Rpc(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
