from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dtmb:
	"""Dtmb commands group definition. 32 total commands, 8 Subgroups, 16 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dtmb", core, parent)

	@property
	def channel(self):
		"""channel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_channel'):
			from .Channel import Channel
			self._channel = Channel(self._core, self._cmd_group)
		return self._channel

	@property
	def dual(self):
		"""dual commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dual'):
			from .Dual import Dual
			self._dual = Dual(self._core, self._cmd_group)
		return self._dual

	@property
	def inputPy(self):
		"""inputPy commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_inputPy'):
			from .InputPy import InputPy
			self._inputPy = InputPy(self._core, self._cmd_group)
		return self._inputPy

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
	def time(self):
		"""time commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_time'):
			from .Time import Time
			self._time = Time(self._core, self._cmd_group)
		return self._time

	@property
	def useful(self):
		"""useful commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_useful'):
			from .Useful import Useful
			self._useful = Useful(self._core, self._cmd_group)
		return self._useful

	@property
	def special(self):
		"""special commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_special'):
			from .Special import Special
			self._special = Special(self._core, self._cmd_group)
		return self._special

	# noinspection PyTypeChecker
	def get_constel(self) -> enums.DtmbCodingConstel:
		"""SCPI: [SOURce<HW>]:BB:DTMB:CONStel \n
		Snippet: value: enums.DtmbCodingConstel = driver.source.bb.dtmb.get_constel() \n
		Defines the constellation. \n
			:return: dtmb_constel: D4| D4NR| D16| D32| D64 D4 4QAM D4NR 4QAM-NR D16 16QAM D32 32QAM D64 64QAM
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DTMB:CONStel?')
		return Conversions.str_to_scalar_enum(response, enums.DtmbCodingConstel)

	def set_constel(self, dtmb_constel: enums.DtmbCodingConstel) -> None:
		"""SCPI: [SOURce<HW>]:BB:DTMB:CONStel \n
		Snippet: driver.source.bb.dtmb.set_constel(dtmb_constel = enums.DtmbCodingConstel.D16) \n
		Defines the constellation. \n
			:param dtmb_constel: D4| D4NR| D16| D32| D64 D4 4QAM D4NR 4QAM-NR D16 16QAM D32 32QAM D64 64QAM
		"""
		param = Conversions.enum_scalar_to_str(dtmb_constel, enums.DtmbCodingConstel)
		self._core.io.write(f'SOURce<HwInstance>:BB:DTMB:CONStel {param}')

	def get_frames(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DTMB:FRAMes \n
		Snippet: value: bool = driver.source.bb.dtmb.get_frames() \n
		Defines whether a control frame is added to each signal frame group or not. \n
			:return: dtmb_frames: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DTMB:FRAMes?')
		return Conversions.str_to_bool(response)

	def set_frames(self, dtmb_frames: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DTMB:FRAMes \n
		Snippet: driver.source.bb.dtmb.set_frames(dtmb_frames = False) \n
		Defines whether a control frame is added to each signal frame group or not. \n
			:param dtmb_frames: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(dtmb_frames)
		self._core.io.write(f'SOURce<HwInstance>:BB:DTMB:FRAMes {param}')

	# noinspection PyTypeChecker
	def get_gic(self) -> enums.DtmbCodingGipN:
		"""SCPI: [SOURce<HW>]:BB:DTMB:GIC \n
		Snippet: value: enums.DtmbCodingGipN = driver.source.bb.dtmb.get_gic() \n
		Defines the initial condition of the PN sequences in the frame headers. \n
			:return: dtmb_guard_pn: VAR| CONSt VAR Uses the definition of the table in the standard. CONSt Uses the initial condition of index 0 for all signal frames.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DTMB:GIC?')
		return Conversions.str_to_scalar_enum(response, enums.DtmbCodingGipN)

	def set_gic(self, dtmb_guard_pn: enums.DtmbCodingGipN) -> None:
		"""SCPI: [SOURce<HW>]:BB:DTMB:GIC \n
		Snippet: driver.source.bb.dtmb.set_gic(dtmb_guard_pn = enums.DtmbCodingGipN.CONSt) \n
		Defines the initial condition of the PN sequences in the frame headers. \n
			:param dtmb_guard_pn: VAR| CONSt VAR Uses the definition of the table in the standard. CONSt Uses the initial condition of index 0 for all signal frames.
		"""
		param = Conversions.enum_scalar_to_str(dtmb_guard_pn, enums.DtmbCodingGipN)
		self._core.io.write(f'SOURce<HwInstance>:BB:DTMB:GIC {param}')

	# noinspection PyTypeChecker
	def get_guard(self) -> enums.DtmbCodingGuardInterval:
		"""SCPI: [SOURce<HW>]:BB:DTMB:GUARd \n
		Snippet: value: enums.DtmbCodingGuardInterval = driver.source.bb.dtmb.get_guard() \n
		Sets the guard interval length. \n
			:return: dtmb_guard: G420| G595| G945
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DTMB:GUARd?')
		return Conversions.str_to_scalar_enum(response, enums.DtmbCodingGuardInterval)

	def set_guard(self, dtmb_guard: enums.DtmbCodingGuardInterval) -> None:
		"""SCPI: [SOURce<HW>]:BB:DTMB:GUARd \n
		Snippet: driver.source.bb.dtmb.set_guard(dtmb_guard = enums.DtmbCodingGuardInterval.G420) \n
		Sets the guard interval length. \n
			:param dtmb_guard: G420| G595| G945
		"""
		param = Conversions.enum_scalar_to_str(dtmb_guard, enums.DtmbCodingGuardInterval)
		self._core.io.write(f'SOURce<HwInstance>:BB:DTMB:GUARd {param}')

	# noinspection PyTypeChecker
	def get_packet_length(self) -> enums.DtmbCodingInputSignalPacketLength:
		"""SCPI: [SOURce<HW>]:BB:DTMB:PACKetlength \n
		Snippet: value: enums.DtmbCodingInputSignalPacketLength = driver.source.bb.dtmb.get_packet_length() \n
		Queries the packet length of the external transport stream in bytes. \n
			:return: dtmb_plength: P188| INValid P188 188 byte packets specified for serial input ('Input TS IN') and parallel input ('Input IP') . INValid Packet length does not match the specified length.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DTMB:PACKetlength?')
		return Conversions.str_to_scalar_enum(response, enums.DtmbCodingInputSignalPacketLength)

	# noinspection PyTypeChecker
	def get_payload(self) -> enums.PayloadTestStuff:
		"""SCPI: [SOURce<HW>]:BB:DTMB:PAYLoad \n
		Snippet: value: enums.PayloadTestStuff = driver.source.bb.dtmb.get_payload() \n
		Defines the payload area content of the packet. \n
			:return: dtmb_payload: H00| HFF| PRBS
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DTMB:PAYLoad?')
		return Conversions.str_to_scalar_enum(response, enums.PayloadTestStuff)

	def set_payload(self, dtmb_payload: enums.PayloadTestStuff) -> None:
		"""SCPI: [SOURce<HW>]:BB:DTMB:PAYLoad \n
		Snippet: driver.source.bb.dtmb.set_payload(dtmb_payload = enums.PayloadTestStuff.H00) \n
		Defines the payload area content of the packet. \n
			:param dtmb_payload: H00| HFF| PRBS
		"""
		param = Conversions.enum_scalar_to_str(dtmb_payload, enums.PayloadTestStuff)
		self._core.io.write(f'SOURce<HwInstance>:BB:DTMB:PAYLoad {param}')

	def get_pid(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DTMB:PID \n
		Snippet: value: int = driver.source.bb.dtmb.get_pid() \n
		Sets the . \n
			:return: dtmb_pid: integer Range: #H0000 to #H1FFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DTMB:PID?')
		return Conversions.str_to_int(response)

	def set_pid(self, dtmb_pid: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:DTMB:PID \n
		Snippet: driver.source.bb.dtmb.set_pid(dtmb_pid = 1) \n
		Sets the . \n
			:param dtmb_pid: integer Range: #H0000 to #H1FFF
		"""
		param = Conversions.decimal_value_to_str(dtmb_pid)
		self._core.io.write(f'SOURce<HwInstance>:BB:DTMB:PID {param}')

	# noinspection PyTypeChecker
	def get_pid_test_pack(self) -> enums.PidTestPacket:
		"""SCPI: [SOURce<HW>]:BB:DTMB:PIDTestpack \n
		Snippet: value: enums.PidTestPacket = driver.source.bb.dtmb.get_pid_test_pack() \n
		If a header is present in the test packet ('Test TS Packet > Head/184 Payload') , you can specify a fixed or variable
		packet identifier (PID) . \n
			:return: dtmb_source: NULL| VARiable
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DTMB:PIDTestpack?')
		return Conversions.str_to_scalar_enum(response, enums.PidTestPacket)

	def set_pid_test_pack(self, dtmb_source: enums.PidTestPacket) -> None:
		"""SCPI: [SOURce<HW>]:BB:DTMB:PIDTestpack \n
		Snippet: driver.source.bb.dtmb.set_pid_test_pack(dtmb_source = enums.PidTestPacket.NULL) \n
		If a header is present in the test packet ('Test TS Packet > Head/184 Payload') , you can specify a fixed or variable
		packet identifier (PID) . \n
			:param dtmb_source: NULL| VARiable
		"""
		param = Conversions.enum_scalar_to_str(dtmb_source, enums.PidTestPacket)
		self._core.io.write(f'SOURce<HwInstance>:BB:DTMB:PIDTestpack {param}')

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:DTMB:PRESet \n
		Snippet: driver.source.bb.dtmb.preset() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:DTMB:STATe. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:DTMB:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:DTMB:PRESet \n
		Snippet: driver.source.bb.dtmb.preset_with_opc() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:DTMB:STATe. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmcv.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:DTMB:PRESet', opc_timeout_ms)

	# noinspection PyTypeChecker
	def get_rate(self) -> enums.DtmbCodingCoderate:
		"""SCPI: [SOURce<HW>]:BB:DTMB:RATE \n
		Snippet: value: enums.DtmbCodingCoderate = driver.source.bb.dtmb.get_rate() \n
		Sets the code rate. \n
			:return: dtmb_code_rate: R04| R06| R08
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DTMB:RATE?')
		return Conversions.str_to_scalar_enum(response, enums.DtmbCodingCoderate)

	def set_rate(self, dtmb_code_rate: enums.DtmbCodingCoderate) -> None:
		"""SCPI: [SOURce<HW>]:BB:DTMB:RATE \n
		Snippet: driver.source.bb.dtmb.set_rate(dtmb_code_rate = enums.DtmbCodingCoderate.R04) \n
		Sets the code rate. \n
			:param dtmb_code_rate: R04| R06| R08
		"""
		param = Conversions.enum_scalar_to_str(dtmb_code_rate, enums.DtmbCodingCoderate)
		self._core.io.write(f'SOURce<HwInstance>:BB:DTMB:RATE {param}')

	def get_single(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DTMB:SINGle \n
		Snippet: value: bool = driver.source.bb.dtmb.get_single() \n
		Enables/disables single carrier mode. \n
			:return: dtmb_single: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DTMB:SINGle?')
		return Conversions.str_to_bool(response)

	def set_single(self, dtmb_single: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DTMB:SINGle \n
		Snippet: driver.source.bb.dtmb.set_single(dtmb_single = False) \n
		Enables/disables single carrier mode. \n
			:param dtmb_single: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(dtmb_single)
		self._core.io.write(f'SOURce<HwInstance>:BB:DTMB:SINGle {param}')

	# noinspection PyTypeChecker
	def get_source(self) -> enums.CodingInputSignalSource:
		"""SCPI: [SOURce<HW>]:BB:DTMB:SOURce \n
		Snippet: value: enums.CodingInputSignalSource = driver.source.bb.dtmb.get_source() \n
		Sets the modulation source for the input signal. \n
			:return: dtmb_source: EXTernal| TSPLayer| TESTsignal
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DTMB:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.CodingInputSignalSource)

	def set_source(self, dtmb_source: enums.CodingInputSignalSource) -> None:
		"""SCPI: [SOURce<HW>]:BB:DTMB:SOURce \n
		Snippet: driver.source.bb.dtmb.set_source(dtmb_source = enums.CodingInputSignalSource.EXTernal) \n
		Sets the modulation source for the input signal. \n
			:param dtmb_source: EXTernal| TSPLayer| TESTsignal
		"""
		param = Conversions.enum_scalar_to_str(dtmb_source, enums.CodingInputSignalSource)
		self._core.io.write(f'SOURce<HwInstance>:BB:DTMB:SOURce {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DTMB:STATe \n
		Snippet: value: bool = driver.source.bb.dtmb.get_state() \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DTMB:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DTMB:STATe \n
		Snippet: driver.source.bb.dtmb.set_state(state = False) \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:DTMB:STATe {param}')

	def get_stuffing(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DTMB:STUFfing \n
		Snippet: value: bool = driver.source.bb.dtmb.get_stuffing() \n
		Activates stuffing. \n
			:return: dtmb_stuffing: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DTMB:STUFfing?')
		return Conversions.str_to_bool(response)

	def set_stuffing(self, dtmb_stuffing: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DTMB:STUFfing \n
		Snippet: driver.source.bb.dtmb.set_stuffing(dtmb_stuffing = False) \n
		Activates stuffing. \n
			:param dtmb_stuffing: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(dtmb_stuffing)
		self._core.io.write(f'SOURce<HwInstance>:BB:DTMB:STUFfing {param}')

	# noinspection PyTypeChecker
	def get_test_signal(self) -> enums.CodingInputSignalTestSignal:
		"""SCPI: [SOURce<HW>]:BB:DTMB:TESTsignal \n
		Snippet: value: enums.CodingInputSignalTestSignal = driver.source.bb.dtmb.get_test_signal() \n
		Queries the test signal, that consists of test packets. \n
			:return: dtmb_test_sig: TTSP Test TS packet with standardized packet data used as modulation data in the transport stream.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DTMB:TESTsignal?')
		return Conversions.str_to_scalar_enum(response, enums.CodingInputSignalTestSignal)

	def set_test_signal(self, dtmb_test_sig: enums.CodingInputSignalTestSignal) -> None:
		"""SCPI: [SOURce<HW>]:BB:DTMB:TESTsignal \n
		Snippet: driver.source.bb.dtmb.set_test_signal(dtmb_test_sig = enums.CodingInputSignalTestSignal.TTSP) \n
		Queries the test signal, that consists of test packets. \n
			:param dtmb_test_sig: TTSP Test TS packet with standardized packet data used as modulation data in the transport stream.
		"""
		param = Conversions.enum_scalar_to_str(dtmb_test_sig, enums.CodingInputSignalTestSignal)
		self._core.io.write(f'SOURce<HwInstance>:BB:DTMB:TESTsignal {param}')

	# noinspection PyTypeChecker
	def get_ts_packet(self) -> enums.SettingsTestTsPacket:
		"""SCPI: [SOURce<HW>]:BB:DTMB:TSPacket \n
		Snippet: value: enums.SettingsTestTsPacket = driver.source.bb.dtmb.get_ts_packet() \n
		Specifies the structure of the test transport stream packet that is fed to the modulator. \n
			:return: dtmb_test_ts_pack: H184| S187
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DTMB:TSPacket?')
		return Conversions.str_to_scalar_enum(response, enums.SettingsTestTsPacket)

	def set_ts_packet(self, dtmb_test_ts_pack: enums.SettingsTestTsPacket) -> None:
		"""SCPI: [SOURce<HW>]:BB:DTMB:TSPacket \n
		Snippet: driver.source.bb.dtmb.set_ts_packet(dtmb_test_ts_pack = enums.SettingsTestTsPacket.H184) \n
		Specifies the structure of the test transport stream packet that is fed to the modulator. \n
			:param dtmb_test_ts_pack: H184| S187
		"""
		param = Conversions.enum_scalar_to_str(dtmb_test_ts_pack, enums.SettingsTestTsPacket)
		self._core.io.write(f'SOURce<HwInstance>:BB:DTMB:TSPacket {param}')

	def clone(self) -> 'Dtmb':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dtmb(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
