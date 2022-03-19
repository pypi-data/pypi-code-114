from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Insert:
	"""Insert commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("insert", core, parent)

	def set(self, vehicle=repcap.Vehicle.Default, obscuredArea=repcap.ObscuredArea.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:ENVironment:FULL:AREA<CH>:INSert \n
		Snippet: driver.source.bb.gnss.receiver.v.environment.full.area.insert.set(vehicle = repcap.Vehicle.Default, obscuredArea = repcap.ObscuredArea.Default) \n
		Appends, insertes or deletes an obscured zone. \n
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
			:param obscuredArea: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Area')
		"""
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		obscuredArea_cmd_val = self._cmd_group.get_repcap_cmd_value(obscuredArea, repcap.ObscuredArea)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:ENVironment:FULL:AREA{obscuredArea_cmd_val}:INSert')

	def set_with_opc(self, vehicle=repcap.Vehicle.Default, obscuredArea=repcap.ObscuredArea.Default, opc_timeout_ms: int = -1) -> None:
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		obscuredArea_cmd_val = self._cmd_group.get_repcap_cmd_value(obscuredArea, repcap.ObscuredArea)
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:ENVironment:FULL:AREA<CH>:INSert \n
		Snippet: driver.source.bb.gnss.receiver.v.environment.full.area.insert.set_with_opc(vehicle = repcap.Vehicle.Default, obscuredArea = repcap.ObscuredArea.Default) \n
		Appends, insertes or deletes an obscured zone. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
			:param obscuredArea: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Area')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:ENVironment:FULL:AREA{obscuredArea_cmd_val}:INSert', opc_timeout_ms)
