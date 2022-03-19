from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RoMode:
	"""RoMode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("roMode", core, parent)

	def set(self, ro_mode: enums.ReadOutMode, vehicle=repcap.Vehicle.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:LOCation:WAYPoints:ROMode \n
		Snippet: driver.source.bb.gnss.receiver.v.location.waypoints.roMode.set(ro_mode = enums.ReadOutMode.CYCLic, vehicle = repcap.Vehicle.Default) \n
		Defines the way the waypoint/attitude file is processed. \n
			:param ro_mode: CYCLic| RTRip| OWAY
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
		"""
		param = Conversions.enum_scalar_to_str(ro_mode, enums.ReadOutMode)
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:LOCation:WAYPoints:ROMode {param}')

	# noinspection PyTypeChecker
	def get(self, vehicle=repcap.Vehicle.Default) -> enums.ReadOutMode:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:LOCation:WAYPoints:ROMode \n
		Snippet: value: enums.ReadOutMode = driver.source.bb.gnss.receiver.v.location.waypoints.roMode.get(vehicle = repcap.Vehicle.Default) \n
		Defines the way the waypoint/attitude file is processed. \n
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
			:return: ro_mode: CYCLic| RTRip| OWAY"""
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:LOCation:WAYPoints:ROMode?')
		return Conversions.str_to_scalar_enum(response, enums.ReadOutMode)
