from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class T2Dvb:
	"""T2Dvb commands group definition. 117 total commands, 15 Subgroups, 18 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("t2Dvb", core, parent)

	@property
	def bandwidth(self):
		"""bandwidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bandwidth'):
			from .Bandwidth import Bandwidth
			self._bandwidth = Bandwidth(self._core, self._cmd_group)
		return self._bandwidth

	@property
	def channel(self):
		"""channel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_channel'):
			from .Channel import Channel
			self._channel = Channel(self._core, self._cmd_group)
		return self._channel

	@property
	def delay(self):
		"""delay commands group. 1 Sub-classes, 6 commands."""
		if not hasattr(self, '_delay'):
			from .Delay import Delay
			self._delay = Delay(self._core, self._cmd_group)
		return self._delay

	@property
	def fef(self):
		"""fef commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_fef'):
			from .Fef import Fef
			self._fef = Fef(self._core, self._cmd_group)
		return self._fef

	@property
	def fft(self):
		"""fft commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fft'):
			from .Fft import Fft
			self._fft = Fft(self._core, self._cmd_group)
		return self._fft

	@property
	def guard(self):
		"""guard commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_guard'):
			from .Guard import Guard
			self._guard = Guard(self._core, self._cmd_group)
		return self._guard

	@property
	def id(self):
		"""id commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_id'):
			from .Id import Id
			self._id = Id(self._core, self._cmd_group)
		return self._id

	@property
	def info(self):
		"""info commands group. 0 Sub-classes, 12 commands."""
		if not hasattr(self, '_info'):
			from .Info import Info
			self._info = Info(self._core, self._cmd_group)
		return self._info

	@property
	def inputPy(self):
		"""inputPy commands group. 1 Sub-classes, 4 commands."""
		if not hasattr(self, '_inputPy'):
			from .InputPy import InputPy
			self._inputPy = InputPy(self._core, self._cmd_group)
		return self._inputPy

	@property
	def lpy(self):
		"""lpy commands group. 1 Sub-classes, 6 commands."""
		if not hasattr(self, '_lpy'):
			from .Lpy import Lpy
			self._lpy = Lpy(self._core, self._cmd_group)
		return self._lpy

	@property
	def miso(self):
		"""miso commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_miso'):
			from .Miso import Miso
			self._miso = Miso(self._core, self._cmd_group)
		return self._miso

	@property
	def plp(self):
		"""plp commands group. 21 Sub-classes, 0 commands."""
		if not hasattr(self, '_plp'):
			from .Plp import Plp
			self._plp = Plp(self._core, self._cmd_group)
		return self._plp

	@property
	def prbs(self):
		"""prbs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_prbs'):
			from .Prbs import Prbs
			self._prbs = Prbs(self._core, self._cmd_group)
		return self._prbs

	@property
	def setting(self):
		"""setting commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_setting'):
			from .Setting import Setting
			self._setting = Setting(self._core, self._cmd_group)
		return self._setting

	@property
	def used(self):
		"""used commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_used'):
			from .Used import Used
			self._used = Used(self._core, self._cmd_group)
		return self._used

	def get_ldata(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:LDATa \n
		Snippet: value: int = driver.source.bb.t2Dvb.get_ldata() \n
		Sets the number of data symbols per T2 frame. \n
			:return: data_symbols: integer Range: 0 to 4095
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:LDATa?')
		return Conversions.str_to_int(response)

	def set_ldata(self, data_symbols: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:LDATa \n
		Snippet: driver.source.bb.t2Dvb.set_ldata(data_symbols = 1) \n
		Sets the number of data symbols per T2 frame. \n
			:param data_symbols: integer Range: 0 to 4095
		"""
		param = Conversions.decimal_value_to_str(data_symbols)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:LDATa {param}')

	def get_lf(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:LF \n
		Snippet: value: int = driver.source.bb.t2Dvb.get_lf() \n
		Queries the computed number of OFDM symbols per T2 frame. \n
			:return: ofdm_symbols: integer Range: 0 to 4095
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:LF?')
		return Conversions.str_to_int(response)

	def get_naux(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:NAUX \n
		Snippet: value: int = driver.source.bb.t2Dvb.get_naux() \n
		Queries the number of auxiliary streams. The current firmware does not support auxiliary streams. \n
			:return: num_aux_str: integer 0 Fixed response of the query.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:NAUX?')
		return Conversions.str_to_int(response)

	def set_naux(self, num_aux_str: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:NAUX \n
		Snippet: driver.source.bb.t2Dvb.set_naux(num_aux_str = 1) \n
		Queries the number of auxiliary streams. The current firmware does not support auxiliary streams. \n
			:param num_aux_str: integer 0 Fixed response of the query.
		"""
		param = Conversions.decimal_value_to_str(num_aux_str)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:NAUX {param}')

	# noinspection PyTypeChecker
	def get_network_mode(self) -> enums.EnetworkMode:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:NETWorkmode \n
		Snippet: value: enums.EnetworkMode = driver.source.bb.t2Dvb.get_network_mode() \n
		Sets the network mode. \n
			:return: network_mode: MFN| SFN
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:NETWorkmode?')
		return Conversions.str_to_scalar_enum(response, enums.EnetworkMode)

	def set_network_mode(self, network_mode: enums.EnetworkMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:NETWorkmode \n
		Snippet: driver.source.bb.t2Dvb.set_network_mode(network_mode = enums.EnetworkMode.MFN) \n
		Sets the network mode. \n
			:param network_mode: MFN| SFN
		"""
		param = Conversions.enum_scalar_to_str(network_mode, enums.EnetworkMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:NETWorkmode {param}')

	def get_nsub(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:NSUB \n
		Snippet: value: int = driver.source.bb.t2Dvb.get_nsub() \n
		Sets the number of subslices per T2 frame. The number of subslices is '1' for 'T2-MI Interface > Off'. \n
			:return: subslices: integer Range: 0 to 32767
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:NSUB?')
		return Conversions.str_to_int(response)

	def set_nsub(self, subslices: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:NSUB \n
		Snippet: driver.source.bb.t2Dvb.set_nsub(subslices = 1) \n
		Sets the number of subslices per T2 frame. The number of subslices is '1' for 'T2-MI Interface > Off'. \n
			:param subslices: integer Range: 0 to 32767
		"""
		param = Conversions.decimal_value_to_str(subslices)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:NSUB {param}')

	def get_nt_2_frames(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:NT2Frames \n
		Snippet: value: int = driver.source.bb.t2Dvb.get_nt_2_frames() \n
		Sets the number of T2 frames per super frame. \n
			:return: nt_2_frames: integer Range: 2 to 255
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:NT2Frames?')
		return Conversions.str_to_int(response)

	def set_nt_2_frames(self, nt_2_frames: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:NT2Frames \n
		Snippet: driver.source.bb.t2Dvb.set_nt_2_frames(nt_2_frames = 1) \n
		Sets the number of T2 frames per super frame. \n
			:param nt_2_frames: integer Range: 2 to 255
		"""
		param = Conversions.decimal_value_to_str(nt_2_frames)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:NT2Frames {param}')

	# noinspection PyTypeChecker
	def get_papr(self) -> enums.T2SystemPapr:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PAPR \n
		Snippet: value: enums.T2SystemPapr = driver.source.bb.t2Dvb.get_papr() \n
		Sets the technique to reduce the peak to average power ratio. \n
			:return: papr: OFF| TR
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:PAPR?')
		return Conversions.str_to_scalar_enum(response, enums.T2SystemPapr)

	def set_papr(self, papr: enums.T2SystemPapr) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PAPR \n
		Snippet: driver.source.bb.t2Dvb.set_papr(papr = enums.T2SystemPapr.OFF) \n
		Sets the technique to reduce the peak to average power ratio. \n
			:param papr: OFF| TR
		"""
		param = Conversions.enum_scalar_to_str(papr, enums.T2SystemPapr)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:PAPR {param}')

	# noinspection PyTypeChecker
	def get_payload(self) -> enums.PayloadTestStuff:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PAYLoad \n
		Snippet: value: enums.PayloadTestStuff = driver.source.bb.t2Dvb.get_payload() \n
		Defines the payload area content of the packet. \n
			:return: payload: PRBS| H00| HFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:PAYLoad?')
		return Conversions.str_to_scalar_enum(response, enums.PayloadTestStuff)

	def set_payload(self, payload: enums.PayloadTestStuff) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PAYLoad \n
		Snippet: driver.source.bb.t2Dvb.set_payload(payload = enums.PayloadTestStuff.H00) \n
		Defines the payload area content of the packet. \n
			:param payload: PRBS| H00| HFF
		"""
		param = Conversions.enum_scalar_to_str(payload, enums.PayloadTestStuff)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:PAYLoad {param}')

	def get_pid(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PID \n
		Snippet: value: int = driver.source.bb.t2Dvb.get_pid() \n
		Sets the . \n
			:return: pid: integer Range: 0 to 8191
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:PID?')
		return Conversions.str_to_int(response)

	def set_pid(self, pid: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PID \n
		Snippet: driver.source.bb.t2Dvb.set_pid(pid = 1) \n
		Sets the . \n
			:param pid: integer Range: 0 to 8191
		"""
		param = Conversions.decimal_value_to_str(pid)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:PID {param}')

	# noinspection PyTypeChecker
	def get_pid_test_pack(self) -> enums.PidTestPacket:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PIDTestpack \n
		Snippet: value: enums.PidTestPacket = driver.source.bb.t2Dvb.get_pid_test_pack() \n
		If a header is present in the test packet ('Test TS Packet > Head/184 Payload') , you can specify a fixed or variable
		packet identifier (PID) . \n
			:return: pid_ts_packet: NULL| VARiable
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:PIDTestpack?')
		return Conversions.str_to_scalar_enum(response, enums.PidTestPacket)

	def set_pid_test_pack(self, pid_ts_packet: enums.PidTestPacket) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PIDTestpack \n
		Snippet: driver.source.bb.t2Dvb.set_pid_test_pack(pid_ts_packet = enums.PidTestPacket.NULL) \n
		If a header is present in the test packet ('Test TS Packet > Head/184 Payload') , you can specify a fixed or variable
		packet identifier (PID) . \n
			:param pid_ts_packet: NULL| VARiable
		"""
		param = Conversions.enum_scalar_to_str(pid_ts_packet, enums.PidTestPacket)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:PIDTestpack {param}')

	# noinspection PyTypeChecker
	def get_pilot(self) -> enums.Dvbt2FramingPilotPattern:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PILot \n
		Snippet: value: enums.Dvbt2FramingPilotPattern = driver.source.bb.t2Dvb.get_pilot() \n
		Sets the pilot pattern. \n
			:return: pilot_pattern: PP1| PP2| PP3| PP4| PP5| PP6| PP7| PP8
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:PILot?')
		return Conversions.str_to_scalar_enum(response, enums.Dvbt2FramingPilotPattern)

	def set_pilot(self, pilot_pattern: enums.Dvbt2FramingPilotPattern) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PILot \n
		Snippet: driver.source.bb.t2Dvb.set_pilot(pilot_pattern = enums.Dvbt2FramingPilotPattern.PP1) \n
		Sets the pilot pattern. \n
			:param pilot_pattern: PP1| PP2| PP3| PP4| PP5| PP6| PP7| PP8
		"""
		param = Conversions.enum_scalar_to_str(pilot_pattern, enums.Dvbt2FramingPilotPattern)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:PILot {param}')

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PRESet \n
		Snippet: driver.source.bb.t2Dvb.preset() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:T2DVb:STATe. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PRESet \n
		Snippet: driver.source.bb.t2Dvb.preset_with_opc() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:T2DVb:STATe. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmcv.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:T2DVb:PRESet', opc_timeout_ms)

	# noinspection PyTypeChecker
	def get_profile(self) -> enums.Dvbt2T2SystemProfileMode:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PROFile \n
		Snippet: value: enums.Dvbt2T2SystemProfileMode = driver.source.bb.t2Dvb.get_profile() \n
		Sets the profile mode. Mutes P1FEF, if the modulator operates in a multi profile environment and is used to generate a RF
		combined T2Base/T2Lite composite signal. \n
			:return: profile_mode: SINGLE| MULTI
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:PROFile?')
		return Conversions.str_to_scalar_enum(response, enums.Dvbt2T2SystemProfileMode)

	def set_profile(self, profile_mode: enums.Dvbt2T2SystemProfileMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PROFile \n
		Snippet: driver.source.bb.t2Dvb.set_profile(profile_mode = enums.Dvbt2T2SystemProfileMode.MULTI) \n
		Sets the profile mode. Mutes P1FEF, if the modulator operates in a multi profile environment and is used to generate a RF
		combined T2Base/T2Lite composite signal. \n
			:param profile_mode: SINGLE| MULTI
		"""
		param = Conversions.enum_scalar_to_str(profile_mode, enums.Dvbt2T2SystemProfileMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:PROFile {param}')

	# noinspection PyTypeChecker
	def get_source(self) -> enums.CodingInputSignalSource:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:SOURce \n
		Snippet: value: enums.CodingInputSignalSource = driver.source.bb.t2Dvb.get_source() \n
		Sets the modulation source for the input signal. \n
			:return: dvbt_2_source: EXTernal| TSPLayer| TESTsignal
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.CodingInputSignalSource)

	def set_source(self, dvbt_2_source: enums.CodingInputSignalSource) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:SOURce \n
		Snippet: driver.source.bb.t2Dvb.set_source(dvbt_2_source = enums.CodingInputSignalSource.EXTernal) \n
		Sets the modulation source for the input signal. \n
			:param dvbt_2_source: EXTernal| TSPLayer| TESTsignal
		"""
		param = Conversions.enum_scalar_to_str(dvbt_2_source, enums.CodingInputSignalSource)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:SOURce {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:STATe \n
		Snippet: value: bool = driver.source.bb.t2Dvb.get_state() \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:STATe \n
		Snippet: driver.source.bb.t2Dvb.set_state(state = False) \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:STATe {param}')

	# noinspection PyTypeChecker
	def get_tfs(self) -> enums.SystemPostExtension:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:TFS \n
		Snippet: value: enums.SystemPostExtension = driver.source.bb.t2Dvb.get_tfs() \n
		Queries the state. The current firmware does not support TFS. \n
			:return: tfs: OFF OFF Fixed response of the query.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:TFS?')
		return Conversions.str_to_scalar_enum(response, enums.SystemPostExtension)

	def set_tfs(self, tfs: enums.SystemPostExtension) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:TFS \n
		Snippet: driver.source.bb.t2Dvb.set_tfs(tfs = enums.SystemPostExtension.OFF) \n
		Queries the state. The current firmware does not support TFS. \n
			:param tfs: OFF OFF Fixed response of the query.
		"""
		param = Conversions.enum_scalar_to_str(tfs, enums.SystemPostExtension)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:TFS {param}')

	# noinspection PyTypeChecker
	def get_ts_packet(self) -> enums.SettingsTestTsPacket:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:TSPacket \n
		Snippet: value: enums.SettingsTestTsPacket = driver.source.bb.t2Dvb.get_ts_packet() \n
		Specifies the structure of the test transport stream packet that is fed to the modulator. \n
			:return: ts_packet: H184| S187
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:TSPacket?')
		return Conversions.str_to_scalar_enum(response, enums.SettingsTestTsPacket)

	def set_ts_packet(self, ts_packet: enums.SettingsTestTsPacket) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:TSPacket \n
		Snippet: driver.source.bb.t2Dvb.set_ts_packet(ts_packet = enums.SettingsTestTsPacket.H184) \n
		Specifies the structure of the test transport stream packet that is fed to the modulator. \n
			:param ts_packet: H184| S187
		"""
		param = Conversions.enum_scalar_to_str(ts_packet, enums.SettingsTestTsPacket)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:TSPacket {param}')

	# noinspection PyTypeChecker
	def get_txsys(self) -> enums.Dvbt2Transmission:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:TXSYs \n
		Snippet: value: enums.Dvbt2Transmission = driver.source.bb.t2Dvb.get_txsys() \n
		Sets the transmission system. \n
			:return: transmission_sys: T2LM| T2LS| NONT2| MISO| SISO T2LM T2 Lite T2LS T2 Lite NONT2 Non-T2 MISO MISO SISO SISO
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:TXSYs?')
		return Conversions.str_to_scalar_enum(response, enums.Dvbt2Transmission)

	def set_txsys(self, transmission_sys: enums.Dvbt2Transmission) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:TXSYs \n
		Snippet: driver.source.bb.t2Dvb.set_txsys(transmission_sys = enums.Dvbt2Transmission.MISO) \n
		Sets the transmission system. \n
			:param transmission_sys: T2LM| T2LS| NONT2| MISO| SISO T2LM T2 Lite T2LS T2 Lite NONT2 Non-T2 MISO MISO SISO SISO
		"""
		param = Conversions.enum_scalar_to_str(transmission_sys, enums.Dvbt2Transmission)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:TXSYs {param}')

	def clone(self) -> 'T2Dvb':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = T2Dvb(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
