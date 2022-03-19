from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ssc:
	"""Ssc commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ssc", core, parent)

	@property
	def ndlSymbols(self):
		"""ndlSymbols commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ndlSymbols'):
			from .NdlSymbols import NdlSymbols
			self._ndlSymbols = NdlSymbols(self._core, self._cmd_group)
		return self._ndlSymbols

	@property
	def ngSymbols(self):
		"""ngSymbols commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ngSymbols'):
			from .NgSymbols import NgSymbols
			self._ngSymbols = NgSymbols(self._core, self._cmd_group)
		return self._ngSymbols

	@property
	def nulSymbols(self):
		"""nulSymbols commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nulSymbols'):
			from .NulSymbols import NulSymbols
			self._nulSymbols = NulSymbols(self._core, self._cmd_group)
		return self._nulSymbols

	@property
	def sfi(self):
		"""sfi commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sfi'):
			from .Sfi import Sfi
			self._sfi = Sfi(self._core, self._cmd_group)
		return self._sfi

	@property
	def slfmt(self):
		"""slfmt commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_slfmt'):
			from .Slfmt import Slfmt
			self._slfmt = Slfmt(self._core, self._cmd_group)
		return self._slfmt

	def clone(self) -> 'Ssc':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ssc(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
