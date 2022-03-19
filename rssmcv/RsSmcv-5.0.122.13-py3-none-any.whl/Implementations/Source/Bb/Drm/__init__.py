from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Drm:
	"""Drm commands group definition. 24 total commands, 3 Subgroups, 12 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("drm", core, parent)

	@property
	def msc(self):
		"""msc commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_msc'):
			from .Msc import Msc
			self._msc = Msc(self._core, self._cmd_group)
		return self._msc

	@property
	def sdc(self):
		"""sdc commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_sdc'):
			from .Sdc import Sdc
			self._sdc = Sdc(self._core, self._cmd_group)
		return self._sdc

	@property
	def setting(self):
		"""setting commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_setting'):
			from .Setting import Setting
			self._setting = Setting(self._core, self._cmd_group)
		return self._setting

	# noinspection PyTypeChecker
	def get_bandwidth(self) -> enums.DrmCodingChannelBw:
		"""SCPI: [SOURce<HW>]:BB:DRM:BANDwidth \n
		Snippet: value: enums.DrmCodingChannelBw = driver.source.bb.drm.get_bandwidth() \n
		Queries the channel bandwidth. \n
			:return: drm_bandwidth: K045| K05| K09| K10| K18| K20| K100| INV K045 4.5 kHz K05 5 kHz K09 9 kHz K10 10 kHz K18 18 kHz K20 20 kHz K100 100 kHz INV Invalid channel bandwidth
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DRM:BANDwidth?')
		return Conversions.str_to_scalar_enum(response, enums.DrmCodingChannelBw)

	def get_filename(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:DRM:FILename \n
		Snippet: value: str = driver.source.bb.drm.get_filename() \n
		Loads the specified file. Refer to 'Accessing Files in the Default or Specified Directory' for general information on
		file handling in the default and in a specific directory. \n
			:return: drm_dcp_file: string Filename or complete file path; file extension (*.dcp) can be omitted.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DRM:FILename?')
		return trim_str_response(response)

	def set_filename(self, drm_dcp_file: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:DRM:FILename \n
		Snippet: driver.source.bb.drm.set_filename(drm_dcp_file = '1') \n
		Loads the specified file. Refer to 'Accessing Files in the Default or Specified Directory' for general information on
		file handling in the default and in a specific directory. \n
			:param drm_dcp_file: string Filename or complete file path; file extension (*.dcp) can be omitted.
		"""
		param = Conversions.value_to_quoted_str(drm_dcp_file)
		self._core.io.write(f'SOURce<HwInstance>:BB:DRM:FILename {param}')

	# noinspection PyTypeChecker
	def get_interleaver(self) -> enums.DrmCodingInterleaver:
		"""SCPI: [SOURce<HW>]:BB:DRM:INTerleaver \n
		Snippet: value: enums.DrmCodingInterleaver = driver.source.bb.drm.get_interleaver() \n
		Queries the interleaver depth. \n
			:return: drm_interleaver: MS4| MS6| S2| INV MS4 400 ms MS6 600 ms S2 2 s INV Invalid interleaver depth
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DRM:INTerleaver?')
		return Conversions.str_to_scalar_enum(response, enums.DrmCodingInterleaver)

	def get_label(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:DRM:LABel \n
		Snippet: value: str = driver.source.bb.drm.get_label() \n
		Queries the label of the transmitted service. \n
			:return: drm_label: string Each service has a maximum length of 16 characters separated by br.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DRM:LABel?')
		return trim_str_response(response)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.DrmCodingRobustness:
		"""SCPI: [SOURce<HW>]:BB:DRM:MODE \n
		Snippet: value: enums.DrmCodingRobustness = driver.source.bb.drm.get_mode() \n
		Queries the robustness mode of the signal. \n
			:return: drm_mode: A| B| C| D| E| INV A|B|C|D|E Available robustness modes. INV Invalid mode.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DRM:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.DrmCodingRobustness)

	# noinspection PyTypeChecker
	def get_num_data(self) -> enums.DrmInputSignalServices:
		"""SCPI: [SOURce<HW>]:BB:DRM:NUMData \n
		Snippet: value: enums.DrmInputSignalServices = driver.source.bb.drm.get_num_data() \n
		Queries the number of data services contained in the input stream. \n
			:return: drm_num_data: 0| 1| 2| 3| 4| INV 0|1|2|3|4 Available number of data services INV Invalid number of data services
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DRM:NUMData?')
		return Conversions.str_to_scalar_enum(response, enums.DrmInputSignalServices)

	# noinspection PyTypeChecker
	def get_num_audio(self) -> enums.DrmInputSignalServices:
		"""SCPI: [SOURce<HW>]:BB:DRM:NUMaudio \n
		Snippet: value: enums.DrmInputSignalServices = driver.source.bb.drm.get_num_audio() \n
		Queries the number of audio services contained in the input stream. \n
			:return: drm_num_audio: 0| 1| 2| 3| 4| INV 0|1|2|3|4 Available number of audio services INV Invalid number of audio services
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DRM:NUMaudio?')
		return Conversions.str_to_scalar_enum(response, enums.DrmInputSignalServices)

	def get_port(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DRM:PORT \n
		Snippet: value: int = driver.source.bb.drm.get_port() \n
		Sets the port. Enter the port number on that the UDP/ receiver listens for UDP datagrams. \n
			:return: drm_port: integer Range: 0 to 65535
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DRM:PORT?')
		return Conversions.str_to_int(response)

	def set_port(self, drm_port: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:DRM:PORT \n
		Snippet: driver.source.bb.drm.set_port(drm_port = 1) \n
		Sets the port. Enter the port number on that the UDP/ receiver listens for UDP datagrams. \n
			:param drm_port: integer Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(drm_port)
		self._core.io.write(f'SOURce<HwInstance>:BB:DRM:PORT {param}')

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:DRM:PRESet \n
		Snippet: driver.source.bb.drm.preset() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:DRM:STATe. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:DRM:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:DRM:PRESet \n
		Snippet: driver.source.bb.drm.preset_with_opc() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:DRM:STATe. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmcv.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:DRM:PRESet', opc_timeout_ms)

	# noinspection PyTypeChecker
	def get_source(self) -> enums.DrmInputSignalSource:
		"""SCPI: [SOURce<HW>]:BB:DRM:SOURce \n
		Snippet: value: enums.DrmInputSignalSource = driver.source.bb.drm.get_source() \n
		Sets the modulation source for the input signal. \n
			:return: drm_source: EXTernal| FILE EXTernal Uses a / stream input at the 'LAN' connector of the host PC of the R&S SMCV100B. FILE Reads the input stream from a *.dcp file. The binary file contains the MDI data encapsulated in packets.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DRM:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.DrmInputSignalSource)

	def set_source(self, drm_source: enums.DrmInputSignalSource) -> None:
		"""SCPI: [SOURce<HW>]:BB:DRM:SOURce \n
		Snippet: driver.source.bb.drm.set_source(drm_source = enums.DrmInputSignalSource.EXTernal) \n
		Sets the modulation source for the input signal. \n
			:param drm_source: EXTernal| FILE EXTernal Uses a / stream input at the 'LAN' connector of the host PC of the R&S SMCV100B. FILE Reads the input stream from a *.dcp file. The binary file contains the MDI data encapsulated in packets.
		"""
		param = Conversions.enum_scalar_to_str(drm_source, enums.DrmInputSignalSource)
		self._core.io.write(f'SOURce<HwInstance>:BB:DRM:SOURce {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DRM:STATe \n
		Snippet: value: bool = driver.source.bb.drm.get_state() \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DRM:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DRM:STATe \n
		Snippet: driver.source.bb.drm.set_state(state = False) \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:DRM:STATe {param}')

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.DrmInputSignalLayerType:
		"""SCPI: [SOURce<HW>]:BB:DRM:TYPE \n
		Snippet: value: enums.DrmInputSignalLayerType = driver.source.bb.drm.get_type_py() \n
		Queries the type of audio in the transmission. \n
			:return: drm_layer_type: BASE| ENHancement| INV BASE Decodable by all DRM receivers. ENHancement Only decodable by receivers with appropriate capabilities. INV Invalid type
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DRM:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.DrmInputSignalLayerType)

	def clone(self) -> 'Drm':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Drm(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
