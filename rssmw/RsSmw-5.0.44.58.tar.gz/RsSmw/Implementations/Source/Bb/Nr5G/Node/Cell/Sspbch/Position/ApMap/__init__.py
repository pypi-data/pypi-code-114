from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal.RepeatedCapability import RepeatedCapability
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ApMap:
	"""ApMap commands group definition. 5 total commands, 2 Subgroups, 0 group commands
	Repeated Capability: AntennaPortNull, default value after init: AntennaPortNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("apMap", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_antennaPortNull_get', 'repcap_antennaPortNull_set', repcap.AntennaPortNull.Nr0)

	def repcap_antennaPortNull_set(self, antennaPortNull: repcap.AntennaPortNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to AntennaPortNull.Default
		Default value after init: AntennaPortNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(antennaPortNull)

	def repcap_antennaPortNull_get(self) -> repcap.AntennaPortNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def col(self):
		"""col commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_col'):
			from .Col import Col
			self._col = Col(self._core, self._cmd_group)
		return self._col

	@property
	def mindex(self):
		"""mindex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mindex'):
			from .Mindex import Mindex
			self._mindex = Mindex(self._core, self._cmd_group)
		return self._mindex

	def clone(self) -> 'ApMap':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ApMap(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
