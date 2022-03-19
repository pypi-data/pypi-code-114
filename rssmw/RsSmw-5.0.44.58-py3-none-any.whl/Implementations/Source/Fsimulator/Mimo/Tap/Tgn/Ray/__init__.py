from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ray:
	"""Ray commands group definition. 6 total commands, 4 Subgroups, 0 group commands
	Repeated Capability: Ray, default value after init: Ray.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ray", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_ray_get', 'repcap_ray_set', repcap.Ray.Nr1)

	def repcap_ray_set(self, ray: repcap.Ray) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Ray.Default
		Default value after init: Ray.Nr1"""
		self._cmd_group.set_repcap_enum_value(ray)

	def repcap_ray_get(self) -> repcap.Ray:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def arrival(self):
		"""arrival commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_arrival'):
			from .Arrival import Arrival
			self._arrival = Arrival(self._core, self._cmd_group)
		return self._arrival

	@property
	def departure(self):
		"""departure commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_departure'):
			from .Departure import Departure
			self._departure = Departure(self._core, self._cmd_group)
		return self._departure

	@property
	def gain(self):
		"""gain commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gain'):
			from .Gain import Gain
			self._gain = Gain(self._core, self._cmd_group)
		return self._gain

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def clone(self) -> 'Ray':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ray(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
