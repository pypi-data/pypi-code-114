from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Iqcoder:
	"""Iqcoder commands group definition. 13 total commands, 8 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iqcoder", core, parent)

	@property
	def atsm(self):
		"""atsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_atsm'):
			from .Atsm import Atsm
			self._atsm = Atsm(self._core, self._cmd_group)
		return self._atsm

	@property
	def dtmb(self):
		"""dtmb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dtmb'):
			from .Dtmb import Dtmb
			self._dtmb = Dtmb(self._core, self._cmd_group)
		return self._dtmb

	@property
	def dvbc(self):
		"""dvbc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dvbc'):
			from .Dvbc import Dvbc
			self._dvbc = Dvbc(self._core, self._cmd_group)
		return self._dvbc

	@property
	def dvbs2(self):
		"""dvbs2 commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_dvbs2'):
			from .Dvbs2 import Dvbs2
			self._dvbs2 = Dvbs2(self._core, self._cmd_group)
		return self._dvbs2

	@property
	def dvbs(self):
		"""dvbs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dvbs'):
			from .Dvbs import Dvbs
			self._dvbs = Dvbs(self._core, self._cmd_group)
		return self._dvbs

	@property
	def dvbt(self):
		"""dvbt commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_dvbt'):
			from .Dvbt import Dvbt
			self._dvbt = Dvbt(self._core, self._cmd_group)
		return self._dvbt

	@property
	def isdbt(self):
		"""isdbt commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_isdbt'):
			from .Isdbt import Isdbt
			self._isdbt = Isdbt(self._core, self._cmd_group)
		return self._isdbt

	@property
	def j83B(self):
		"""j83B commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_j83B'):
			from .J83B import J83B
			self._j83B = J83B(self._core, self._cmd_group)
		return self._j83B

	def clone(self) -> 'Iqcoder':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Iqcoder(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
