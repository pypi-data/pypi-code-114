from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Monitor:
	"""Monitor commands group definition. 39 total commands, 1 Subgroups, 0 group commands
	Repeated Capability: MonitorPane, default value after init: MonitorPane.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("monitor", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_monitorPane_get', 'repcap_monitorPane_set', repcap.MonitorPane.Nr1)

	def repcap_monitorPane_set(self, monitorPane: repcap.MonitorPane) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to MonitorPane.Default
		Default value after init: MonitorPane.Nr1"""
		self._cmd_group.set_repcap_enum_value(monitorPane)

	def repcap_monitorPane_get(self) -> repcap.MonitorPane:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def display(self):
		"""display commands group. 8 Sub-classes, 1 commands."""
		if not hasattr(self, '_display'):
			from .Display import Display
			self._display = Display(self._core, self._cmd_group)
		return self._display

	def clone(self) -> 'Monitor':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Monitor(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
