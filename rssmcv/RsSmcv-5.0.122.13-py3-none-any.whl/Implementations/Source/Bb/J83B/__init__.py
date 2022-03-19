from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class J83B:
	"""J83B commands group definition. 27 total commands, 5 Subgroups, 14 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("j83B", core, parent)

	@property
	def inputPy(self):
		"""inputPy commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_inputPy'):
			from .InputPy import InputPy
			self._inputPy = InputPy(self._core, self._cmd_group)
		return self._inputPy

	@property
	def interleaver(self):
		"""interleaver commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_interleaver'):
			from .Interleaver import Interleaver
			self._interleaver = Interleaver(self._core, self._cmd_group)
		return self._interleaver

	@property
	def setting(self):
		"""setting commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_setting'):
			from .Setting import Setting
			self._setting = Setting(self._core, self._cmd_group)
		return self._setting

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
	def get_constel(self) -> enums.J83BcodingJ83BcodingConstel:
		"""SCPI: [SOURce<HW>]:BB:J83B:CONStel \n
		Snippet: value: enums.J83BcodingJ83BcodingConstel = driver.source.bb.j83B.get_constel() \n
		Sets the constellation for modulation schemes. \n
			:return: constel: J64| J256| J1024 J64 Modulation setting QAM64. J256 Modulation setting QAM256. J1024 Modulation setting QAM1024.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:J83B:CONStel?')
		return Conversions.str_to_scalar_enum(response, enums.J83BcodingJ83BcodingConstel)

	def set_constel(self, constel: enums.J83BcodingJ83BcodingConstel) -> None:
		"""SCPI: [SOURce<HW>]:BB:J83B:CONStel \n
		Snippet: driver.source.bb.j83B.set_constel(constel = enums.J83BcodingJ83BcodingConstel.J1024) \n
		Sets the constellation for modulation schemes. \n
			:param constel: J64| J256| J1024 J64 Modulation setting QAM64. J256 Modulation setting QAM256. J1024 Modulation setting QAM1024.
		"""
		param = Conversions.enum_scalar_to_str(constel, enums.J83BcodingJ83BcodingConstel)
		self._core.io.write(f'SOURce<HwInstance>:BB:J83B:CONStel {param}')

	# noinspection PyTypeChecker
	def get_packet_length(self) -> enums.CodingInputSignalPacketLength:
		"""SCPI: [SOURce<HW>]:BB:J83B:PACKetlength \n
		Snippet: value: enums.CodingInputSignalPacketLength = driver.source.bb.j83B.get_packet_length() \n
		Queries the packet length of the external transport stream in bytes. \n
			:return: inp_sig_plength: P188| INValid P188 188 byte packets specified for serial input and parallel input. INValid Packet length does not match the specified length.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:J83B:PACKetlength?')
		return Conversions.str_to_scalar_enum(response, enums.CodingInputSignalPacketLength)

	# noinspection PyTypeChecker
	def get_payload(self) -> enums.PayloadTestStuff:
		"""SCPI: [SOURce<HW>]:BB:J83B:PAYLoad \n
		Snippet: value: enums.PayloadTestStuff = driver.source.bb.j83B.get_payload() \n
		Sets the payload field of the transport stream packet content. \n
			:return: set_payload: PRBS| H00| HFF PRBS PRBS data in accordance with H00 Exclusively 00 (hex) data HFF Exclusively FF (hex) data
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:J83B:PAYLoad?')
		return Conversions.str_to_scalar_enum(response, enums.PayloadTestStuff)

	def set_payload(self, set_payload: enums.PayloadTestStuff) -> None:
		"""SCPI: [SOURce<HW>]:BB:J83B:PAYLoad \n
		Snippet: driver.source.bb.j83B.set_payload(set_payload = enums.PayloadTestStuff.H00) \n
		Sets the payload field of the transport stream packet content. \n
			:param set_payload: PRBS| H00| HFF PRBS PRBS data in accordance with H00 Exclusively 00 (hex) data HFF Exclusively FF (hex) data
		"""
		param = Conversions.enum_scalar_to_str(set_payload, enums.PayloadTestStuff)
		self._core.io.write(f'SOURce<HwInstance>:BB:J83B:PAYLoad {param}')

	def get_pid(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:J83B:PID \n
		Snippet: value: int = driver.source.bb.j83B.get_pid() \n
		Sets the packet identifier (PID) . \n
			:return: set_pid: integer Range: 0 to 8191
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:J83B:PID?')
		return Conversions.str_to_int(response)

	def set_pid(self, set_pid: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:J83B:PID \n
		Snippet: driver.source.bb.j83B.set_pid(set_pid = 1) \n
		Sets the packet identifier (PID) . \n
			:param set_pid: integer Range: 0 to 8191
		"""
		param = Conversions.decimal_value_to_str(set_pid)
		self._core.io.write(f'SOURce<HwInstance>:BB:J83B:PID {param}')

	# noinspection PyTypeChecker
	def get_pid_test_pack(self) -> enums.PidTestPacket:
		"""SCPI: [SOURce<HW>]:BB:J83B:PIDTestpack \n
		Snippet: value: enums.PidTestPacket = driver.source.bb.j83B.get_pid_test_pack() \n
		Sets a fixed or variable packet identifier (PID) . If a header is present in the test packet ('Test TS Packet > Head/184
		Payload') , you can specify a fixed or variable packet identifier (PID) . \n
			:return: set_pid_testpack: NULL| VARiable
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:J83B:PIDTestpack?')
		return Conversions.str_to_scalar_enum(response, enums.PidTestPacket)

	def set_pid_test_pack(self, set_pid_testpack: enums.PidTestPacket) -> None:
		"""SCPI: [SOURce<HW>]:BB:J83B:PIDTestpack \n
		Snippet: driver.source.bb.j83B.set_pid_test_pack(set_pid_testpack = enums.PidTestPacket.NULL) \n
		Sets a fixed or variable packet identifier (PID) . If a header is present in the test packet ('Test TS Packet > Head/184
		Payload') , you can specify a fixed or variable packet identifier (PID) . \n
			:param set_pid_testpack: NULL| VARiable
		"""
		param = Conversions.enum_scalar_to_str(set_pid_testpack, enums.PidTestPacket)
		self._core.io.write(f'SOURce<HwInstance>:BB:J83B:PIDTestpack {param}')

	# noinspection PyTypeChecker
	def get_prbs(self) -> enums.SettingsPrbs:
		"""SCPI: [SOURce<HW>]:BB:J83B:PRBS \n
		Snippet: value: enums.SettingsPrbs = driver.source.bb.j83B.get_prbs() \n
		Sets the length of the PRBS sequence. \n
			:return: set_prbs: P23_1| P15_1 P23_1 PRBS 23 sequence as specified by . P15_1 PRBS 15 sequence as specified by .
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:J83B:PRBS?')
		return Conversions.str_to_scalar_enum(response, enums.SettingsPrbs)

	def set_prbs(self, set_prbs: enums.SettingsPrbs) -> None:
		"""SCPI: [SOURce<HW>]:BB:J83B:PRBS \n
		Snippet: driver.source.bb.j83B.set_prbs(set_prbs = enums.SettingsPrbs.P15_1) \n
		Sets the length of the PRBS sequence. \n
			:param set_prbs: P23_1| P15_1 P23_1 PRBS 23 sequence as specified by . P15_1 PRBS 15 sequence as specified by .
		"""
		param = Conversions.enum_scalar_to_str(set_prbs, enums.SettingsPrbs)
		self._core.io.write(f'SOURce<HwInstance>:BB:J83B:PRBS {param}')

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:J83B:PRESet \n
		Snippet: driver.source.bb.j83B.preset() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:J83B:STATe. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:J83B:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:J83B:PRESet \n
		Snippet: driver.source.bb.j83B.preset_with_opc() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:J83B:STATe. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmcv.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:J83B:PRESet', opc_timeout_ms)

	# noinspection PyTypeChecker
	def get_rolloff(self) -> enums.J83BcodingJ83BcodingRolloff:
		"""SCPI: [SOURce<HW>]:BB:J83B:ROLLoff \n
		Snippet: value: enums.J83BcodingJ83BcodingRolloff = driver.source.bb.j83B.get_rolloff() \n
		Queries the roll-off factor. \n
			:return: rolloff: 0.12| 0.18
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:J83B:ROLLoff?')
		return Conversions.str_to_scalar_enum(response, enums.J83BcodingJ83BcodingRolloff)

	# noinspection PyTypeChecker
	def get_source(self) -> enums.CodingInputSignalSource:
		"""SCPI: [SOURce<HW>]:BB:J83B:SOURce \n
		Snippet: value: enums.CodingInputSignalSource = driver.source.bb.j83B.get_source() \n
		Sets the modulation source for the input signal. \n
			:return: inp_sig_source: EXTernal| TSPLayer| TESTsignal
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:J83B:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.CodingInputSignalSource)

	def set_source(self, inp_sig_source: enums.CodingInputSignalSource) -> None:
		"""SCPI: [SOURce<HW>]:BB:J83B:SOURce \n
		Snippet: driver.source.bb.j83B.set_source(inp_sig_source = enums.CodingInputSignalSource.EXTernal) \n
		Sets the modulation source for the input signal. \n
			:param inp_sig_source: EXTernal| TSPLayer| TESTsignal
		"""
		param = Conversions.enum_scalar_to_str(inp_sig_source, enums.CodingInputSignalSource)
		self._core.io.write(f'SOURce<HwInstance>:BB:J83B:SOURce {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:J83B:STATe \n
		Snippet: value: bool = driver.source.bb.j83B.get_state() \n
		Enables/disables the DVB-S standard. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:J83B:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:J83B:STATe \n
		Snippet: driver.source.bb.j83B.set_state(state = False) \n
		Enables/disables the DVB-S standard. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:J83B:STATe {param}')

	# noinspection PyTypeChecker
	def get_stuffing(self) -> enums.StateOn:
		"""SCPI: [SOURce<HW>]:BB:J83B:STUFfing \n
		Snippet: value: enums.StateOn = driver.source.bb.j83B.get_stuffing() \n
		Queries the stuffing state that is active. \n
			:return: inp_sig_stuffing: 1| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:J83B:STUFfing?')
		return Conversions.str_to_scalar_enum(response, enums.StateOn)

	def get_symbols(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:J83B:SYMBols \n
		Snippet: value: int = driver.source.bb.j83B.get_symbols() \n
		Sets the symbol rate. \n
			:return: symbol_rate: integer Range: 4.5512469E+06 to 5.8965907E+06
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:J83B:SYMBols?')
		return Conversions.str_to_int(response)

	def set_symbols(self, symbol_rate: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:J83B:SYMBols \n
		Snippet: driver.source.bb.j83B.set_symbols(symbol_rate = 1) \n
		Sets the symbol rate. \n
			:param symbol_rate: integer Range: 4.5512469E+06 to 5.8965907E+06
		"""
		param = Conversions.decimal_value_to_str(symbol_rate)
		self._core.io.write(f'SOURce<HwInstance>:BB:J83B:SYMBols {param}')

	# noinspection PyTypeChecker
	def get_test_signal(self) -> enums.J83BcodingJ83BinputSignalTestSignal:
		"""SCPI: [SOURce<HW>]:BB:J83B:TESTsignal \n
		Snippet: value: enums.J83BcodingJ83BinputSignalTestSignal = driver.source.bb.j83B.get_test_signal() \n
		Defines the test signal data. \n
			:return: inp_sig_test_sig: TTSP| PBEM| PBTR TTSP Test TS packet with standardized packet data used as modulation data in the transport stream. PBDE Pure pseudo-random bit sequence (PRBS) data used as modulation data with no packet structure. The sequence is inserted before the convolutional encoder. PRBS data conforms with specification. PBEM PRBS after convolutional encoder Pure pseudo-random bit sequence (PRBS) data used as modulation data with no packet structure. The sequence is inserted after the convolutional encoder.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:J83B:TESTsignal?')
		return Conversions.str_to_scalar_enum(response, enums.J83BcodingJ83BinputSignalTestSignal)

	def set_test_signal(self, inp_sig_test_sig: enums.J83BcodingJ83BinputSignalTestSignal) -> None:
		"""SCPI: [SOURce<HW>]:BB:J83B:TESTsignal \n
		Snippet: driver.source.bb.j83B.set_test_signal(inp_sig_test_sig = enums.J83BcodingJ83BinputSignalTestSignal.PBEM) \n
		Defines the test signal data. \n
			:param inp_sig_test_sig: TTSP| PBEM| PBTR TTSP Test TS packet with standardized packet data used as modulation data in the transport stream. PBDE Pure pseudo-random bit sequence (PRBS) data used as modulation data with no packet structure. The sequence is inserted before the convolutional encoder. PRBS data conforms with specification. PBEM PRBS after convolutional encoder Pure pseudo-random bit sequence (PRBS) data used as modulation data with no packet structure. The sequence is inserted after the convolutional encoder.
		"""
		param = Conversions.enum_scalar_to_str(inp_sig_test_sig, enums.J83BcodingJ83BinputSignalTestSignal)
		self._core.io.write(f'SOURce<HwInstance>:BB:J83B:TESTsignal {param}')

	# noinspection PyTypeChecker
	def get_ts_packet(self) -> enums.SettingsTestTsPacket:
		"""SCPI: [SOURce<HW>]:BB:J83B:TSPacket \n
		Snippet: value: enums.SettingsTestTsPacket = driver.source.bb.j83B.get_ts_packet() \n
		Specifies the structure of the test transport stream packet that is fed to the modulator. \n
			:return: set_ts_packet: H184| S187 H184 Head/184 Payload S187 Sync/187 Payload
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:J83B:TSPacket?')
		return Conversions.str_to_scalar_enum(response, enums.SettingsTestTsPacket)

	def set_ts_packet(self, set_ts_packet: enums.SettingsTestTsPacket) -> None:
		"""SCPI: [SOURce<HW>]:BB:J83B:TSPacket \n
		Snippet: driver.source.bb.j83B.set_ts_packet(set_ts_packet = enums.SettingsTestTsPacket.H184) \n
		Specifies the structure of the test transport stream packet that is fed to the modulator. \n
			:param set_ts_packet: H184| S187 H184 Head/184 Payload S187 Sync/187 Payload
		"""
		param = Conversions.enum_scalar_to_str(set_ts_packet, enums.SettingsTestTsPacket)
		self._core.io.write(f'SOURce<HwInstance>:BB:J83B:TSPacket {param}')

	def clone(self) -> 'J83B':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = J83B(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
