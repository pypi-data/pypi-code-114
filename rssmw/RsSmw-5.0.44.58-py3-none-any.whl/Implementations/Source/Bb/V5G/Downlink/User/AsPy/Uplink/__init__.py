from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Uplink:
	"""Uplink commands group definition. 18 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uplink", core, parent)

	@property
	def afSeq(self):
		"""afSeq commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_afSeq'):
			from .AfSeq import AfSeq
			self._afSeq = AfSeq(self._core, self._cmd_group)
		return self._afSeq

	@property
	def cell(self):
		"""cell commands group. 6 Sub-classes, 2 commands."""
		if not hasattr(self, '_cell'):
			from .Cell import Cell
			self._cell = Cell(self._core, self._cmd_group)
		return self._cell

	@property
	def indi(self):
		"""indi commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_indi'):
			from .Indi import Indi
			self._indi = Indi(self._core, self._cmd_group)
		return self._indi

	@property
	def nhtrans(self):
		"""nhtrans commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nhtrans'):
			from .Nhtrans import Nhtrans
			self._nhtrans = Nhtrans(self._core, self._cmd_group)
		return self._nhtrans

	def clone(self) -> 'Uplink':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Uplink(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
