from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Zprs:
	"""Zprs commands group definition. 4 total commands, 4 Subgroups, 0 group commands
	Repeated Capability: IndexNull, default value after init: IndexNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("zprs", core, parent)
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
	def zp(self):
		"""zp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_zp'):
			from .Zp import Zp
			self._zp = Zp(self._core, self._cmd_group)
		return self._zp

	@property
	def zpDelta(self):
		"""zpDelta commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_zpDelta'):
			from .ZpDelta import ZpDelta
			self._zpDelta = ZpDelta(self._core, self._cmd_group)
		return self._zpDelta

	@property
	def zpi(self):
		"""zpi commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_zpi'):
			from .Zpi import Zpi
			self._zpi = Zpi(self._core, self._cmd_group)
		return self._zpi

	@property
	def zpt(self):
		"""zpt commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_zpt'):
			from .Zpt import Zpt
			self._zpt = Zpt(self._core, self._cmd_group)
		return self._zpt

	def clone(self) -> 'Zprs':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Zprs(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
