from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rcs:
	"""Rcs commands group definition. 6 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rcs", core, parent)

	@property
	def mean(self):
		"""mean commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mean'):
			from .Mean import Mean
			self._mean = Mean(self._core, self._cmd_group)
		return self._mean

	@property
	def model(self):
		"""model commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_model'):
			from .Model import Model
			self._model = Model(self._core, self._cmd_group)
		return self._model

	@property
	def peak(self):
		"""peak commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_peak'):
			from .Peak import Peak
			self._peak = Peak(self._core, self._cmd_group)
		return self._peak

	@property
	def sper(self):
		"""sper commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sper'):
			from .Sper import Sper
			self._sper = Sper(self._core, self._cmd_group)
		return self._sper

	@property
	def tcoverage(self):
		"""tcoverage commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tcoverage'):
			from .Tcoverage import Tcoverage
			self._tcoverage = Tcoverage(self._core, self._cmd_group)
		return self._tcoverage

	@property
	def upInterval(self):
		"""upInterval commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_upInterval'):
			from .UpInterval import UpInterval
			self._upInterval = UpInterval(self._core, self._cmd_group)
		return self._upInterval

	def clone(self) -> 'Rcs':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Rcs(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
