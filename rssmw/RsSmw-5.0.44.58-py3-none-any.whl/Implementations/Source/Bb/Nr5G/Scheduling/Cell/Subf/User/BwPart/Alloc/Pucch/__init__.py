from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pucch:
	"""Pucch commands group definition. 17 total commands, 8 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pucch", core, parent)

	@property
	def fs(self):
		"""fs commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_fs'):
			from .Fs import Fs
			self._fs = Fs(self._core, self._cmd_group)
		return self._fs

	@property
	def grpHopping(self):
		"""grpHopping commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_grpHopping'):
			from .GrpHopping import GrpHopping
			self._grpHopping = GrpHopping(self._core, self._cmd_group)
		return self._grpHopping

	@property
	def hopId(self):
		"""hopId commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hopId'):
			from .HopId import HopId
			self._hopId = HopId(self._core, self._cmd_group)
		return self._hopId

	@property
	def int(self):
		"""int commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_int'):
			from .Int import Int
			self._int = Int(self._core, self._cmd_group)
		return self._int

	@property
	def isfHopping(self):
		"""isfHopping commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_isfHopping'):
			from .IsfHopping import IsfHopping
			self._isfHopping = IsfHopping(self._core, self._cmd_group)
		return self._isfHopping

	@property
	def nint(self):
		"""nint commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nint'):
			from .Nint import Nint
			self._nint = Nint(self._core, self._cmd_group)
		return self._nint

	@property
	def pl(self):
		"""pl commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_pl'):
			from .Pl import Pl
			self._pl = Pl(self._core, self._cmd_group)
		return self._pl

	@property
	def shopping(self):
		"""shopping commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_shopping'):
			from .Shopping import Shopping
			self._shopping = Shopping(self._core, self._cmd_group)
		return self._shopping

	def clone(self) -> 'Pucch':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pucch(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
