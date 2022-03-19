from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Lpy:
	"""Lpy commands group definition. 8 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lpy", core, parent)

	@property
	def basic(self):
		"""basic commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_basic'):
			from .Basic import Basic
			self._basic = Basic(self._core, self._cmd_group)
		return self._basic

	@property
	def carrier(self):
		"""carrier commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_carrier'):
			from .Carrier import Carrier
			self._carrier = Carrier(self._core, self._cmd_group)
		return self._carrier

	@property
	def detail(self):
		"""detail commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_detail'):
			from .Detail import Detail
			self._detail = Detail(self._core, self._cmd_group)
		return self._detail

	@property
	def npreamble(self):
		"""npreamble commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_npreamble'):
			from .Npreamble import Npreamble
			self._npreamble = Npreamble(self._core, self._cmd_group)
		return self._npreamble

	@property
	def pilot(self):
		"""pilot commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pilot'):
			from .Pilot import Pilot
			self._pilot = Pilot(self._core, self._cmd_group)
		return self._pilot

	def clone(self) -> 'Lpy':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Lpy(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
