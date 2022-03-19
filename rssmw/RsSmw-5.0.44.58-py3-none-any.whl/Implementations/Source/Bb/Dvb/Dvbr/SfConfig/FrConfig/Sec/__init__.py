from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sec:
	"""Sec commands group definition. 29 total commands, 29 Subgroups, 0 group commands
	Repeated Capability: IndexNull, default value after init: IndexNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sec", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_indexNull_get', 'repcap_indexNull_set', repcap.IndexNull.Nr0)

	def repcap_indexNull_set(self, indexNull: repcap.IndexNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to IndexNull.Default
		Default value after init: IndexNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(indexNull)

	def repcap_indexNull_get(self) -> repcap.IndexNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def blChips(self):
		"""blChips commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_blChips'):
			from .BlChips import BlChips
			self._blChips = BlChips(self._core, self._cmd_group)
		return self._blChips

	@property
	def bsOffset(self):
		"""bsOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bsOffset'):
			from .BsOffset import BsOffset
			self._bsOffset = BsOffset(self._core, self._cmd_group)
		return self._bsOffset

	@property
	def bstLen(self):
		"""bstLen commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bstLen'):
			from .BstLen import BstLen
			self._bstLen = BstLen(self._core, self._cmd_group)
		return self._bstLen

	@property
	def dapAtt(self):
		"""dapAtt commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dapAtt'):
			from .DapAtt import DapAtt
			self._dapAtt = DapAtt(self._core, self._cmd_group)
		return self._dapAtt

	@property
	def data(self):
		"""data commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_data'):
			from .Data import Data
			self._data = Data(self._core, self._cmd_group)
		return self._data

	@property
	def listSel(self):
		"""listSel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_listSel'):
			from .ListSel import ListSel
			self._listSel = ListSel(self._core, self._cmd_group)
		return self._listSel

	@property
	def mod(self):
		"""mod commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mod'):
			from .Mod import Mod
			self._mod = Mod(self._core, self._cmd_group)
		return self._mod

	@property
	def modu(self):
		"""modu commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_modu'):
			from .Modu import Modu
			self._modu = Modu(self._core, self._cmd_group)
		return self._modu

	@property
	def npBlocks(self):
		"""npBlocks commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_npBlocks'):
			from .NpBlocks import NpBlocks
			self._npBlocks = NpBlocks(self._core, self._cmd_group)
		return self._npBlocks

	@property
	def p(self):
		"""p commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_p'):
			from .P import P
			self._p = P(self._core, self._cmd_group)
		return self._p

	@property
	def palType(self):
		"""palType commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_palType'):
			from .PalType import PalType
			self._palType = PalType(self._core, self._cmd_group)
		return self._palType

	@property
	def pbLen(self):
		"""pbLen commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pbLen'):
			from .PbLen import PbLen
			self._pbLen = PbLen(self._core, self._cmd_group)
		return self._pbLen

	@property
	def plen(self):
		"""plen commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_plen'):
			from .Plen import Plen
			self._plen = Plen(self._core, self._cmd_group)
		return self._plen

	@property
	def posLen(self):
		"""posLen commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_posLen'):
			from .PosLen import PosLen
			self._posLen = PosLen(self._core, self._cmd_group)
		return self._posLen

	@property
	def pperiod(self):
		"""pperiod commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pperiod'):
			from .Pperiod import Pperiod
			self._pperiod = Pperiod(self._core, self._cmd_group)
		return self._pperiod

	@property
	def preLen(self):
		"""preLen commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_preLen'):
			from .PreLen import PreLen
			self._preLen = PreLen(self._core, self._cmd_group)
		return self._preLen

	@property
	def q0(self):
		"""q0 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_q0'):
			from .Q0 import Q0
			self._q0 = Q0(self._core, self._cmd_group)
		return self._q0

	@property
	def q1(self):
		"""q1 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_q1'):
			from .Q1 import Q1
			self._q1 = Q1(self._core, self._cmd_group)
		return self._q1

	@property
	def q2(self):
		"""q2 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_q2'):
			from .Q2 import Q2
			self._q2 = Q2(self._core, self._cmd_group)
		return self._q2

	@property
	def q3(self):
		"""q3 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_q3'):
			from .Q3 import Q3
			self._q3 = Q3(self._core, self._cmd_group)
		return self._q3

	@property
	def repcount(self):
		"""repcount commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_repcount'):
			from .Repcount import Repcount
			self._repcount = Repcount(self._core, self._cmd_group)
		return self._repcount

	@property
	def sfactor(self):
		"""sfactor commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sfactor'):
			from .Sfactor import Sfactor
			self._sfactor = Sfactor(self._core, self._cmd_group)
		return self._sfactor

	@property
	def stbTu(self):
		"""stbTu commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stbTu'):
			from .StbTu import StbTu
			self._stbTu = StbTu(self._core, self._cmd_group)
		return self._stbTu

	@property
	def tsSize(self):
		"""tsSize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tsSize'):
			from .TsSize import TsSize
			self._tsSize = TsSize(self._core, self._cmd_group)
		return self._tsSize

	@property
	def uw(self):
		"""uw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_uw'):
			from .Uw import Uw
			self._uw = Uw(self._core, self._cmd_group)
		return self._uw

	@property
	def uwLen(self):
		"""uwLen commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_uwLen'):
			from .UwLen import UwLen
			self._uwLen = UwLen(self._core, self._cmd_group)
		return self._uwLen

	@property
	def wpat(self):
		"""wpat commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_wpat'):
			from .Wpat import Wpat
			self._wpat = Wpat(self._core, self._cmd_group)
		return self._wpat

	@property
	def wvId(self):
		"""wvId commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_wvId'):
			from .WvId import WvId
			self._wvId = WvId(self._core, self._cmd_group)
		return self._wvId

	@property
	def ypat(self):
		"""ypat commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ypat'):
			from .Ypat import Ypat
			self._ypat = Ypat(self._core, self._cmd_group)
		return self._ypat

	def clone(self) -> 'Sec':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sec(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
