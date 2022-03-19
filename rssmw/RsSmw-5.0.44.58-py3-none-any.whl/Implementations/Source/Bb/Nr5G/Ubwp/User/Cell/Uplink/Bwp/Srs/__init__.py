from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Srs:
	"""Srs commands group definition. 31 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("srs", core, parent)

	@property
	def config(self):
		"""config commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_config'):
			from .Config import Config
			self._config = Config(self._core, self._cmd_group)
		return self._config

	@property
	def naPort(self):
		"""naPort commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_naPort'):
			from .NaPort import NaPort
			self._naPort = NaPort(self._core, self._cmd_group)
		return self._naPort

	@property
	def re02(self):
		"""re02 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_re02'):
			from .Re02 import Re02
			self._re02 = Re02(self._core, self._cmd_group)
		return self._re02

	@property
	def request(self):
		"""request commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_request'):
			from .Request import Request
			self._request = Request(self._core, self._cmd_group)
		return self._request

	@property
	def rs(self):
		"""rs commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_rs'):
			from .Rs import Rs
			self._rs = Rs(self._core, self._cmd_group)
		return self._rs

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def clone(self) -> 'Srs':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Srs(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
