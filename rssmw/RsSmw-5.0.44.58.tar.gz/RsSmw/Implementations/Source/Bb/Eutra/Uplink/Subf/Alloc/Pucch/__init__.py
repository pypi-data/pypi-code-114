from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pucch:
	"""Pucch commands group definition. 20 total commands, 15 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pucch", core, parent)

	@property
	def conflict(self):
		"""conflict commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_conflict'):
			from .Conflict import Conflict
			self._conflict = Conflict(self._core, self._cmd_group)
		return self._conflict

	@property
	def cqi(self):
		"""cqi commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_cqi'):
			from .Cqi import Cqi
			self._cqi = Cqi(self._core, self._cmd_group)
		return self._cqi

	@property
	def cycShift(self):
		"""cycShift commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cycShift'):
			from .CycShift import CycShift
			self._cycShift = CycShift(self._core, self._cmd_group)
		return self._cycShift

	@property
	def dmr1(self):
		"""dmr1 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dmr1'):
			from .Dmr1 import Dmr1
			self._dmr1 = Dmr1(self._core, self._cmd_group)
		return self._dmr1

	@property
	def dmr2(self):
		"""dmr2 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dmr2'):
			from .Dmr2 import Dmr2
			self._dmr2 = Dmr2(self._core, self._cmd_group)
		return self._dmr2

	@property
	def harq(self):
		"""harq commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_harq'):
			from .Harq import Harq
			self._harq = Harq(self._core, self._cmd_group)
		return self._harq

	@property
	def mrb(self):
		"""mrb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mrb'):
			from .Mrb import Mrb
			self._mrb = Mrb(self._core, self._cmd_group)
		return self._mrb

	@property
	def napUsed(self):
		"""napUsed commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_napUsed'):
			from .NapUsed import NapUsed
			self._napUsed = NapUsed(self._core, self._cmd_group)
		return self._napUsed

	@property
	def noc(self):
		"""noc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_noc'):
			from .Noc import Noc
			self._noc = Noc(self._core, self._cmd_group)
		return self._noc

	@property
	def npar(self):
		"""npar commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_npar'):
			from .Npar import Npar
			self._npar = Npar(self._core, self._cmd_group)
		return self._npar

	@property
	def physBits(self):
		"""physBits commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_physBits'):
			from .PhysBits import PhysBits
			self._physBits = PhysBits(self._core, self._cmd_group)
		return self._physBits

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def rbCount(self):
		"""rbCount commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rbCount'):
			from .RbCount import RbCount
			self._rbCount = RbCount(self._core, self._cmd_group)
		return self._rbCount

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def formatPy(self):
		"""formatPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_formatPy'):
			from .FormatPy import FormatPy
			self._formatPy = FormatPy(self._core, self._cmd_group)
		return self._formatPy

	def clone(self) -> 'Pucch':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pucch(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
