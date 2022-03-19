from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Prach:
	"""Prach commands group definition. 32 total commands, 8 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("prach", core, parent)

	@property
	def att(self):
		"""att commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_att'):
			from .Att import Att
			self._att = Att(self._core, self._cmd_group)
		return self._att

	@property
	def cframes(self):
		"""cframes commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cframes'):
			from .Cframes import Cframes
			self._cframes = Cframes(self._core, self._cmd_group)
		return self._cframes

	@property
	def emtc(self):
		"""emtc commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_emtc'):
			from .Emtc import Emtc
			self._emtc = Emtc(self._core, self._cmd_group)
		return self._emtc

	@property
	def niot(self):
		"""niot commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_niot'):
			from .Niot import Niot
			self._niot = Niot(self._core, self._cmd_group)
		return self._niot

	@property
	def prFormat(self):
		"""prFormat commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_prFormat'):
			from .PrFormat import PrFormat
			self._prFormat = PrFormat(self._core, self._cmd_group)
		return self._prFormat

	@property
	def prState(self):
		"""prState commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_prState'):
			from .PrState import PrState
			self._prState = PrState(self._core, self._cmd_group)
		return self._prState

	@property
	def prtt(self):
		"""prtt commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_prtt'):
			from .Prtt import Prtt
			self._prtt = Prtt(self._core, self._cmd_group)
		return self._prtt

	@property
	def subf(self):
		"""subf commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_subf'):
			from .Subf import Subf
			self._subf = Subf(self._core, self._cmd_group)
		return self._subf

	def clone(self) -> 'Prach':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Prach(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
