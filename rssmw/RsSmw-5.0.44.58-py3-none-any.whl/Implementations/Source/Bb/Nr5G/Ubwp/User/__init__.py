from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class User:
	"""User commands group definition. 379 total commands, 8 Subgroups, 0 group commands
	Repeated Capability: UserNull, default value after init: UserNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("user", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_userNull_get', 'repcap_userNull_set', repcap.UserNull.Nr0)

	def repcap_userNull_set(self, userNull: repcap.UserNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to UserNull.Default
		Default value after init: UserNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(userNull)

	def repcap_userNull_get(self) -> repcap.UserNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def cell(self):
		"""cell commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_cell'):
			from .Cell import Cell
			self._cell = Cell(self._core, self._cmd_group)
		return self._cell

	@property
	def dsch(self):
		"""dsch commands group. 17 Sub-classes, 0 commands."""
		if not hasattr(self, '_dsch'):
			from .Dsch import Dsch
			self._dsch = Dsch(self._core, self._cmd_group)
		return self._dsch

	@property
	def ncarrier(self):
		"""ncarrier commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ncarrier'):
			from .Ncarrier import Ncarrier
			self._ncarrier = Ncarrier(self._core, self._cmd_group)
		return self._ncarrier

	@property
	def numSfi(self):
		"""numSfi commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_numSfi'):
			from .NumSfi import NumSfi
			self._numSfi = NumSfi(self._core, self._cmd_group)
		return self._numSfi

	@property
	def rnti(self):
		"""rnti commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_rnti'):
			from .Rnti import Rnti
			self._rnti = Rnti(self._core, self._cmd_group)
		return self._rnti

	@property
	def ssch(self):
		"""ssch commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_ssch'):
			from .Ssch import Ssch
			self._ssch = Ssch(self._core, self._cmd_group)
		return self._ssch

	@property
	def ueId(self):
		"""ueId commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ueId'):
			from .UeId import UeId
			self._ueId = UeId(self._core, self._cmd_group)
		return self._ueId

	@property
	def usch(self):
		"""usch commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_usch'):
			from .Usch import Usch
			self._usch = Usch(self._core, self._cmd_group)
		return self._usch

	def clone(self) -> 'User':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = User(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
