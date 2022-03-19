from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Emtc:
	"""Emtc commands group definition. 8 total commands, 8 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("emtc", core, parent)

	@property
	def celv(self):
		"""celv commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_celv'):
			from .Celv import Celv
			self._celv = Celv(self._core, self._cmd_group)
		return self._celv

	@property
	def dt(self):
		"""dt commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dt'):
			from .Dt import Dt
			self._dt = Dt(self._core, self._cmd_group)
		return self._dt

	@property
	def frIndex(self):
		"""frIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frIndex'):
			from .FrIndex import FrIndex
			self._frIndex = FrIndex(self._core, self._cmd_group)
		return self._frIndex

	@property
	def ncsConf(self):
		"""ncsConf commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ncsConf'):
			from .NcsConf import NcsConf
			self._ncsConf = NcsConf(self._core, self._cmd_group)
		return self._ncsConf

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def rsequence(self):
		"""rsequence commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rsequence'):
			from .Rsequence import Rsequence
			self._rsequence = Rsequence(self._core, self._cmd_group)
		return self._rsequence

	@property
	def sfStart(self):
		"""sfStart commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sfStart'):
			from .SfStart import SfStart
			self._sfStart = SfStart(self._core, self._cmd_group)
		return self._sfStart

	@property
	def sindex(self):
		"""sindex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sindex'):
			from .Sindex import Sindex
			self._sindex = Sindex(self._core, self._cmd_group)
		return self._sindex

	def clone(self) -> 'Emtc':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Emtc(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
