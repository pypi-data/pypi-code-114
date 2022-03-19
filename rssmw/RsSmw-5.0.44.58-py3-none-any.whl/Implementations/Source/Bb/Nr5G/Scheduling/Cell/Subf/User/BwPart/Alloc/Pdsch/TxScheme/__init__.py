from .............Internal.Core import Core
from .............Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TxScheme:
	"""TxScheme commands group definition. 12 total commands, 9 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("txScheme", core, parent)

	@property
	def apcsirs(self):
		"""apcsirs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_apcsirs'):
			from .Apcsirs import Apcsirs
			self._apcsirs = Apcsirs(self._core, self._cmd_group)
		return self._apcsirs

	@property
	def cbmd(self):
		"""cbmd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cbmd'):
			from .Cbmd import Cbmd
			self._cbmd = Cbmd(self._core, self._cmd_group)
		return self._cbmd

	@property
	def cbType(self):
		"""cbType commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cbType'):
			from .CbType import CbType
			self._cbType = CbType(self._core, self._cmd_group)
		return self._cbType

	@property
	def cdmData(self):
		"""cdmData commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cdmData'):
			from .CdmData import CdmData
			self._cdmData = CdmData(self._core, self._cmd_group)
		return self._cdmData

	@property
	def intervp(self):
		"""intervp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_intervp'):
			from .Intervp import Intervp
			self._intervp = Intervp(self._core, self._cmd_group)
		return self._intervp

	@property
	def nlayers(self):
		"""nlayers commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nlayers'):
			from .Nlayers import Nlayers
			self._nlayers = Nlayers(self._core, self._cmd_group)
		return self._nlayers

	@property
	def pcn1(self):
		"""pcn1 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pcn1'):
			from .Pcn1 import Pcn1
			self._pcn1 = Pcn1(self._core, self._cmd_group)
		return self._pcn1

	@property
	def pcn2(self):
		"""pcn2 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pcn2'):
			from .Pcn2 import Pcn2
			self._pcn2 = Pcn2(self._core, self._cmd_group)
		return self._pcn2

	@property
	def spcb(self):
		"""spcb commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_spcb'):
			from .Spcb import Spcb
			self._spcb = Spcb(self._core, self._cmd_group)
		return self._spcb

	def clone(self) -> 'TxScheme':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TxScheme(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
