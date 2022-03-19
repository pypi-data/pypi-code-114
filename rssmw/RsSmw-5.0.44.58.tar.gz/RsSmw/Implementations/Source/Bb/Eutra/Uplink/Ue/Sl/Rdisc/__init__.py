from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rdisc:
	"""Rdisc commands group definition. 13 total commands, 13 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rdisc", core, parent)

	@property
	def cperiod(self):
		"""cperiod commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cperiod'):
			from .Cperiod import Cperiod
			self._cperiod = Cperiod(self._core, self._cmd_group)
		return self._cperiod

	@property
	def n1Pdsch(self):
		"""n1Pdsch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_n1Pdsch'):
			from .N1Pdsch import N1Pdsch
			self._n1Pdsch = N1Pdsch(self._core, self._cmd_group)
		return self._n1Pdsch

	@property
	def n2Pdsch(self):
		"""n2Pdsch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_n2Pdsch'):
			from .N2Pdsch import N2Pdsch
			self._n2Pdsch = N2Pdsch(self._core, self._cmd_group)
		return self._n2Pdsch

	@property
	def n3Pdsch(self):
		"""n3Pdsch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_n3Pdsch'):
			from .N3Pdsch import N3Pdsch
			self._n3Pdsch = N3Pdsch(self._core, self._cmd_group)
		return self._n3Pdsch

	@property
	def nrepetitions(self):
		"""nrepetitions commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nrepetitions'):
			from .Nrepetitions import Nrepetitions
			self._nrepetitions = Nrepetitions(self._core, self._cmd_group)
		return self._nrepetitions

	@property
	def nretrans(self):
		"""nretrans commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nretrans'):
			from .Nretrans import Nretrans
			self._nretrans = Nretrans(self._core, self._cmd_group)
		return self._nretrans

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
	def prIndex(self):
		"""prIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_prIndex'):
			from .PrIndex import PrIndex
			self._prIndex = PrIndex(self._core, self._cmd_group)
		return self._prIndex

	@property
	def sfbmp(self):
		"""sfbmp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sfbmp'):
			from .Sfbmp import Sfbmp
			self._sfbmp = Sfbmp(self._core, self._cmd_group)
		return self._sfbmp

	@property
	def sfIndex(self):
		"""sfIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sfIndex'):
			from .SfIndex import SfIndex
			self._sfIndex = SfIndex(self._core, self._cmd_group)
		return self._sfIndex

	def clone(self) -> 'Rdisc':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Rdisc(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
