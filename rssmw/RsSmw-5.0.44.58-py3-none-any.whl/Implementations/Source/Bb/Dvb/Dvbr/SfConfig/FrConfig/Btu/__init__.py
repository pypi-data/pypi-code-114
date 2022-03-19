from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Btu:
	"""Btu commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("btu", core, parent)

	@property
	def bw(self):
		"""bw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bw'):
			from .Bw import Bw
			self._bw = Bw(self._core, self._cmd_group)
		return self._bw

	@property
	def chiRate(self):
		"""chiRate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_chiRate'):
			from .ChiRate import ChiRate
			self._chiRate = ChiRate(self._core, self._cmd_group)
		return self._chiRate

	@property
	def duration(self):
		"""duration commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_duration'):
			from .Duration import Duration
			self._duration = Duration(self._core, self._cmd_group)
		return self._duration

	@property
	def sybRate(self):
		"""sybRate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sybRate'):
			from .SybRate import SybRate
			self._sybRate = SybRate(self._core, self._cmd_group)
		return self._sybRate

	@property
	def tuCount(self):
		"""tuCount commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tuCount'):
			from .TuCount import TuCount
			self._tuCount = TuCount(self._core, self._cmd_group)
		return self._tuCount

	def clone(self) -> 'Btu':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Btu(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
