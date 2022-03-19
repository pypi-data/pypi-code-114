from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class User:
	"""User commands group definition. 92 total commands, 23 Subgroups, 0 group commands
	Repeated Capability: UserIx, default value after init: UserIx.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("user", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_userIx_get', 'repcap_userIx_set', repcap.UserIx.Nr1)

	def repcap_userIx_set(self, userIx: repcap.UserIx) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to UserIx.Default
		Default value after init: UserIx.Nr1"""
		self._cmd_group.set_repcap_enum_value(userIx)

	def repcap_userIx_get(self) -> repcap.UserIx:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def apm(self):
		"""apm commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_apm'):
			from .Apm import Apm
			self._apm = Apm(self._core, self._cmd_group)
		return self._apm

	@property
	def asPy(self):
		"""asPy commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_asPy'):
			from .AsPy import AsPy
			self._asPy = AsPy(self._core, self._cmd_group)
		return self._asPy

	@property
	def asrs(self):
		"""asrs commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_asrs'):
			from .Asrs import Asrs
			self._asrs = Asrs(self._core, self._cmd_group)
		return self._asrs

	@property
	def ca(self):
		"""ca commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ca'):
			from .Ca import Ca
			self._ca = Ca(self._core, self._cmd_group)
		return self._ca

	@property
	def caw(self):
		"""caw commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_caw'):
			from .Caw import Caw
			self._caw = Caw(self._core, self._cmd_group)
		return self._caw

	@property
	def ccoding(self):
		"""ccoding commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ccoding'):
			from .Ccoding import Ccoding
			self._ccoding = Ccoding(self._core, self._cmd_group)
		return self._ccoding

	@property
	def cell(self):
		"""cell commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cell'):
			from .Cell import Cell
			self._cell = Cell(self._core, self._cmd_group)
		return self._cell

	@property
	def data(self):
		"""data commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_data'):
			from .Data import Data
			self._data = Data(self._core, self._cmd_group)
		return self._data

	@property
	def dselect(self):
		"""dselect commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dselect'):
			from .Dselect import Dselect
			self._dselect = Dselect(self._core, self._cmd_group)
		return self._dselect

	@property
	def eimtaRnti(self):
		"""eimtaRnti commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_eimtaRnti'):
			from .EimtaRnti import EimtaRnti
			self._eimtaRnti = EimtaRnti(self._core, self._cmd_group)
		return self._eimtaRnti

	@property
	def epdcch(self):
		"""epdcch commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_epdcch'):
			from .Epdcch import Epdcch
			self._epdcch = Epdcch(self._core, self._cmd_group)
		return self._epdcch

	@property
	def mcsTwo(self):
		"""mcsTwo commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_mcsTwo'):
			from .McsTwo import McsTwo
			self._mcsTwo = McsTwo(self._core, self._cmd_group)
		return self._mcsTwo

	@property
	def pa(self):
		"""pa commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pa'):
			from .Pa import Pa
			self._pa = Pa(self._core, self._cmd_group)
		return self._pa

	@property
	def pattern(self):
		"""pattern commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pattern'):
			from .Pattern import Pattern
			self._pattern = Pattern(self._core, self._cmd_group)
		return self._pattern

	@property
	def release(self):
		"""release commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_release'):
			from .Release import Release
			self._release = Release(self._core, self._cmd_group)
		return self._release

	@property
	def scrambling(self):
		"""scrambling commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_scrambling'):
			from .Scrambling import Scrambling
			self._scrambling = Scrambling(self._core, self._cmd_group)
		return self._scrambling

	@property
	def sps(self):
		"""sps commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_sps'):
			from .Sps import Sps
			self._sps = Sps(self._core, self._cmd_group)
		return self._sps

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def taltIndex(self):
		"""taltIndex commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_taltIndex'):
			from .TaltIndex import TaltIndex
			self._taltIndex = TaltIndex(self._core, self._cmd_group)
		return self._taltIndex

	@property
	def txm(self):
		"""txm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_txm'):
			from .Txm import Txm
			self._txm = Txm(self._core, self._cmd_group)
		return self._txm

	@property
	def uec(self):
		"""uec commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_uec'):
			from .Uec import Uec
			self._uec = Uec(self._core, self._cmd_group)
		return self._uec

	@property
	def ueId(self):
		"""ueId commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ueId'):
			from .UeId import UeId
			self._ueId = UeId(self._core, self._cmd_group)
		return self._ueId

	@property
	def ulca(self):
		"""ulca commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ulca'):
			from .Ulca import Ulca
			self._ulca = Ulca(self._core, self._cmd_group)
		return self._ulca

	def clone(self) -> 'User':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = User(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
