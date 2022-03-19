from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Niot:
	"""Niot commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("niot", core, parent)

	@property
	def config(self):
		"""config commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_config'):
			from .Config import Config
			self._config = Config(self._core, self._cmd_group)
		return self._config

	@property
	def init(self):
		"""init commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_init'):
			from .Init import Init
			self._init = Init(self._core, self._cmd_group)
		return self._init

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def sfStart(self):
		"""sfStart commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sfStart'):
			from .SfStart import SfStart
			self._sfStart = SfStart(self._core, self._cmd_group)
		return self._sfStart

	@property
	def strt(self):
		"""strt commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_strt'):
			from .Strt import Strt
			self._strt = Strt(self._core, self._cmd_group)
		return self._strt

	def clone(self) -> 'Niot':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Niot(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
