from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal.RepeatedCapability import RepeatedCapability
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Set:
	"""Set commands group definition. 10 total commands, 10 Subgroups, 0 group commands
	Repeated Capability: SetItem, default value after init: SetItem.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("set", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_setItem_get', 'repcap_setItem_set', repcap.SetItem.Nr1)

	def repcap_setItem_set(self, setItem: repcap.SetItem) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to SetItem.Default
		Default value after init: SetItem.Nr1"""
		self._cmd_group.set_repcap_enum_value(setItem)

	def repcap_setItem_get(self) -> repcap.SetItem:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def hopping(self):
		"""hopping commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hopping'):
			from .Hopping import Hopping
			self._hopping = Hopping(self._core, self._cmd_group)
		return self._hopping

	@property
	def nid(self):
		"""nid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nid'):
			from .Nid import Nid
			self._nid = Nid(self._core, self._cmd_group)
		return self._nid

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def prbs(self):
		"""prbs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_prbs'):
			from .Prbs import Prbs
			self._prbs = Prbs(self._core, self._cmd_group)
		return self._prbs

	@property
	def rba(self):
		"""rba commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rba'):
			from .Rba import Rba
			self._rba = Rba(self._core, self._cmd_group)
		return self._rba

	@property
	def repmpdcch(self):
		"""repmpdcch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_repmpdcch'):
			from .Repmpdcch import Repmpdcch
			self._repmpdcch = Repmpdcch(self._core, self._cmd_group)
		return self._repmpdcch

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def stnb(self):
		"""stnb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stnb'):
			from .Stnb import Stnb
			self._stnb = Stnb(self._core, self._cmd_group)
		return self._stnb

	@property
	def stsf(self):
		"""stsf commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stsf'):
			from .Stsf import Stsf
			self._stsf = Stsf(self._core, self._cmd_group)
		return self._stsf

	@property
	def ttyp(self):
		"""ttyp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ttyp'):
			from .Ttyp import Ttyp
			self._ttyp = Ttyp(self._core, self._cmd_group)
		return self._ttyp

	def clone(self) -> 'Set':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Set(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
