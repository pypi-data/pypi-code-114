from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cell:
	"""Cell commands group definition. 142 total commands, 12 Subgroups, 0 group commands
	Repeated Capability: Cell, default value after init: Cell.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cell", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_cell_get', 'repcap_cell_set', repcap.Cell.Nr1)

	def repcap_cell_set(self, cell: repcap.Cell) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Cell.Default
		Default value after init: Cell.Nr1"""
		self._cmd_group.set_repcap_enum_value(cell)

	def repcap_cell_get(self) -> repcap.Cell:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def dwpts(self):
		"""dwpts commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_dwpts'):
			from .Dwpts import Dwpts
			self._dwpts = Dwpts(self._core, self._cmd_group)
		return self._dwpts

	@property
	def enh(self):
		"""enh commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_enh'):
			from .Enh import Enh
			self._enh = Enh(self._core, self._cmd_group)
		return self._enh

	@property
	def mcode(self):
		"""mcode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcode'):
			from .Mcode import Mcode
			self._mcode = Mcode(self._core, self._cmd_group)
		return self._mcode

	@property
	def protation(self):
		"""protation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_protation'):
			from .Protation import Protation
			self._protation = Protation(self._core, self._cmd_group)
		return self._protation

	@property
	def scode(self):
		"""scode commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_scode'):
			from .Scode import Scode
			self._scode = Scode(self._core, self._cmd_group)
		return self._scode

	@property
	def sdCode(self):
		"""sdCode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sdCode'):
			from .SdCode import SdCode
			self._sdCode = SdCode(self._core, self._cmd_group)
		return self._sdCode

	@property
	def slot(self):
		"""slot commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_slot'):
			from .Slot import Slot
			self._slot = Slot(self._core, self._cmd_group)
		return self._slot

	@property
	def spoint(self):
		"""spoint commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_spoint'):
			from .Spoint import Spoint
			self._spoint = Spoint(self._core, self._cmd_group)
		return self._spoint

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def suCode(self):
		"""suCode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_suCode'):
			from .SuCode import SuCode
			self._suCode = SuCode(self._core, self._cmd_group)
		return self._suCode

	@property
	def tdelay(self):
		"""tdelay commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tdelay'):
			from .Tdelay import Tdelay
			self._tdelay = Tdelay(self._core, self._cmd_group)
		return self._tdelay

	@property
	def users(self):
		"""users commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_users'):
			from .Users import Users
			self._users = Users(self._core, self._cmd_group)
		return self._users

	def clone(self) -> 'Cell':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cell(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
