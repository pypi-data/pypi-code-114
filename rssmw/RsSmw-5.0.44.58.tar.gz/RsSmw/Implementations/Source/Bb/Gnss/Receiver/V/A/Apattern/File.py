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

	def set(self, filename: str, vehicle=repcap.Vehicle.Default, antenna=repcap.Antenna.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:A<CH>:APATtern:FILE \n
		Snippet: driver.source.bb.gnss.receiver.v.a.apattern.file.set(filename = '1', vehicle = repcap.Vehicle.Default, antenna = repcap.Antenna.Default) \n
		Loads the selected file from the default or the specified directory. Loaded are files with extension *.ant_pat/*.
		body_mask. Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in
		the default and in a specific directory. \n
			:param filename: 'filename' Filename or complete file path; file extension can be omitted. Query the existing files with the following commands: [:SOURcehw]:BB:GNSS:APATtern:CATalog:PREDefined? [:SOURcehw]:BB:GNSS:APATtern:CATalog:USER?
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'A')
		"""
		param = Conversions.value_to_quoted_str(filename)
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:A{antenna_cmd_val}:APATtern:FILE {param}')

	def get(self, vehicle=repcap.Vehicle.Default, antenna=repcap.Antenna.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:A<CH>:APATtern:FILE \n
		Snippet: value: str = driver.source.bb.gnss.receiver.v.a.apattern.file.get(vehicle = repcap.Vehicle.Default, antenna = repcap.Antenna.Default) \n
		Loads the selected file from the default or the specified directory. Loaded are files with extension *.ant_pat/*.
		body_mask. Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in
		the default and in a specific directory. \n
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'A')
			:return: filename: 'filename' Filename or complete file path; file extension can be omitted. Query the existing files with the following commands: [:SOURcehw]:BB:GNSS:APATtern:CATalog:PREDefined? [:SOURcehw]:BB:GNSS:APATtern:CATalog:USER?"""
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:A{antenna_cmd_val}:APATtern:FILE?')
		return trim_str_response(response)
