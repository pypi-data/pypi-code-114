from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rctrl:
	"""Rctrl commands group definition. 6 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rctrl", core, parent)

	@property
	def cperiod(self):
		"""cperiod commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cperiod'):
			from .Cperiod import Cperiod
			self._cperiod = Cperiod(self._core, self._cmd_group)
		return self._cperiod

	@property
	def offsetInd(self):
		"""offsetInd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_offsetInd'):
			from .OffsetInd import OffsetInd
			self._offsetInd = OffsetInd(self._core, self._cmd_group)
		return self._offsetInd

	@property
	def prbNumber(self):
		"""prbNumber commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_prbNumber'):
			from .PrbNumber import PrbNumber
			self._prbNumber = PrbNumber(self._core, self._cmd_group)
		return self._prbNumber

	@property
	def prbStart(self):
		"""prbStart commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_prbStart'):
			from .PrbStart import PrbStart
			self._prbStart = PrbStart(self._core, self._cmd_group)
		return self._prbStart

	@property
	def prend(self):
		"""prend commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_prend'):
			from .Prend import Prend
			self._prend = Prend(self._core, self._cmd_group)
		return self._prend

	@property
	def sfbmp(self):
		"""sfbmp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sfbmp'):
			from .Sfbmp import Sfbmp
			self._sfbmp = Sfbmp(self._core, self._cmd_group)
		return self._sfbmp

	def clone(self) -> 'Rctrl':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Rctrl(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
