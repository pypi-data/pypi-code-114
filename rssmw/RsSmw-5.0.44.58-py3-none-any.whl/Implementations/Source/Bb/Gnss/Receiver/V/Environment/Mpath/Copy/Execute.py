from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Execute:
	"""Execute commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("execute", core, parent)

	def set(self, vehicle=repcap.Vehicle.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:ENVironment:MPATh:COPY:EXECute \n
		Snippet: driver.source.bb.gnss.receiver.v.environment.mpath.copy.execute.set(vehicle = repcap.Vehicle.Default) \n
		Copies the multipath configuration of the source GNSS System and SV ID to the target SV ID and GNSS system or to all SV
		IDs from a system.
			INTRO_CMD_HELP: Set the source with: \n
			- [:SOURce<hw>]:BB:GNSS:RECeiver[:V<st>]:ENVironment:MPATh:SYSTem
			- [:SOURce<hw>]:BB:GNSS:RECeiver[:V<st>]:ENVironment:MPATh:SVID
			INTRO_CMD_HELP: Set the target with: \n
			- [:SOURce<hw>]:BB:GNSS:RECeiver[:V<st>]:ENVironment:MPATh:COPY:SYSTem
			- [:SOURce<hw>]:BB:GNSS:RECeiver[:V<st>]:ENVironment:MPATh:COPY:SVID \n
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
		"""
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:ENVironment:MPATh:COPY:EXECute')

	def set_with_opc(self, vehicle=repcap.Vehicle.Default, opc_timeout_ms: int = -1) -> None:
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:ENVironment:MPATh:COPY:EXECute \n
		Snippet: driver.source.bb.gnss.receiver.v.environment.mpath.copy.execute.set_with_opc(vehicle = repcap.Vehicle.Default) \n
		Copies the multipath configuration of the source GNSS System and SV ID to the target SV ID and GNSS system or to all SV
		IDs from a system.
			INTRO_CMD_HELP: Set the source with: \n
			- [:SOURce<hw>]:BB:GNSS:RECeiver[:V<st>]:ENVironment:MPATh:SYSTem
			- [:SOURce<hw>]:BB:GNSS:RECeiver[:V<st>]:ENVironment:MPATh:SVID
			INTRO_CMD_HELP: Set the target with: \n
			- [:SOURce<hw>]:BB:GNSS:RECeiver[:V<st>]:ENVironment:MPATh:COPY:SYSTem
			- [:SOURce<hw>]:BB:GNSS:RECeiver[:V<st>]:ENVironment:MPATh:COPY:SVID \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:ENVironment:MPATh:COPY:EXECute', opc_timeout_ms)
