from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dsch:
	"""Dsch commands group definition. 17 total commands, 17 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dsch", core, parent)

	@property
	def anfMode(self):
		"""anfMode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_anfMode'):
			from .AnfMode import AnfMode
			self._anfMode = AnfMode(self._core, self._cmd_group)
		return self._anfMode

	@property
	def ccoding(self):
		"""ccoding commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ccoding'):
			from .Ccoding import Ccoding
			self._ccoding = Ccoding(self._core, self._cmd_group)
		return self._ccoding

	@property
	def cdin(self):
		"""cdin commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cdin'):
			from .Cdin import Cdin
			self._cdin = Cdin(self._core, self._cmd_group)
		return self._cdin

	@property
	def cods(self):
		"""cods commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cods'):
			from .Cods import Cods
			self._cods = Cods(self._core, self._cmd_group)
		return self._cods

	@property
	def da02(self):
		"""da02 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_da02'):
			from .Da02 import Da02
			self._da02 = Da02(self._core, self._cmd_group)
		return self._da02

	@property
	def dait(self):
		"""dait commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dait'):
			from .Dait import Dait
			self._dait = Dait(self._core, self._cmd_group)
		return self._dait

	@property
	def data(self):
		"""data commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_data'):
			from .Data import Data
			self._data = Data(self._core, self._cmd_group)
		return self._data

	@property
	def daul(self):
		"""daul commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_daul'):
			from .Daul import Daul
			self._daul = Daul(self._core, self._cmd_group)
		return self._daul

	@property
	def dlist(self):
		"""dlist commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dlist'):
			from .Dlist import Dlist
			self._dlist = Dlist(self._core, self._cmd_group)
		return self._dlist

	@property
	def initPattern(self):
		"""initPattern commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_initPattern'):
			from .InitPattern import InitPattern
			self._initPattern = InitPattern(self._core, self._cmd_group)
		return self._initPattern

	@property
	def nrbs(self):
		"""nrbs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nrbs'):
			from .Nrbs import Nrbs
			self._nrbs = Nrbs(self._core, self._cmd_group)
		return self._nrbs

	@property
	def nssf(self):
		"""nssf commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nssf'):
			from .Nssf import Nssf
			self._nssf = Nssf(self._core, self._cmd_group)
		return self._nssf

	@property
	def pattern(self):
		"""pattern commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pattern'):
			from .Pattern import Pattern
			self._pattern = Pattern(self._core, self._cmd_group)
		return self._pattern

	@property
	def ph1F(self):
		"""ph1F commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ph1F'):
			from .Ph1F import Ph1F
			self._ph1F = Ph1F(self._core, self._cmd_group)
		return self._ph1F

	@property
	def rbis(self):
		"""rbis commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rbis'):
			from .Rbis import Rbis
			self._rbis = Rbis(self._core, self._cmd_group)
		return self._rbis

	@property
	def scgw(self):
		"""scgw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scgw'):
			from .Scgw import Scgw
			self._scgw = Scgw(self._core, self._cmd_group)
		return self._scgw

	@property
	def scrambling(self):
		"""scrambling commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_scrambling'):
			from .Scrambling import Scrambling
			self._scrambling = Scrambling(self._core, self._cmd_group)
		return self._scrambling

	def clone(self) -> 'Dsch':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dsch(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
