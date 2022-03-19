from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pusch:
	"""Pusch commands group definition. 8 total commands, 8 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pusch", core, parent)

	@property
	def esupport(self):
		"""esupport commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_esupport'):
			from .Esupport import Esupport
			self._esupport = Esupport(self._core, self._cmd_group)
		return self._esupport

	@property
	def etbs(self):
		"""etbs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_etbs'):
			from .Etbs import Etbs
			self._etbs = Etbs(self._core, self._cmd_group)
		return self._etbs

	@property
	def etrSize(self):
		"""etrSize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_etrSize'):
			from .EtrSize import EtrSize
			self._etrSize = EtrSize(self._core, self._cmd_group)
		return self._etrSize

	@property
	def physBits(self):
		"""physBits commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_physBits'):
			from .PhysBits import PhysBits
			self._physBits = PhysBits(self._core, self._cmd_group)
		return self._physBits

	@property
	def ruIndex(self):
		"""ruIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ruIndex'):
			from .RuIndex import RuIndex
			self._ruIndex = RuIndex(self._core, self._cmd_group)
		return self._ruIndex

	@property
	def rvIndex(self):
		"""rvIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rvIndex'):
			from .RvIndex import RvIndex
			self._rvIndex = RvIndex(self._core, self._cmd_group)
		return self._rvIndex

	@property
	def tbIndex(self):
		"""tbIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tbIndex'):
			from .TbIndex import TbIndex
			self._tbIndex = TbIndex(self._core, self._cmd_group)
		return self._tbIndex

	@property
	def tbSize(self):
		"""tbSize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tbSize'):
			from .TbSize import TbSize
			self._tbSize = TbSize(self._core, self._cmd_group)
		return self._tbSize

	def clone(self) -> 'Pusch':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pusch(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
