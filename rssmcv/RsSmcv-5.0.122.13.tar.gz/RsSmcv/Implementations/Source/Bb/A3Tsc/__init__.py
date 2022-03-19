from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class A3Tsc:
	"""A3Tsc commands group definition. 131 total commands, 14 Subgroups, 14 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("a3Tsc", core, parent)

	@property
	def channel(self):
		"""channel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_channel'):
			from .Channel import Channel
			self._channel = Channel(self._core, self._cmd_group)
		return self._channel

	@property
	def delay(self):
		"""delay commands group. 2 Sub-classes, 9 commands."""
		if not hasattr(self, '_delay'):
			from .Delay import Delay
			self._delay = Delay(self._core, self._cmd_group)
		return self._delay

	@property
	def frame(self):
		"""frame commands group. 2 Sub-classes, 5 commands."""
		if not hasattr(self, '_frame'):
			from .Frame import Frame
			self._frame = Frame(self._core, self._cmd_group)
		return self._frame

	@property
	def info(self):
		"""info commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_info'):
			from .Info import Info
			self._info = Info(self._core, self._cmd_group)
		return self._info

	@property
	def inputPy(self):
		"""inputPy commands group. 2 Sub-classes, 5 commands."""
		if not hasattr(self, '_inputPy'):
			from .InputPy import InputPy
			self._inputPy = InputPy(self._core, self._cmd_group)
		return self._inputPy

	@property
	def lpy(self):
		"""lpy commands group. 5 Sub-classes, 0 commands."""
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
		"""plp commands group. 16 Sub-classes, 0 commands."""
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
	def return(self):
		"""return commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_return'):
			from .Return import Return
			self._return = Return(self._core, self._cmd_group)
		return self._return

	@property
	def setting(self):
		"""setting commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_setting'):
			from .Setting import Setting
			self._setting = Setting(self._core, self._cmd_group)
		return self._setting

	@property
	def special(self):
		"""special commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_special'):
			from .Special import Special
			self._special = Special(self._core, self._cmd_group)
		return self._special

	@property
	def subframe(self):
		"""subframe commands group. 12 Sub-classes, 0 commands."""
		if not hasattr(self, '_subframe'):
			from .Subframe import Subframe
			self._subframe = Subframe(self._core, self._cmd_group)
		return self._subframe

	@property
	def txid(self):
		"""txid commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_txid'):
			from .Txid import Txid
			self._txid = Txid(self._core, self._cmd_group)
		return self._txid

	def get_bsid(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:BSID \n
		Snippet: value: int = driver.source.bb.a3Tsc.get_bsid() \n
		Sets the ID of the broadcast stream. \n
			:return: broadcast_str_id: integer Range: 0 to 65535
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:BSID?')
		return Conversions.str_to_int(response)

	def set_bsid(self, broadcast_str_id: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:BSID \n
		Snippet: driver.source.bb.a3Tsc.set_bsid(broadcast_str_id = 1) \n
		Sets the ID of the broadcast stream. \n
			:param broadcast_str_id: integer Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(broadcast_str_id)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:BSID {param}')

	# noinspection PyTypeChecker
	def get_ip_packet(self) -> enums.Atsc30TestIppAcket:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:IPPacket \n
		Snippet: value: enums.Atsc30TestIppAcket = driver.source.bb.a3Tsc.get_ip_packet() \n
		Specifies the structure of the test IP packet that is fed to the modulator. \n
			:return: test_ip_packet: HUDP
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:IPPacket?')
		return Conversions.str_to_scalar_enum(response, enums.Atsc30TestIppAcket)

	def set_ip_packet(self, test_ip_packet: enums.Atsc30TestIppAcket) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:IPPacket \n
		Snippet: driver.source.bb.a3Tsc.set_ip_packet(test_ip_packet = enums.Atsc30TestIppAcket.HUDP) \n
		Specifies the structure of the test IP packet that is fed to the modulator. \n
			:param test_ip_packet: HUDP
		"""
		param = Conversions.enum_scalar_to_str(test_ip_packet, enums.Atsc30TestIppAcket)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:IPPacket {param}')

	# noinspection PyTypeChecker
	def get_lls(self) -> enums.Atsc30LowLevelSignaling:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:LLS \n
		Snippet: value: enums.Atsc30LowLevelSignaling = driver.source.bb.a3Tsc.get_lls() \n
		Queries, if low-level signaling is present or absent. \n
			:return: low_level_sign: ABSent| PRESent
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:LLS?')
		return Conversions.str_to_scalar_enum(response, enums.Atsc30LowLevelSignaling)

	# noinspection PyTypeChecker
	def get_network_mode(self) -> enums.EnetworkMode:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:NETWorkmode \n
		Snippet: value: enums.EnetworkMode = driver.source.bb.a3Tsc.get_network_mode() \n
		Sets the network mode. \n
			:return: network_mode: MFN| SFN
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:NETWorkmode?')
		return Conversions.str_to_scalar_enum(response, enums.EnetworkMode)

	def set_network_mode(self, network_mode: enums.EnetworkMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:NETWorkmode \n
		Snippet: driver.source.bb.a3Tsc.set_network_mode(network_mode = enums.EnetworkMode.MFN) \n
		Sets the network mode. \n
			:param network_mode: MFN| SFN
		"""
		param = Conversions.enum_scalar_to_str(network_mode, enums.EnetworkMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:NETWorkmode {param}')

	def get_nrf(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:NRF \n
		Snippet: value: int = driver.source.bb.a3Tsc.get_nrf() \n
		Queries the number of radio frequencies involved in channel bonding. \n
			:return: num_rfs: integer 0 Channel bonding is not used for the current frame. Range: 0 to 1
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:NRF?')
		return Conversions.str_to_int(response)

	# noinspection PyTypeChecker
	def get_papr(self) -> enums.T2SystemPapr:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:PAPR \n
		Snippet: value: enums.T2SystemPapr = driver.source.bb.a3Tsc.get_papr() \n
		Sets the technique to reduce the peak to average power ratio. \n
			:return: papr: OFF| TR
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:PAPR?')
		return Conversions.str_to_scalar_enum(response, enums.T2SystemPapr)

	def set_papr(self, papr: enums.T2SystemPapr) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:PAPR \n
		Snippet: driver.source.bb.a3Tsc.set_papr(papr = enums.T2SystemPapr.OFF) \n
		Sets the technique to reduce the peak to average power ratio. \n
			:param papr: OFF| TR
		"""
		param = Conversions.enum_scalar_to_str(papr, enums.T2SystemPapr)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:PAPR {param}')

	# noinspection PyTypeChecker
	def get_payload(self) -> enums.PayloadTestStuff:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:PAYLoad \n
		Snippet: value: enums.PayloadTestStuff = driver.source.bb.a3Tsc.get_payload() \n
		Defines the payload area content of the packet. \n
			:return: payload: H00| HFF| PRBS
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:PAYLoad?')
		return Conversions.str_to_scalar_enum(response, enums.PayloadTestStuff)

	def set_payload(self, payload: enums.PayloadTestStuff) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:PAYLoad \n
		Snippet: driver.source.bb.a3Tsc.set_payload(payload = enums.PayloadTestStuff.H00) \n
		Defines the payload area content of the packet. \n
			:param payload: H00| HFF| PRBS
		"""
		param = Conversions.enum_scalar_to_str(payload, enums.PayloadTestStuff)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:PAYLoad {param}')

	def get_pid(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:PID \n
		Snippet: value: int = driver.source.bb.a3Tsc.get_pid() \n
		Sets the . \n
			:return: pid: integer Range: #H0000 to #H1FFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:PID?')
		return Conversions.str_to_int(response)

	def set_pid(self, pid: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:PID \n
		Snippet: driver.source.bb.a3Tsc.set_pid(pid = 1) \n
		Sets the . \n
			:param pid: integer Range: #H0000 to #H1FFF
		"""
		param = Conversions.decimal_value_to_str(pid)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:PID {param}')

	# noinspection PyTypeChecker
	def get_pid_test_pack(self) -> enums.PidTestPacket:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:PIDTestpack \n
		Snippet: value: enums.PidTestPacket = driver.source.bb.a3Tsc.get_pid_test_pack() \n
		If a header is present in the test packet ('Test TS Packet > Head/184 Payload') , you can specify a fixed or variable
		packet identifier (PID) . \n
			:return: pid_test_packet: VARiable| NULL
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:PIDTestpack?')
		return Conversions.str_to_scalar_enum(response, enums.PidTestPacket)

	def set_pid_test_pack(self, pid_test_packet: enums.PidTestPacket) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:PIDTestpack \n
		Snippet: driver.source.bb.a3Tsc.set_pid_test_pack(pid_test_packet = enums.PidTestPacket.NULL) \n
		If a header is present in the test packet ('Test TS Packet > Head/184 Payload') , you can specify a fixed or variable
		packet identifier (PID) . \n
			:param pid_test_packet: VARiable| NULL
		"""
		param = Conversions.enum_scalar_to_str(pid_test_packet, enums.PidTestPacket)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:PIDTestpack {param}')

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:PRESet \n
		Snippet: driver.source.bb.a3Tsc.preset() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:A3TSc:STATe. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:PRESet \n
		Snippet: driver.source.bb.a3Tsc.preset_with_opc() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:A3TSc:STATe. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmcv.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:A3TSc:PRESet', opc_timeout_ms)

	# noinspection PyTypeChecker
	def get_source(self) -> enums.CodingInputSignalSource:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:SOURce \n
		Snippet: value: enums.CodingInputSignalSource = driver.source.bb.a3Tsc.get_source() \n
		Sets the modulation source for the input signal. \n
			:return: source: EXTernal| TSPLayer| TESTsignal
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.CodingInputSignalSource)

	def set_source(self, source: enums.CodingInputSignalSource) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:SOURce \n
		Snippet: driver.source.bb.a3Tsc.set_source(source = enums.CodingInputSignalSource.EXTernal) \n
		Sets the modulation source for the input signal. \n
			:param source: EXTernal| TSPLayer| TESTsignal
		"""
		param = Conversions.enum_scalar_to_str(source, enums.CodingInputSignalSource)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:SOURce {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:STATe \n
		Snippet: value: bool = driver.source.bb.a3Tsc.get_state() \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:STATe \n
		Snippet: driver.source.bb.a3Tsc.set_state(state = False) \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:STATe {param}')

	# noinspection PyTypeChecker
	def get_time(self) -> enums.Atsc30TimeInfo:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:TIME \n
		Snippet: value: enums.Atsc30TimeInfo = driver.source.bb.a3Tsc.get_time() \n
		Configures the time information. \n
			:return: time_info: MSEC| USEC| NSEC| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:TIME?')
		return Conversions.str_to_scalar_enum(response, enums.Atsc30TimeInfo)

	def set_time(self, time_info: enums.Atsc30TimeInfo) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:TIME \n
		Snippet: driver.source.bb.a3Tsc.set_time(time_info = enums.Atsc30TimeInfo.MSEC) \n
		Configures the time information. \n
			:param time_info: MSEC| USEC| NSEC| OFF
		"""
		param = Conversions.enum_scalar_to_str(time_info, enums.Atsc30TimeInfo)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:TIME {param}')

	# noinspection PyTypeChecker
	def get_ts_packet(self) -> enums.SettingsTestTsPacket:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:TSPacket \n
		Snippet: value: enums.SettingsTestTsPacket = driver.source.bb.a3Tsc.get_ts_packet() \n
		Specifies the structure of the test transport stream packet that is fed to the modulator. \n
			:return: ts_packet: S187| H184
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:TSPacket?')
		return Conversions.str_to_scalar_enum(response, enums.SettingsTestTsPacket)

	def set_ts_packet(self, ts_packet: enums.SettingsTestTsPacket) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:TSPacket \n
		Snippet: driver.source.bb.a3Tsc.set_ts_packet(ts_packet = enums.SettingsTestTsPacket.H184) \n
		Specifies the structure of the test transport stream packet that is fed to the modulator. \n
			:param ts_packet: S187| H184
		"""
		param = Conversions.enum_scalar_to_str(ts_packet, enums.SettingsTestTsPacket)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:TSPacket {param}')

	def clone(self) -> 'A3Tsc':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = A3Tsc(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
