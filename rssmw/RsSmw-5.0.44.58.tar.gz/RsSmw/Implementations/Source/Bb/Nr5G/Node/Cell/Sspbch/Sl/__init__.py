from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sl:
	"""Sl commands group definition. 6 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sl", core, parent)

	@property
	def binPeriod(self):
		"""binPeriod commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_binPeriod'):
			from .BinPeriod import BinPeriod
			self._binPeriod = BinPeriod(self._core, self._cmd_group)
		return self._binPeriod

	@property
	def inCoverage(self):
		"""inCoverage commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_inCoverage'):
			from .InCoverage import InCoverage
			self._inCoverage = InCoverage(self._core, self._cmd_group)
		return self._inCoverage

	@property
	def interval(self):
		"""interval commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_interval'):
			from .Interval import Interval
			self._interval = Interval(self._core, self._cmd_group)
		return self._interval

	@property
	def sbits(self):
		"""sbits commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sbits'):
			from .Sbits import Sbits
			self._sbits = Sbits(self._core, self._cmd_group)
		return self._sbits

	@property
	def tddConf(self):
		"""tddConf commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tddConf'):
			from .TddConf import TddConf
			self._tddConf = TddConf(self._core, self._cmd_group)
		return self._tddConf

	@property
	def toffs(self):
		"""toffs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_toffs'):
			from .Toffs import Toffs
			self._toffs = Toffs(self._core, self._cmd_group)
		return self._toffs

	def clone(self) -> 'Sl':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sl(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
