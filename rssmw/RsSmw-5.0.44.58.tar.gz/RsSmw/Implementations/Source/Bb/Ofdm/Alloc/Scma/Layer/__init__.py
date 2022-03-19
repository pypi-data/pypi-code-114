from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Layer:
	"""Layer commands group definition. 3 total commands, 3 Subgroups, 0 group commands
	Repeated Capability: LayerNull, default value after init: LayerNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("layer", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_layerNull_get', 'repcap_layerNull_set', repcap.LayerNull.Nr0)

	def repcap_layerNull_set(self, layerNull: repcap.LayerNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to LayerNull.Default
		Default value after init: LayerNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(layerNull)

	def repcap_layerNull_get(self) -> repcap.LayerNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def pwr(self):
		"""pwr commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pwr'):
			from .Pwr import Pwr
			self._pwr = Pwr(self._core, self._cmd_group)
		return self._pwr

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def user(self):
		"""user commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_user'):
			from .User import User
			self._user = User(self._core, self._cmd_group)
		return self._user

	def clone(self) -> 'Layer':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Layer(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
