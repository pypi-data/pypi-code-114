from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Set:
	"""Set commands group definition. 8 total commands, 8 Subgroups, 0 group commands
	Repeated Capability: ModCodSet, default value after init: ModCodSet.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("set", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_modCodSet_get', 'repcap_modCodSet_set', repcap.ModCodSet.Nr1)

	def repcap_modCodSet_set(self, modCodSet: repcap.ModCodSet) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to ModCodSet.Default
		Default value after init: ModCodSet.Nr1"""
		self._cmd_group.set_repcap_enum_value(modCodSet)

	def repcap_modCodSet_get(self) -> repcap.ModCodSet:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def adfl(self):
		"""adfl commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_adfl'):
			from .Adfl import Adfl
			self._adfl = Adfl(self._core, self._cmd_group)
		return self._adfl

	@property
	def ctype(self):
		"""ctype commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ctype'):
			from .Ctype import Ctype
			self._ctype = Ctype(self._core, self._cmd_group)
		return self._ctype

	@property
	def dfl(self):
		"""dfl commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dfl'):
			from .Dfl import Dfl
			self._dfl = Dfl(self._core, self._cmd_group)
		return self._dfl

	@property
	def frames(self):
		"""frames commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frames'):
			from .Frames import Frames
			self._frames = Frames(self._core, self._cmd_group)
		return self._frames

	@property
	def mcod(self):
		"""mcod commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcod'):
			from .Mcod import Mcod
			self._mcod = Mcod(self._core, self._cmd_group)
		return self._mcod

	@property
	def pcod(self):
		"""pcod commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pcod'):
			from .Pcod import Pcod
			self._pcod = Pcod(self._core, self._cmd_group)
		return self._pcod

	@property
	def pstate(self):
		"""pstate commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pstate'):
			from .Pstate import Pstate
			self._pstate = Pstate(self._core, self._cmd_group)
		return self._pstate

	@property
	def sfactor(self):
		"""sfactor commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sfactor'):
			from .Sfactor import Sfactor
			self._sfactor = Sfactor(self._core, self._cmd_group)
		return self._sfactor

	def clone(self) -> 'Set':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Set(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
