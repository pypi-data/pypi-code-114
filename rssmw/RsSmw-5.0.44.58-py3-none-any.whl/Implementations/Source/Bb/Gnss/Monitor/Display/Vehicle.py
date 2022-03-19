from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Vehicle:
	"""Vehicle commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("vehicle", core, parent)

	def set(self, vehicle: enums.RefVehicle, monitorPane=repcap.MonitorPane.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:MONitor<CH>:DISPlay:VEHicle \n
		Snippet: driver.source.bb.gnss.monitor.display.vehicle.set(vehicle = enums.RefVehicle.V1, monitorPane = repcap.MonitorPane.Default) \n
		Sets the vehicle for that the information displayed in the 'Simulation Monitor' applies. \n
			:param vehicle: V1| V2
			:param monitorPane: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Monitor')
		"""
		param = Conversions.enum_scalar_to_str(vehicle, enums.RefVehicle)
		monitorPane_cmd_val = self._cmd_group.get_repcap_cmd_value(monitorPane, repcap.MonitorPane)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:MONitor{monitorPane_cmd_val}:DISPlay:VEHicle {param}')

	# noinspection PyTypeChecker
	def get(self, monitorPane=repcap.MonitorPane.Default) -> enums.RefVehicle:
		"""SCPI: [SOURce<HW>]:BB:GNSS:MONitor<CH>:DISPlay:VEHicle \n
		Snippet: value: enums.RefVehicle = driver.source.bb.gnss.monitor.display.vehicle.get(monitorPane = repcap.MonitorPane.Default) \n
		Sets the vehicle for that the information displayed in the 'Simulation Monitor' applies. \n
			:param monitorPane: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Monitor')
			:return: vehicle: V1| V2"""
		monitorPane_cmd_val = self._cmd_group.get_repcap_cmd_value(monitorPane, repcap.MonitorPane)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:MONitor{monitorPane_cmd_val}:DISPlay:VEHicle?')
		return Conversions.str_to_scalar_enum(response, enums.RefVehicle)
