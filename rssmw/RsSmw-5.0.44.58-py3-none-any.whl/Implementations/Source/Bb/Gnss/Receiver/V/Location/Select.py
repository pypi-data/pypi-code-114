from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, location: str, vehicle=repcap.Vehicle.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:LOCation:[SELect] \n
		Snippet: driver.source.bb.gnss.receiver.v.location.select.set(location = '1', vehicle = repcap.Vehicle.Default) \n
		Selects the geographic location of the GNSS receiver. \n
			:param location: string User Defined Enables the definition of the 'Latitude', 'Longitude' and 'Altitude' of the GNSS receiver with fixed position in the ECEF WGS84 coordinate system. 'City' Selects one of the predefined fixed geographic locations, see Table 'Coordinates of the simulated predefined positions'. The parameters latitude, longitude and altitude are set according to the selected position.
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
		"""
		param = Conversions.value_to_quoted_str(location)
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:LOCation:SELect {param}')

	def get(self, vehicle=repcap.Vehicle.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:LOCation:[SELect] \n
		Snippet: value: str = driver.source.bb.gnss.receiver.v.location.select.get(vehicle = repcap.Vehicle.Default) \n
		Selects the geographic location of the GNSS receiver. \n
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
			:return: location: string User Defined Enables the definition of the 'Latitude', 'Longitude' and 'Altitude' of the GNSS receiver with fixed position in the ECEF WGS84 coordinate system. 'City' Selects one of the predefined fixed geographic locations, see Table 'Coordinates of the simulated predefined positions'. The parameters latitude, longitude and altitude are set according to the selected position."""
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:LOCation:SELect?')
		return trim_str_response(response)
