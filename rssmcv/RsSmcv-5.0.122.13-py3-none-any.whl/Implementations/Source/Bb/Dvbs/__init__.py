from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dvbs:
	"""Dvbs commands group definition. 27 total commands, 4 Subgroups, 15 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dvbs", core, parent)

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
	def get_constel(self) -> enums.DvbsCodingDvbsCodingConstel:
		"""SCPI: [SOURce<HW>]:BB:DVBS:CONStel \n
		Snippet: value: enums.DvbsCodingDvbsCodingConstel = driver.source.bb.dvbs.get_constel() \n
		Defines the constellation. \n
			:return: constel: S4| S8| S16 S4 S8 8 S16 16
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBS:CONStel?')
		return Conversions.str_to_scalar_enum(response, enums.DvbsCodingDvbsCodingConstel)

	def set_constel(self, constel: enums.DvbsCodingDvbsCodingConstel) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS:CONStel \n
		Snippet: driver.source.bb.dvbs.set_constel(constel = enums.DvbsCodingDvbsCodingConstel.S16) \n
		Defines the constellation. \n
			:param constel: S4| S8| S16 S4 S8 8 S16 16
		"""
		param = Conversions.enum_scalar_to_str(constel, enums.DvbsCodingDvbsCodingConstel)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS:CONStel {param}')

	# noinspection PyTypeChecker
	def get_packet_length(self) -> enums.DvbxCodingInputSignalPacketLength:
		"""SCPI: [SOURce<HW>]:BB:DVBS:PACKetlength \n
		Snippet: value: enums.DvbxCodingInputSignalPacketLength = driver.source.bb.dvbs.get_packet_length() \n
		Queries the packet length of the external transport stream in bytes. \n
			:return: inp_sig_plength: P188| P204| INValid P188|P204 188/204 byte packets specified for serial input and parallel input. INValid Packet length does not match the specified length.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBS:PACKetlength?')
		return Conversions.str_to_scalar_enum(response, enums.DvbxCodingInputSignalPacketLength)

	# noinspection PyTypeChecker
	def get_payload(self) -> enums.PayloadTestStuff:
		"""SCPI: [SOURce<HW>]:BB:DVBS:PAYLoad \n
		Snippet: value: enums.PayloadTestStuff = driver.source.bb.dvbs.get_payload() \n
		Defines the payload area content of the packet. \n
			:return: set_payload: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBS:PAYLoad?')
		return Conversions.str_to_scalar_enum(response, enums.PayloadTestStuff)

	def set_payload(self, set_payload: enums.PayloadTestStuff) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS:PAYLoad \n
		Snippet: driver.source.bb.dvbs.set_payload(set_payload = enums.PayloadTestStuff.H00) \n
		Defines the payload area content of the packet. \n
			:param set_payload: HFF| H00| PRBS
		"""
		param = Conversions.enum_scalar_to_str(set_payload, enums.PayloadTestStuff)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS:PAYLoad {param}')

	def get_pid(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVBS:PID \n
		Snippet: value: int = driver.source.bb.dvbs.get_pid() \n
		Sets the . \n
			:return: set_pid: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBS:PID?')
		return Conversions.str_to_int(response)

	def set_pid(self, set_pid: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS:PID \n
		Snippet: driver.source.bb.dvbs.set_pid(set_pid = 1) \n
		Sets the . \n
			:param set_pid: float Range: #H0 to #HFFF
		"""
		param = Conversions.decimal_value_to_str(set_pid)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS:PID {param}')

	# noinspection PyTypeChecker
	def get_pid_test_pack(self) -> enums.PidTestPacket:
		"""SCPI: [SOURce<HW>]:BB:DVBS:PIDTestpack \n
		Snippet: value: enums.PidTestPacket = driver.source.bb.dvbs.get_pid_test_pack() \n
		If a header is present in the test packet ('Test TS Packet > Head/184 Payload') , you can specify a fixed or variable
		packet identifier (PID) . \n
			:return: set_pid_testpack: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBS:PIDTestpack?')
		return Conversions.str_to_scalar_enum(response, enums.PidTestPacket)

	def set_pid_test_pack(self, set_pid_testpack: enums.PidTestPacket) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS:PIDTestpack \n
		Snippet: driver.source.bb.dvbs.set_pid_test_pack(set_pid_testpack = enums.PidTestPacket.NULL) \n
		If a header is present in the test packet ('Test TS Packet > Head/184 Payload') , you can specify a fixed or variable
		packet identifier (PID) . \n
			:param set_pid_testpack: VARiable| NULL
		"""
		param = Conversions.enum_scalar_to_str(set_pid_testpack, enums.PidTestPacket)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS:PIDTestpack {param}')

	# noinspection PyTypeChecker
	def get_prbs(self) -> enums.SettingsPrbs:
		"""SCPI: [SOURce<HW>]:BB:DVBS:PRBS \n
		Snippet: value: enums.SettingsPrbs = driver.source.bb.dvbs.get_prbs() \n
		Sets the length of the PRBS sequence. You can select a PRBS 15 or a PRBS 23 sequence as specified by . \n
			:return: set_prbs: P23_1| P15_1
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBS:PRBS?')
		return Conversions.str_to_scalar_enum(response, enums.SettingsPrbs)

	def set_prbs(self, set_prbs: enums.SettingsPrbs) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS:PRBS \n
		Snippet: driver.source.bb.dvbs.set_prbs(set_prbs = enums.SettingsPrbs.P15_1) \n
		Sets the length of the PRBS sequence. You can select a PRBS 15 or a PRBS 23 sequence as specified by . \n
			:param set_prbs: P23_1| P15_1
		"""
		param = Conversions.enum_scalar_to_str(set_prbs, enums.SettingsPrbs)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS:PRBS {param}')

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS:PRESet \n
		Snippet: driver.source.bb.dvbs.preset() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:DVBS2:STATe. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS:PRESet \n
		Snippet: driver.source.bb.dvbs.preset_with_opc() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:DVBS2:STATe. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmcv.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:DVBS:PRESet', opc_timeout_ms)

	# noinspection PyTypeChecker
	def get_rate(self) -> enums.DvbsCodingDvbsCodingCoderate:
		"""SCPI: [SOURce<HW>]:BB:DVBS:RATE \n
		Snippet: value: enums.DvbsCodingDvbsCodingCoderate = driver.source.bb.dvbs.get_rate() \n
		Defines the code rate. The available code rates depend on the value of [:SOURce<hw>]:BB:DVBS:CONStel. \n
			:return: coderate: R1_2| R2_3| R3_4| R5_6| R7_8| R8_9
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBS:RATE?')
		return Conversions.str_to_scalar_enum(response, enums.DvbsCodingDvbsCodingCoderate)

	def set_rate(self, coderate: enums.DvbsCodingDvbsCodingCoderate) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS:RATE \n
		Snippet: driver.source.bb.dvbs.set_rate(coderate = enums.DvbsCodingDvbsCodingCoderate.R1_2) \n
		Defines the code rate. The available code rates depend on the value of [:SOURce<hw>]:BB:DVBS:CONStel. \n
			:param coderate: R1_2| R2_3| R3_4| R5_6| R7_8| R8_9
		"""
		param = Conversions.enum_scalar_to_str(coderate, enums.DvbsCodingDvbsCodingCoderate)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS:RATE {param}')

	# noinspection PyTypeChecker
	def get_rolloff(self) -> enums.DvbsCodingDvbsCodingRolloff:
		"""SCPI: [SOURce<HW>]:BB:DVBS:ROLLoff \n
		Snippet: value: enums.DvbsCodingDvbsCodingRolloff = driver.source.bb.dvbs.get_rolloff() \n
		Sets the roll-off alpha factor value. \n
			:return: rolloff: 0.35| 0.25| 0.20| 0.15| 0.10| 0.05
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBS:ROLLoff?')
		return Conversions.str_to_scalar_enum(response, enums.DvbsCodingDvbsCodingRolloff)

	def set_rolloff(self, rolloff: enums.DvbsCodingDvbsCodingRolloff) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS:ROLLoff \n
		Snippet: driver.source.bb.dvbs.set_rolloff(rolloff = enums.DvbsCodingDvbsCodingRolloff._0_dot_20) \n
		Sets the roll-off alpha factor value. \n
			:param rolloff: 0.35| 0.25| 0.20| 0.15| 0.10| 0.05
		"""
		param = Conversions.enum_scalar_to_str(rolloff, enums.DvbsCodingDvbsCodingRolloff)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS:ROLLoff {param}')

	# noinspection PyTypeChecker
	def get_source(self) -> enums.CodingInputSignalSource:
		"""SCPI: [SOURce<HW>]:BB:DVBS:SOURce \n
		Snippet: value: enums.CodingInputSignalSource = driver.source.bb.dvbs.get_source() \n
		Sets the modulation source for the input signal. \n
			:return: inp_sig_source: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBS:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.CodingInputSignalSource)

	def set_source(self, inp_sig_source: enums.CodingInputSignalSource) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS:SOURce \n
		Snippet: driver.source.bb.dvbs.set_source(inp_sig_source = enums.CodingInputSignalSource.EXTernal) \n
		Sets the modulation source for the input signal. \n
			:param inp_sig_source: EXTernal| TSPLayer| TESTsignal
		"""
		param = Conversions.enum_scalar_to_str(inp_sig_source, enums.CodingInputSignalSource)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS:SOURce {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVBS:STATe \n
		Snippet: value: bool = driver.source.bb.dvbs.get_state() \n
		Enables/disables the DVB-S standard. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBS:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS:STATe \n
		Snippet: driver.source.bb.dvbs.set_state(state = False) \n
		Enables/disables the DVB-S standard. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS:STATe {param}')

	def get_stuffing(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVBS:STUFfing \n
		Snippet: value: bool = driver.source.bb.dvbs.get_stuffing() \n
		Queries the stuffing state that is active. \n
			:return: inp_sig_stuffing: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBS:STUFfing?')
		return Conversions.str_to_bool(response)

	def get_symbols(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVBS:SYMBols \n
		Snippet: value: int = driver.source.bb.dvbs.get_symbols() \n
		Sets the symbol rate. \n
			:return: symbol_rate: integer Range: 1.00E+05 to 9.00E+07
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBS:SYMBols?')
		return Conversions.str_to_int(response)

	def set_symbols(self, symbol_rate: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS:SYMBols \n
		Snippet: driver.source.bb.dvbs.set_symbols(symbol_rate = 1) \n
		Sets the symbol rate. \n
			:param symbol_rate: integer Range: 1.00E+05 to 9.00E+07
		"""
		param = Conversions.decimal_value_to_str(symbol_rate)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS:SYMBols {param}')

	# noinspection PyTypeChecker
	def get_test_signal(self) -> enums.DvbsCodingDvbsInputSignalTestSignal:
		"""SCPI: [SOURce<HW>]:BB:DVBS:TESTsignal \n
		Snippet: value: enums.DvbsCodingDvbsInputSignalTestSignal = driver.source.bb.dvbs.get_test_signal() \n
		Defines the test signal data. \n
			:return: inp_sig_test_sig: TTSP| PBEC TTSP Test TS packet with standardized packet data used as modulation data in the transport stream. PBEC PRBS before convolutional encoder Pure pseudo-random bit sequence (PRBS) data used as modulation data with no packet structure. The sequence is inserted before the convolutional encoder. PRBS data conforms with specification.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBS:TESTsignal?')
		return Conversions.str_to_scalar_enum(response, enums.DvbsCodingDvbsInputSignalTestSignal)

	def set_test_signal(self, inp_sig_test_sig: enums.DvbsCodingDvbsInputSignalTestSignal) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS:TESTsignal \n
		Snippet: driver.source.bb.dvbs.set_test_signal(inp_sig_test_sig = enums.DvbsCodingDvbsInputSignalTestSignal.PBEC) \n
		Defines the test signal data. \n
			:param inp_sig_test_sig: TTSP| PBEC TTSP Test TS packet with standardized packet data used as modulation data in the transport stream. PBEC PRBS before convolutional encoder Pure pseudo-random bit sequence (PRBS) data used as modulation data with no packet structure. The sequence is inserted before the convolutional encoder. PRBS data conforms with specification.
		"""
		param = Conversions.enum_scalar_to_str(inp_sig_test_sig, enums.DvbsCodingDvbsInputSignalTestSignal)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS:TESTsignal {param}')

	# noinspection PyTypeChecker
	def get_ts_packet(self) -> enums.SettingsTestTsPacket:
		"""SCPI: [SOURce<HW>]:BB:DVBS:TSPacket \n
		Snippet: value: enums.SettingsTestTsPacket = driver.source.bb.dvbs.get_ts_packet() \n
		Specifies the structure of the test transport stream packet that is fed to the modulator. \n
			:return: set_ts_packet: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBS:TSPacket?')
		return Conversions.str_to_scalar_enum(response, enums.SettingsTestTsPacket)

	def set_ts_packet(self, set_ts_packet: enums.SettingsTestTsPacket) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS:TSPacket \n
		Snippet: driver.source.bb.dvbs.set_ts_packet(set_ts_packet = enums.SettingsTestTsPacket.H184) \n
		Specifies the structure of the test transport stream packet that is fed to the modulator. \n
			:param set_ts_packet: H184| S187
		"""
		param = Conversions.enum_scalar_to_str(set_ts_packet, enums.SettingsTestTsPacket)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS:TSPacket {param}')

	def clone(self) -> 'Dvbs':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dvbs(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
