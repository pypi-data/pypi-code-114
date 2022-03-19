from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class V:
	"""V commands group definition. 16 total commands, 1 Subgroups, 0 group commands
	Repeated Capability: Vehicle, default value after init: Vehicle.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("v", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_vehicle_get', 'repcap_vehicle_set', repcap.Vehicle.Nr1)

	def repcap_vehicle_set(self, vehicle: repcap.Vehicle) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Vehicle.Default
		Default value after init: Vehicle.Nr1"""
		self._cmd_group.set_repcap_enum_value(vehicle)

	def repcap_vehicle_get(self) -> repcap.Vehicle:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def a(self):
		"""a commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_a'):
			from .A import A
			self._a = A(self._core, self._cmd_group)
		return self._a

	def clone(self) -> 'V':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = V(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
