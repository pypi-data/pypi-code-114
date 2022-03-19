from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Base:
	"""Base commands group definition. 22 total commands, 2 Subgroups, 0 group commands
	Repeated Capability: BaseSt, default value after init: BaseSt.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("base", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_baseSt_get', 'repcap_baseSt_set', repcap.BaseSt.Nr1)

	def repcap_baseSt_set(self, baseSt: repcap.BaseSt) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to BaseSt.Default
		Default value after init: BaseSt.Nr1"""
		self._cmd_group.set_repcap_enum_value(baseSt)

	def repcap_baseSt_get(self) -> repcap.BaseSt:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def a(self):
		"""a commands group. 9 Sub-classes, 0 commands."""
		if not hasattr(self, '_a'):
			from .A import A
			self._a = A(self._core, self._cmd_group)
		return self._a

	@property
	def location(self):
		"""location commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_location'):
			from .Location import Location
			self._location = Location(self._core, self._cmd_group)
		return self._location

	def clone(self) -> 'Base':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Base(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
