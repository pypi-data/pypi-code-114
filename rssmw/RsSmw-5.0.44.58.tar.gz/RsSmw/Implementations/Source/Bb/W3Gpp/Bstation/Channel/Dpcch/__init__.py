from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dpcch:
	"""Dpcch commands group definition. 13 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dpcch", core, parent)

	@property
	def mcode(self):
		"""mcode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcode'):
			from .Mcode import Mcode
			self._mcode = Mcode(self._core, self._cmd_group)
		return self._mcode

	@property
	def plength(self):
		"""plength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_plength'):
			from .Plength import Plength
			self._plength = Plength(self._core, self._cmd_group)
		return self._plength

	@property
	def poffset(self):
		"""poffset commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_poffset'):
			from .Poffset import Poffset
			self._poffset = Poffset(self._core, self._cmd_group)
		return self._poffset

	@property
	def tfci(self):
		"""tfci commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_tfci'):
			from .Tfci import Tfci
			self._tfci = Tfci(self._core, self._cmd_group)
		return self._tfci

	@property
	def tpc(self):
		"""tpc commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_tpc'):
			from .Tpc import Tpc
			self._tpc = Tpc(self._core, self._cmd_group)
		return self._tpc

	def clone(self) -> 'Dpcch':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dpcch(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
