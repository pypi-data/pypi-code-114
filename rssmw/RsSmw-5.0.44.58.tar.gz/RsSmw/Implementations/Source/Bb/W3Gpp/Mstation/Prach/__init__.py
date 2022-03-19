from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Prach:
	"""Prach commands group definition. 25 total commands, 15 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("prach", core, parent)

	@property
	def aslot(self):
		"""aslot commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aslot'):
			from .Aslot import Aslot
			self._aslot = Aslot(self._core, self._cmd_group)
		return self._aslot

	@property
	def atTiming(self):
		"""atTiming commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_atTiming'):
			from .AtTiming import AtTiming
			self._atTiming = AtTiming(self._core, self._cmd_group)
		return self._atTiming

	@property
	def cpower(self):
		"""cpower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cpower'):
			from .Cpower import Cpower
			self._cpower = Cpower(self._core, self._cmd_group)
		return self._cpower

	@property
	def data(self):
		"""data commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_data'):
			from .Data import Data
			self._data = Data(self._core, self._cmd_group)
		return self._data

	@property
	def dpower(self):
		"""dpower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dpower'):
			from .Dpower import Dpower
			self._dpower = Dpower(self._core, self._cmd_group)
		return self._dpower

	@property
	def mlength(self):
		"""mlength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mlength'):
			from .Mlength import Mlength
			self._mlength = Mlength(self._core, self._cmd_group)
		return self._mlength

	@property
	def ppower(self):
		"""ppower commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_ppower'):
			from .Ppower import Ppower
			self._ppower = Ppower(self._core, self._cmd_group)
		return self._ppower

	@property
	def prepetition(self):
		"""prepetition commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_prepetition'):
			from .Prepetition import Prepetition
			self._prepetition = Prepetition(self._core, self._cmd_group)
		return self._prepetition

	@property
	def rafter(self):
		"""rafter commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rafter'):
			from .Rafter import Rafter
			self._rafter = Rafter(self._core, self._cmd_group)
		return self._rafter

	@property
	def rarb(self):
		"""rarb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rarb'):
			from .Rarb import Rarb
			self._rarb = Rarb(self._core, self._cmd_group)
		return self._rarb

	@property
	def sformat(self):
		"""sformat commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sformat'):
			from .Sformat import Sformat
			self._sformat = Sformat(self._core, self._cmd_group)
		return self._sformat

	@property
	def signature(self):
		"""signature commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_signature'):
			from .Signature import Signature
			self._signature = Signature(self._core, self._cmd_group)
		return self._signature

	@property
	def symbolRate(self):
		"""symbolRate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_symbolRate'):
			from .SymbolRate import SymbolRate
			self._symbolRate = SymbolRate(self._core, self._cmd_group)
		return self._symbolRate

	@property
	def tfci(self):
		"""tfci commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tfci'):
			from .Tfci import Tfci
			self._tfci = Tfci(self._core, self._cmd_group)
		return self._tfci

	@property
	def timing(self):
		"""timing commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_timing'):
			from .Timing import Timing
			self._timing = Timing(self._core, self._cmd_group)
		return self._timing

	def clone(self) -> 'Prach':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Prach(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
