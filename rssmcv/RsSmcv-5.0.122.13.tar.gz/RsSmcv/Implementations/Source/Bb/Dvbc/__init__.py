from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dvbc:
	"""Dvbc commands group definition. 26 total commands, 4 Subgroups, 14 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dvbc", core, parent)

	@property
	def inputPy(self):
		"""inputPy commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_inputPy'):
			from .InputPy import InputPy
			self._inputPy = InputPy(self._core, self._cmd_group)
		return self._inputPy

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
	def get_constel(self) -> enums.DvbcCodingDvbcCodingConstel:
		"""SCPI: [SOURce<HW>]:BB:DVBC:CONStel \n
		Snippet: value: enums.DvbcCodingDvbcCodingConstel = driver.source.bb.dvbc.get_constel() \n
		Defines the constellation. \n
			:return: constel: C16| C32| C64| C128| C256 C16|C32|C64|C128|C256 16/32/64/128/256QAM
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBC:CONStel?')
		return Conversions.str_to_scalar_enum(response, enums.DvbcCodingDvbcCodingConstel)

	def set_constel(self, constel: enums.DvbcCodingDvbcCodingConstel) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBC:CONStel \n
		Snippet: driver.source.bb.dvbc.set_constel(constel = enums.DvbcCodingDvbcCodingConstel.C128) \n
		Defines the constellation. \n
			:param constel: C16| C32| C64| C128| C256 C16|C32|C64|C128|C256 16/32/64/128/256QAM
		"""
		param = Conversions.enum_scalar_to_str(constel, enums.DvbcCodingDvbcCodingConstel)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBC:CONStel {param}')

	# noinspection PyTypeChecker
	def get_packet_length(self) -> enums.DvbxCodingInputSignalPacketLength:
		"""SCPI: [SOURce<HW>]:BB:DVBC:PACKetlength \n
		Snippet: value: enums.DvbxCodingInputSignalPacketLength = driver.source.bb.dvbc.get_packet_length() \n
		Queries the packet length of the external transport stream in bytes. \n
			:return: inp_sig_plength: P188| P204| INValid P188|P204 188/204 byte packets specified for serial input and parallel input. INValid Packet length does not match the specified length.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBC:PACKetlength?')
		return Conversions.str_to_scalar_enum(response, enums.DvbxCodingInputSignalPacketLength)

	# noinspection PyTypeChecker
	def get_payload(self) -> enums.PayloadTestStuff:
		"""SCPI: [SOURce<HW>]:BB:DVBC:PAYLoad \n
		Snippet: value: enums.PayloadTestStuff = driver.source.bb.dvbc.get_payload() \n
		Defines the payload area content of the packet. \n
			:return: set_payload: PRBS| H00| HFF PRBS PRBS data in accordance with H00 Exclusively 00 (hex) data HFF Exclusively FF (hex) data
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBC:PAYLoad?')
		return Conversions.str_to_scalar_enum(response, enums.PayloadTestStuff)

	def set_payload(self, set_payload: enums.PayloadTestStuff) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBC:PAYLoad \n
		Snippet: driver.source.bb.dvbc.set_payload(set_payload = enums.PayloadTestStuff.H00) \n
		Defines the payload area content of the packet. \n
			:param set_payload: PRBS| H00| HFF PRBS PRBS data in accordance with H00 Exclusively 00 (hex) data HFF Exclusively FF (hex) data
		"""
		param = Conversions.enum_scalar_to_str(set_payload, enums.PayloadTestStuff)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBC:PAYLoad {param}')

	def get_pid(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVBC:PID \n
		Snippet: value: int = driver.source.bb.dvbc.get_pid() \n
		Sets the . \n
			:return: set_pid: integer Range: 0 to 8191
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBC:PID?')
		return Conversions.str_to_int(response)

	def set_pid(self, set_pid: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBC:PID \n
		Snippet: driver.source.bb.dvbc.set_pid(set_pid = 1) \n
		Sets the . \n
			:param set_pid: integer Range: 0 to 8191
		"""
		param = Conversions.decimal_value_to_str(set_pid)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBC:PID {param}')

	# noinspection PyTypeChecker
	def get_pid_test_pack(self) -> enums.PidTestPacket:
		"""SCPI: [SOURce<HW>]:BB:DVBC:PIDTestpack \n
		Snippet: value: enums.PidTestPacket = driver.source.bb.dvbc.get_pid_test_pack() \n
		If a header is present in the test packet ('Test TS Packet > Head/184 Payload') , you can specify a fixed or variable
		packet identifier (PID) . \n
			:return: set_pid_testpack: NULL| VARiable
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBC:PIDTestpack?')
		return Conversions.str_to_scalar_enum(response, enums.PidTestPacket)

	def set_pid_test_pack(self, set_pid_testpack: enums.PidTestPacket) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBC:PIDTestpack \n
		Snippet: driver.source.bb.dvbc.set_pid_test_pack(set_pid_testpack = enums.PidTestPacket.NULL) \n
		If a header is present in the test packet ('Test TS Packet > Head/184 Payload') , you can specify a fixed or variable
		packet identifier (PID) . \n
			:param set_pid_testpack: NULL| VARiable
		"""
		param = Conversions.enum_scalar_to_str(set_pid_testpack, enums.PidTestPacket)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBC:PIDTestpack {param}')

	# noinspection PyTypeChecker
	def get_prbs(self) -> enums.SettingsPrbs:
		"""SCPI: [SOURce<HW>]:BB:DVBC:PRBS \n
		Snippet: value: enums.SettingsPrbs = driver.source.bb.dvbc.get_prbs() \n
		Sets the length of the PRBS sequence. You can select a PRBS 15 or a PRBS 23 sequence as specified by . \n
			:return: set_prbs: P23_1| P15_1 P23_1 PRBS 23 sequence as specified by . P15_1 PRBS 15 sequence as specified by .
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBC:PRBS?')
		return Conversions.str_to_scalar_enum(response, enums.SettingsPrbs)

	def set_prbs(self, set_prbs: enums.SettingsPrbs) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBC:PRBS \n
		Snippet: driver.source.bb.dvbc.set_prbs(set_prbs = enums.SettingsPrbs.P15_1) \n
		Sets the length of the PRBS sequence. You can select a PRBS 15 or a PRBS 23 sequence as specified by . \n
			:param set_prbs: P23_1| P15_1 P23_1 PRBS 23 sequence as specified by . P15_1 PRBS 15 sequence as specified by .
		"""
		param = Conversions.enum_scalar_to_str(set_prbs, enums.SettingsPrbs)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBC:PRBS {param}')

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBC:PRESet \n
		Snippet: driver.source.bb.dvbc.preset() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:DVBC:STATe. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBC:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBC:PRESet \n
		Snippet: driver.source.bb.dvbc.preset_with_opc() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:DVBC:STATe. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmcv.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:DVBC:PRESet', opc_timeout_ms)

	# noinspection PyTypeChecker
	def get_rolloff(self) -> enums.DvbcCodingDvbcCodingRolloff:
		"""SCPI: [SOURce<HW>]:BB:DVBC:ROLLoff \n
		Snippet: value: enums.DvbcCodingDvbcCodingRolloff = driver.source.bb.dvbc.get_rolloff() \n
		Displays the roll-off factor. \n
			:return: rolloff: 0.13| 0.15
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBC:ROLLoff?')
		return Conversions.str_to_scalar_enum(response, enums.DvbcCodingDvbcCodingRolloff)

	def set_rolloff(self, rolloff: enums.DvbcCodingDvbcCodingRolloff) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBC:ROLLoff \n
		Snippet: driver.source.bb.dvbc.set_rolloff(rolloff = enums.DvbcCodingDvbcCodingRolloff._0_dot_13) \n
		Displays the roll-off factor. \n
			:param rolloff: 0.13| 0.15
		"""
		param = Conversions.enum_scalar_to_str(rolloff, enums.DvbcCodingDvbcCodingRolloff)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBC:ROLLoff {param}')

	# noinspection PyTypeChecker
	def get_source(self) -> enums.CodingInputSignalSource:
		"""SCPI: [SOURce<HW>]:BB:DVBC:SOURce \n
		Snippet: value: enums.CodingInputSignalSource = driver.source.bb.dvbc.get_source() \n
		Sets the modulation source for the input signal. \n
			:return: inp_sig_source: EXTernal| TSPLayer| TESTsignal
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBC:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.CodingInputSignalSource)

	def set_source(self, inp_sig_source: enums.CodingInputSignalSource) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBC:SOURce \n
		Snippet: driver.source.bb.dvbc.set_source(inp_sig_source = enums.CodingInputSignalSource.EXTernal) \n
		Sets the modulation source for the input signal. \n
			:param inp_sig_source: EXTernal| TSPLayer| TESTsignal
		"""
		param = Conversions.enum_scalar_to_str(inp_sig_source, enums.CodingInputSignalSource)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBC:SOURce {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVBC:STATe \n
		Snippet: value: bool = driver.source.bb.dvbc.get_state() \n
		Enables/disables the DVB-S standard. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBC:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBC:STATe \n
		Snippet: driver.source.bb.dvbc.set_state(state = False) \n
		Enables/disables the DVB-S standard. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBC:STATe {param}')

	# noinspection PyTypeChecker
	def get_stuffing(self) -> enums.StateOn:
		"""SCPI: [SOURce<HW>]:BB:DVBC:STUFfing \n
		Snippet: value: enums.StateOn = driver.source.bb.dvbc.get_stuffing() \n
		Queries the stuffing state that is active. \n
			:return: inp_sig_stuffing: 1| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBC:STUFfing?')
		return Conversions.str_to_scalar_enum(response, enums.StateOn)

	def get_symbols(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVBC:SYMBols \n
		Snippet: value: int = driver.source.bb.dvbc.get_symbols() \n
		Sets the symbol rate. \n
			:return: symbol_rate: integer Range: 1.00E+05 to 8.00E+07
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBC:SYMBols?')
		return Conversions.str_to_int(response)

	def set_symbols(self, symbol_rate: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBC:SYMBols \n
		Snippet: driver.source.bb.dvbc.set_symbols(symbol_rate = 1) \n
		Sets the symbol rate. \n
			:param symbol_rate: integer Range: 1.00E+05 to 8.00E+07
		"""
		param = Conversions.decimal_value_to_str(symbol_rate)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBC:SYMBols {param}')

	# noinspection PyTypeChecker
	def get_test_signal(self) -> enums.DvbcCodingDvbcInputSignalTestSignal:
		"""SCPI: [SOURce<HW>]:BB:DVBC:TESTsignal \n
		Snippet: value: enums.DvbcCodingDvbcInputSignalTestSignal = driver.source.bb.dvbc.get_test_signal() \n
		Defines the test signal data. \n
			:return: inp_sig_test_sig: TTSP| PBDE| PBEM TTSP Test TS packet with standardized packet data used as modulation data in the transport stream. PBDE PRBS before differential encoder Pure pseudo-random bit sequence (PRBS) data used as modulation data with no packet structure. The sequence is inserted before the differential encoder. PRBS data conforms with specification. PBEM PRBS before mapper Pure pseudo-random bit sequence (PRBS) data used as modulation data with no packet structure. The sequence is inserted before the mapper.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBC:TESTsignal?')
		return Conversions.str_to_scalar_enum(response, enums.DvbcCodingDvbcInputSignalTestSignal)

	def set_test_signal(self, inp_sig_test_sig: enums.DvbcCodingDvbcInputSignalTestSignal) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBC:TESTsignal \n
		Snippet: driver.source.bb.dvbc.set_test_signal(inp_sig_test_sig = enums.DvbcCodingDvbcInputSignalTestSignal.PBDE) \n
		Defines the test signal data. \n
			:param inp_sig_test_sig: TTSP| PBDE| PBEM TTSP Test TS packet with standardized packet data used as modulation data in the transport stream. PBDE PRBS before differential encoder Pure pseudo-random bit sequence (PRBS) data used as modulation data with no packet structure. The sequence is inserted before the differential encoder. PRBS data conforms with specification. PBEM PRBS before mapper Pure pseudo-random bit sequence (PRBS) data used as modulation data with no packet structure. The sequence is inserted before the mapper.
		"""
		param = Conversions.enum_scalar_to_str(inp_sig_test_sig, enums.DvbcCodingDvbcInputSignalTestSignal)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBC:TESTsignal {param}')

	# noinspection PyTypeChecker
	def get_ts_packet(self) -> enums.SettingsTestTsPacket:
		"""SCPI: [SOURce<HW>]:BB:DVBC:TSPacket \n
		Snippet: value: enums.SettingsTestTsPacket = driver.source.bb.dvbc.get_ts_packet() \n
		Specifies the structure of the test transport stream packet that is fed to the modulator. \n
			:return: set_ts_packet: H184| S187 H184 Head/184 Payload S187 Sync/187 Payload
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBC:TSPacket?')
		return Conversions.str_to_scalar_enum(response, enums.SettingsTestTsPacket)

	def set_ts_packet(self, set_ts_packet: enums.SettingsTestTsPacket) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBC:TSPacket \n
		Snippet: driver.source.bb.dvbc.set_ts_packet(set_ts_packet = enums.SettingsTestTsPacket.H184) \n
		Specifies the structure of the test transport stream packet that is fed to the modulator. \n
			:param set_ts_packet: H184| S187 H184 Head/184 Payload S187 Sync/187 Payload
		"""
		param = Conversions.enum_scalar_to_str(set_ts_packet, enums.SettingsTestTsPacket)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBC:TSPacket {param}')

	def clone(self) -> 'Dvbc':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dvbc(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
