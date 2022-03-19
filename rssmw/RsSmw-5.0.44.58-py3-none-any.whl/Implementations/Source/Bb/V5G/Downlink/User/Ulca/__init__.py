from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ulca:
	"""Ulca commands group definition. 1 total commands, 1 Subgroups, 0 group commands
	Repeated Capability: UlCarriersNull, default value after init: UlCarriersNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ulca", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_ulCarriersNull_get', 'repcap_ulCarriersNull_set', repcap.UlCarriersNull.Nr0)

	def repcap_ulCarriersNull_set(self, ulCarriersNull: repcap.UlCarriersNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to UlCarriersNull.Default
		Default value after init: UlCarriersNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(ulCarriersNull)

	def repcap_ulCarriersNull_get(self) -> repcap.UlCarriersNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def clone(self) -> 'Ulca':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ulca(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
