from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cell:
	"""Cell commands group definition. 15 total commands, 14 Subgroups, 0 group commands
	Repeated Capability: CellNull, default value after init: CellNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cell", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_cellNull_get', 'repcap_cellNull_set', repcap.CellNull.Nr0)

	def repcap_cellNull_set(self, cellNull: repcap.CellNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to CellNull.Default
		Default value after init: CellNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(cellNull)

	def repcap_cellNull_get(self) -> repcap.CellNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def bw(self):
		"""bw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bw'):
			from .Bw import Bw
			self._bw = Bw(self._core, self._cmd_group)
		return self._bw

	@property
	def cif(self):
		"""cif commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cif'):
			from .Cif import Cif
			self._cif = Cif(self._core, self._cmd_group)
		return self._cif

	@property
	def dfreq(self):
		"""dfreq commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dfreq'):
			from .Dfreq import Dfreq
			self._dfreq = Dfreq(self._core, self._cmd_group)
		return self._dfreq

	@property
	def id(self):
		"""id commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_id'):
			from .Id import Id
			self._id = Id(self._core, self._cmd_group)
		return self._id

	@property
	def index(self):
		"""index commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_index'):
			from .Index import Index
			self._index = Index(self._core, self._cmd_group)
		return self._index

	@property
	def nidcsi(self):
		"""nidcsi commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nidcsi'):
			from .Nidcsi import Nidcsi
			self._nidcsi = Nidcsi(self._core, self._cmd_group)
		return self._nidcsi

	@property
	def phich(self):
		"""phich commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_phich'):
			from .Phich import Phich
			self._phich = Phich(self._core, self._cmd_group)
		return self._phich

	@property
	def poffset(self):
		"""poffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_poffset'):
			from .Poffset import Poffset
			self._poffset = Poffset(self._core, self._cmd_group)
		return self._poffset

	@property
	def pstart(self):
		"""pstart commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pstart'):
			from .Pstart import Pstart
			self._pstart = Pstart(self._core, self._cmd_group)
		return self._pstart

	@property
	def scIndex(self):
		"""scIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scIndex'):
			from .ScIndex import ScIndex
			self._scIndex = ScIndex(self._core, self._cmd_group)
		return self._scIndex

	@property
	def spsConf(self):
		"""spsConf commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_spsConf'):
			from .SpsConf import SpsConf
			self._spsConf = SpsConf(self._core, self._cmd_group)
		return self._spsConf

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def tdelay(self):
		"""tdelay commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tdelay'):
			from .Tdelay import Tdelay
			self._tdelay = Tdelay(self._core, self._cmd_group)
		return self._tdelay

	@property
	def udConf(self):
		"""udConf commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_udConf'):
			from .UdConf import UdConf
			self._udConf = UdConf(self._core, self._cmd_group)
		return self._udConf

	def clone(self) -> 'Cell':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cell(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
