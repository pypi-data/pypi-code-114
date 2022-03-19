from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal.RepeatedCapability import RepeatedCapability
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Area:
	"""Area commands group definition. 6 total commands, 5 Subgroups, 1 group commands
	Repeated Capability: ObscuredArea, default value after init: ObscuredArea.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("area", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_obscuredArea_get', 'repcap_obscuredArea_set', repcap.ObscuredArea.Nr1)

	def repcap_obscuredArea_set(self, obscuredArea: repcap.ObscuredArea) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to ObscuredArea.Default
		Default value after init: ObscuredArea.Nr1"""
		self._cmd_group.set_repcap_enum_value(obscuredArea)

	def repcap_obscuredArea_get(self) -> repcap.ObscuredArea:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def append(self):
		"""append commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_append'):
			from .Append import Append
			self._append = Append(self._core, self._cmd_group)
		return self._append

	@property
	def count(self):
		"""count commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_count'):
			from .Count import Count
			self._count = Count(self._core, self._cmd_group)
		return self._count

	@property
	def insert(self):
		"""insert commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_insert'):
			from .Insert import Insert
			self._insert = Insert(self._core, self._cmd_group)
		return self._insert

	@property
	def length(self):
		"""length commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_length'):
			from .Length import Length
			self._length = Length(self._core, self._cmd_group)
		return self._length

	@property
	def reference(self):
		"""reference commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_reference'):
			from .Reference import Reference
			self._reference = Reference(self._core, self._cmd_group)
		return self._reference

	def delete(self, vehicle=repcap.Vehicle.Default, obscuredArea=repcap.ObscuredArea.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:ENVironment:FULL:AREA<CH>:DELete \n
		Snippet: driver.source.bb.gnss.receiver.v.environment.full.area.delete(vehicle = repcap.Vehicle.Default, obscuredArea = repcap.ObscuredArea.Default) \n
		Appends, insertes or deletes an obscured zone. \n
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
			:param obscuredArea: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Area')
		"""
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		obscuredArea_cmd_val = self._cmd_group.get_repcap_cmd_value(obscuredArea, repcap.ObscuredArea)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:ENVironment:FULL:AREA{obscuredArea_cmd_val}:DELete')

	def delete_with_opc(self, vehicle=repcap.Vehicle.Default, obscuredArea=repcap.ObscuredArea.Default, opc_timeout_ms: int = -1) -> None:
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		obscuredArea_cmd_val = self._cmd_group.get_repcap_cmd_value(obscuredArea, repcap.ObscuredArea)
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:ENVironment:FULL:AREA<CH>:DELete \n
		Snippet: driver.source.bb.gnss.receiver.v.environment.full.area.delete_with_opc(vehicle = repcap.Vehicle.Default, obscuredArea = repcap.ObscuredArea.Default) \n
		Appends, insertes or deletes an obscured zone. \n
		Same as delete, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
			:param obscuredArea: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Area')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:ENVironment:FULL:AREA{obscuredArea_cmd_val}:DELete', opc_timeout_ms)

	def clone(self) -> 'Area':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Area(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
