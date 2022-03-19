from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ccoding:
	"""Ccoding commands group definition. 9 total commands, 9 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ccoding", core, parent)

	@property
	def mib(self):
		"""mib commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mib'):
			from .Mib import Mib
			self._mib = Mib(self._core, self._cmd_group)
		return self._mib

	@property
	def mspare(self):
		"""mspare commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mspare'):
			from .Mspare import Mspare
			self._mspare = Mspare(self._core, self._cmd_group)
		return self._mspare

	@property
	def rsib(self):
		"""rsib commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rsib'):
			from .Rsib import Rsib
			self._rsib = Rsib(self._core, self._cmd_group)
		return self._rsib

	@property
	def sib(self):
		"""sib commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sib'):
			from .Sib import Sib
			self._sib = Sib(self._core, self._cmd_group)
		return self._sib

	@property
	def soffset(self):
		"""soffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_soffset'):
			from .Soffset import Soffset
			self._soffset = Soffset(self._core, self._cmd_group)
		return self._soffset

	@property
	def srPeriod(self):
		"""srPeriod commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_srPeriod'):
			from .SrPeriod import SrPeriod
			self._srPeriod = SrPeriod(self._core, self._cmd_group)
		return self._srPeriod

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def tbsi(self):
		"""tbsi commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tbsi'):
			from .Tbsi import Tbsi
			self._tbsi = Tbsi(self._core, self._cmd_group)
		return self._tbsi

	@property
	def tbSize(self):
		"""tbSize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tbSize'):
			from .TbSize import TbSize
			self._tbSize = TbSize(self._core, self._cmd_group)
		return self._tbSize

	def clone(self) -> 'Ccoding':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ccoding(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
