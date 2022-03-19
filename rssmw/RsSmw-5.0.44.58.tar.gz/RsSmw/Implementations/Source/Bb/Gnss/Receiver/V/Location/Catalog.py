from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Catalog:
	"""Catalog commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("catalog", core, parent)

	def set(self, gnss_location_names: List[str], vehicle=repcap.Vehicle.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:LOCation:CATalog \n
		Snippet: driver.source.bb.gnss.receiver.v.location.catalog.set(gnss_location_names = ['1', '2', '3'], vehicle = repcap.Vehicle.Default) \n
		Queries the names of the predefined geographic locations. \n
			:param gnss_location_names: No help available
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
		"""
		param = Conversions.list_to_csv_quoted_str(gnss_location_names)
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:LOCation:CATalog {param}')

	def get(self, vehicle=repcap.Vehicle.Default) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:LOCation:CATalog \n
		Snippet: value: List[str] = driver.source.bb.gnss.receiver.v.location.catalog.get(vehicle = repcap.Vehicle.Default) \n
		Queries the names of the predefined geographic locations. \n
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
			:return: gnss_location_names: No help available"""
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:LOCation:CATalog?')
		return Conversions.str_to_str_list(response)
