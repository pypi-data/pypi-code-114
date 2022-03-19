from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Service:
	"""Service commands group definition. 2 total commands, 2 Subgroups, 0 group commands
	Repeated Capability: ServiceListTable, default value after init: ServiceListTable.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("service", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_serviceListTable_get', 'repcap_serviceListTable_set', repcap.ServiceListTable.Nr1)

	def repcap_serviceListTable_set(self, serviceListTable: repcap.ServiceListTable) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to ServiceListTable.Default
		Default value after init: ServiceListTable.Nr1"""
		self._cmd_group.set_repcap_enum_value(serviceListTable)

	def repcap_serviceListTable_get(self) -> repcap.ServiceListTable:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def aattributes(self):
		"""aattributes commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aattributes'):
			from .Aattributes import Aattributes
			self._aattributes = Aattributes(self._core, self._cmd_group)
		return self._aattributes

	@property
	def snumber(self):
		"""snumber commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_snumber'):
			from .Snumber import Snumber
			self._snumber = Snumber(self._core, self._cmd_group)
		return self._snumber

	def clone(self) -> 'Service':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Service(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
