from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Utilities import trim_str_response
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class File:
	"""File commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("file", core, parent)

	def set(self, filename: str, vehicle=repcap.Vehicle.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:LOCation:VEHicle:FILE \n
		Snippet: driver.source.bb.gnss.receiver.v.location.vehicle.file.set(filename = '1', vehicle = repcap.Vehicle.Default) \n
		Selects a predefined or user-defined vehicle description (*.xvd) file. \n
			:param filename: Filename or complete file path; file extension is optional Query the existing files with: [:SOURcehw]:BB:GNSS:VEHicle:CATalog:PREDefined? [:SOURcehw]:BB:GNSS:VEHicle:CATalog:USER?
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
		"""
		param = Conversions.value_to_quoted_str(filename)
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:LOCation:VEHicle:FILE {param}')

	def get(self, vehicle=repcap.Vehicle.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:LOCation:VEHicle:FILE \n
		Snippet: value: str = driver.source.bb.gnss.receiver.v.location.vehicle.file.get(vehicle = repcap.Vehicle.Default) \n
		Selects a predefined or user-defined vehicle description (*.xvd) file. \n
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
			:return: filename: Filename or complete file path; file extension is optional Query the existing files with: [:SOURcehw]:BB:GNSS:VEHicle:CATalog:PREDefined? [:SOURcehw]:BB:GNSS:VEHicle:CATalog:USER?"""
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:LOCation:VEHicle:FILE?')
		return trim_str_response(response)
