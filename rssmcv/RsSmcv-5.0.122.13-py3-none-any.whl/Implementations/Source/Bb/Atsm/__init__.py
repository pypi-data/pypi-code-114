from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Atsm:
	"""Atsm commands group definition. 34 total commands, 9 Subgroups, 17 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("atsm", core, parent)

	@property
	def bury(self):
		"""bury commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bury'):
			from .Bury import Bury
			self._bury = Bury(self._core, self._cmd_group)
		return self._bury

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	@property
	def inputPy(self):
		"""inputPy commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_inputPy'):
			from .InputPy import InputPy
			self._inputPy = InputPy(self._core, self._cmd_group)
		return self._inputPy

	@property
	def mtxId(self):
		"""mtxId commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_mtxId'):
			from .MtxId import MtxId
			self._mtxId = MtxId(self._core, self._cmd_group)
		return self._mtxId

	@property
	def network(self):
		"""network commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_network'):
			from .Network import Network
			self._network = Network(self._core, self._cmd_group)
		return self._network

	@property
	def setting(self):
		"""setting commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_setting'):
			from .Setting import Setting
			self._setting = Setting(self._core, self._cmd_group)
		return self._setting

	@property
	def symbols(self):
		"""symbols commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_symbols'):
			from .Symbols import Symbols
			self._symbols = Symbols(self._core, self._cmd_group)
		return self._symbols

	@property
	def tx(self):
		"""tx commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tx'):
			from .Tx import Tx
			self._tx = Tx(self._core, self._cmd_group)
		return self._tx

	@property
	def useful(self):
		"""useful commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_useful'):
			from .Useful import Useful
			self._useful = Useful(self._core, self._cmd_group)
		return self._useful

	# noinspection PyTypeChecker
	def get_constel(self) -> enums.AtscmhCodingConstel:
		"""SCPI: [SOURce<HW>]:BB:ATSM:CONStel \n
		Snippet: value: enums.AtscmhCodingConstel = driver.source.bb.atsm.get_constel() \n
		Queries the constellation. \n
			:return: constellation: VSB8
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ATSM:CONStel?')
		return Conversions.str_to_scalar_enum(response, enums.AtscmhCodingConstel)

	def get_mhe_pid(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ATSM:MHEPid \n
		Snippet: value: int = driver.source.bb.atsm.get_mhe_pid() \n
		Sets the PID of MPEG-2 packets that contain ATSC M/H data. The PID is a four-digit value in hexadecimal format. \n
			:return: mhe_pid: integer Range: 0 to 8191
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ATSM:MHEPid?')
		return Conversions.str_to_int(response)

	def set_mhe_pid(self, mhe_pid: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ATSM:MHEPid \n
		Snippet: driver.source.bb.atsm.set_mhe_pid(mhe_pid = 1) \n
		Sets the PID of MPEG-2 packets that contain ATSC M/H data. The PID is a four-digit value in hexadecimal format. \n
			:param mhe_pid: integer Range: 0 to 8191
		"""
		param = Conversions.decimal_value_to_str(mhe_pid)
		self._core.io.write(f'SOURce<HwInstance>:BB:ATSM:MHEPid {param}')

	def get_mh_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ATSM:MHSTate \n
		Snippet: value: bool = driver.source.bb.atsm.get_mh_state() \n
		Enables/disableses all ATSC-M/H elements of the . \n
			:return: mh_state: 1| ON| 0| OFF ON ATSC-M/H-compliant output signal OFF 8VSB state, output signal complies with the ATSC digital television standard (A/53)
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ATSM:MHSTate?')
		return Conversions.str_to_bool(response)

	def set_mh_state(self, mh_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:ATSM:MHSTate \n
		Snippet: driver.source.bb.atsm.set_mh_state(mh_state = False) \n
		Enables/disableses all ATSC-M/H elements of the . \n
			:param mh_state: 1| ON| 0| OFF ON ATSC-M/H-compliant output signal OFF 8VSB state, output signal complies with the ATSC digital television standard (A/53)
		"""
		param = Conversions.bool_to_str(mh_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:ATSM:MHSTate {param}')

	# noinspection PyTypeChecker
	def get_packet_length(self) -> enums.AtscmhCodingInputSignalPacketLength:
		"""SCPI: [SOURce<HW>]:BB:ATSM:PACKetlength \n
		Snippet: value: enums.AtscmhCodingInputSignalPacketLength = driver.source.bb.atsm.get_packet_length() \n
		Queries the packet length of the external transport stream in bytes. \n
			:return: packet_length: P188| P208| INValid P188|P208 188/208 byte packets specified for serial input and parallel input. INValid Packet length does not match the specified length.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ATSM:PACKetlength?')
		return Conversions.str_to_scalar_enum(response, enums.AtscmhCodingInputSignalPacketLength)

	# noinspection PyTypeChecker
	def get_payload(self) -> enums.PayloadTestStuff:
		"""SCPI: [SOURce<HW>]:BB:ATSM:PAYLoad \n
		Snippet: value: enums.PayloadTestStuff = driver.source.bb.atsm.get_payload() \n
		Defines the payload area content of the packet. \n
			:return: payload: HFF| H00| PRBS
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ATSM:PAYLoad?')
		return Conversions.str_to_scalar_enum(response, enums.PayloadTestStuff)

	def set_payload(self, payload: enums.PayloadTestStuff) -> None:
		"""SCPI: [SOURce<HW>]:BB:ATSM:PAYLoad \n
		Snippet: driver.source.bb.atsm.set_payload(payload = enums.PayloadTestStuff.H00) \n
		Defines the payload area content of the packet. \n
			:param payload: HFF| H00| PRBS
		"""
		param = Conversions.enum_scalar_to_str(payload, enums.PayloadTestStuff)
		self._core.io.write(f'SOURce<HwInstance>:BB:ATSM:PAYLoad {param}')

	def get_pid(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ATSM:PID \n
		Snippet: value: int = driver.source.bb.atsm.get_pid() \n
		Sets the . \n
			:return: pid: integer Range: 0 to 8191
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ATSM:PID?')
		return Conversions.str_to_int(response)

	def set_pid(self, pid: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ATSM:PID \n
		Snippet: driver.source.bb.atsm.set_pid(pid = 1) \n
		Sets the . \n
			:param pid: integer Range: 0 to 8191
		"""
		param = Conversions.decimal_value_to_str(pid)
		self._core.io.write(f'SOURce<HwInstance>:BB:ATSM:PID {param}')

	# noinspection PyTypeChecker
	def get_pid_test_pack(self) -> enums.PidTestPacket:
		"""SCPI: [SOURce<HW>]:BB:ATSM:PIDTestpack \n
		Snippet: value: enums.PidTestPacket = driver.source.bb.atsm.get_pid_test_pack() \n
		If a header is present in the test packet ('Test TS Packet > Head/184 Payload') , you can specify a fixed or variable
		packet identifier (PID) . \n
			:return: pid_test_pack: NULL| VARiable
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ATSM:PIDTestpack?')
		return Conversions.str_to_scalar_enum(response, enums.PidTestPacket)

	def set_pid_test_pack(self, pid_test_pack: enums.PidTestPacket) -> None:
		"""SCPI: [SOURce<HW>]:BB:ATSM:PIDTestpack \n
		Snippet: driver.source.bb.atsm.set_pid_test_pack(pid_test_pack = enums.PidTestPacket.NULL) \n
		If a header is present in the test packet ('Test TS Packet > Head/184 Payload') , you can specify a fixed or variable
		packet identifier (PID) . \n
			:param pid_test_pack: NULL| VARiable
		"""
		param = Conversions.enum_scalar_to_str(pid_test_pack, enums.PidTestPacket)
		self._core.io.write(f'SOURce<HwInstance>:BB:ATSM:PIDTestpack {param}')

	# noinspection PyTypeChecker
	def get_prbs(self) -> enums.SettingsPrbs:
		"""SCPI: [SOURce<HW>]:BB:ATSM:PRBS \n
		Snippet: value: enums.SettingsPrbs = driver.source.bb.atsm.get_prbs() \n
		Sets the length of the PRBS sequence. You can select a PRBS 15 or a PRBS 23 sequence as specified by . \n
			:return: prbs: P23_1| P15_1
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ATSM:PRBS?')
		return Conversions.str_to_scalar_enum(response, enums.SettingsPrbs)

	def set_prbs(self, prbs: enums.SettingsPrbs) -> None:
		"""SCPI: [SOURce<HW>]:BB:ATSM:PRBS \n
		Snippet: driver.source.bb.atsm.set_prbs(prbs = enums.SettingsPrbs.P15_1) \n
		Sets the length of the PRBS sequence. You can select a PRBS 15 or a PRBS 23 sequence as specified by . \n
			:param prbs: P23_1| P15_1
		"""
		param = Conversions.enum_scalar_to_str(prbs, enums.SettingsPrbs)
		self._core.io.write(f'SOURce<HwInstance>:BB:ATSM:PRBS {param}')

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:ATSM:PRESet \n
		Snippet: driver.source.bb.atsm.preset() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:ATSM:STATe. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:ATSM:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:ATSM:PRESet \n
		Snippet: driver.source.bb.atsm.preset_with_opc() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:ATSM:STATe. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmcv.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:ATSM:PRESet', opc_timeout_ms)

	# noinspection PyTypeChecker
	def get_rolloff(self) -> enums.AtscmhCodingRolloff:
		"""SCPI: [SOURce<HW>]:BB:ATSM:ROLLoff \n
		Snippet: value: enums.AtscmhCodingRolloff = driver.source.bb.atsm.get_rolloff() \n
		Queries the roll-off factor alpha (α) . \n
			:return: rolloff: R115
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ATSM:ROLLoff?')
		return Conversions.str_to_scalar_enum(response, enums.AtscmhCodingRolloff)

	# noinspection PyTypeChecker
	def get_source(self) -> enums.CodingInputSignalSource:
		"""SCPI: [SOURce<HW>]:BB:ATSM:SOURce \n
		Snippet: value: enums.CodingInputSignalSource = driver.source.bb.atsm.get_source() \n
		Sets the modulation source for the input signal. \n
			:return: atscmh_source: EXTernal| TSPLayer| TESTsignal
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ATSM:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.CodingInputSignalSource)

	def set_source(self, atscmh_source: enums.CodingInputSignalSource) -> None:
		"""SCPI: [SOURce<HW>]:BB:ATSM:SOURce \n
		Snippet: driver.source.bb.atsm.set_source(atscmh_source = enums.CodingInputSignalSource.EXTernal) \n
		Sets the modulation source for the input signal. \n
			:param atscmh_source: EXTernal| TSPLayer| TESTsignal
		"""
		param = Conversions.enum_scalar_to_str(atscmh_source, enums.CodingInputSignalSource)
		self._core.io.write(f'SOURce<HwInstance>:BB:ATSM:SOURce {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ATSM:STATe \n
		Snippet: value: bool = driver.source.bb.atsm.get_state() \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ATSM:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:ATSM:STATe \n
		Snippet: driver.source.bb.atsm.set_state(state = False) \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:ATSM:STATe {param}')

	def get_stuffing(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ATSM:STUFfing \n
		Snippet: value: bool = driver.source.bb.atsm.get_stuffing() \n
		Activates stuffing. \n
			:return: stuffing: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ATSM:STUFfing?')
		return Conversions.str_to_bool(response)

	def set_stuffing(self, stuffing: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:ATSM:STUFfing \n
		Snippet: driver.source.bb.atsm.set_stuffing(stuffing = False) \n
		Activates stuffing. \n
			:param stuffing: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(stuffing)
		self._core.io.write(f'SOURce<HwInstance>:BB:ATSM:STUFfing {param}')

	# noinspection PyTypeChecker
	def get_test_signal(self) -> enums.AtscmhInputSignalTestSignal:
		"""SCPI: [SOURce<HW>]:BB:ATSM:TESTsignal \n
		Snippet: value: enums.AtscmhInputSignalTestSignal = driver.source.bb.atsm.get_test_signal() \n
		Defines the test signal data. \n
			:return: test_signal: TTSP| PBIN| PBET| PBEM TTSP Test TS packet with standardized packet data used as modulation data in the transport stream. PBIN PRBS before interleaver. Pure pseudo-random bit sequence (PRBS) data used as modulation data with no packet structure. PRBS data conforms with specification. PBET PRBS before trellis. Pure pseudo-random bit sequence (PRBS) data used as modulation data with no packet structure and interleaving. Modulation data is directly fed to the trellis encoder. PBEM PRBS before mapper. Pure pseudo-random bit sequence (PRBS) data directly fed to the mapper. Three bits at a time in two's complement are assigned to the stages -7, -5, -3, -1, 1, 3, 5, 7. Subsequent pilot insertion and VSB filtering remain unaffected.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ATSM:TESTsignal?')
		return Conversions.str_to_scalar_enum(response, enums.AtscmhInputSignalTestSignal)

	def set_test_signal(self, test_signal: enums.AtscmhInputSignalTestSignal) -> None:
		"""SCPI: [SOURce<HW>]:BB:ATSM:TESTsignal \n
		Snippet: driver.source.bb.atsm.set_test_signal(test_signal = enums.AtscmhInputSignalTestSignal.PBEM) \n
		Defines the test signal data. \n
			:param test_signal: TTSP| PBIN| PBET| PBEM TTSP Test TS packet with standardized packet data used as modulation data in the transport stream. PBIN PRBS before interleaver. Pure pseudo-random bit sequence (PRBS) data used as modulation data with no packet structure. PRBS data conforms with specification. PBET PRBS before trellis. Pure pseudo-random bit sequence (PRBS) data used as modulation data with no packet structure and interleaving. Modulation data is directly fed to the trellis encoder. PBEM PRBS before mapper. Pure pseudo-random bit sequence (PRBS) data directly fed to the mapper. Three bits at a time in two's complement are assigned to the stages -7, -5, -3, -1, 1, 3, 5, 7. Subsequent pilot insertion and VSB filtering remain unaffected.
		"""
		param = Conversions.enum_scalar_to_str(test_signal, enums.AtscmhInputSignalTestSignal)
		self._core.io.write(f'SOURce<HwInstance>:BB:ATSM:TESTsignal {param}')

	def get_transmission(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ATSM:TRANsmission \n
		Snippet: value: bool = driver.source.bb.atsm.get_transmission() \n
		Enables/disables transmission. \n
			:return: transmission: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ATSM:TRANsmission?')
		return Conversions.str_to_bool(response)

	def set_transmission(self, transmission: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:ATSM:TRANsmission \n
		Snippet: driver.source.bb.atsm.set_transmission(transmission = False) \n
		Enables/disables transmission. \n
			:param transmission: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(transmission)
		self._core.io.write(f'SOURce<HwInstance>:BB:ATSM:TRANsmission {param}')

	# noinspection PyTypeChecker
	def get_ts_packet(self) -> enums.SettingsTestTsPacket:
		"""SCPI: [SOURce<HW>]:BB:ATSM:TSPacket \n
		Snippet: value: enums.SettingsTestTsPacket = driver.source.bb.atsm.get_ts_packet() \n
		Specifies the structure of the test transport stream packet that is fed to the modulator. \n
			:return: ts_packet: H184| S187
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ATSM:TSPacket?')
		return Conversions.str_to_scalar_enum(response, enums.SettingsTestTsPacket)

	def set_ts_packet(self, ts_packet: enums.SettingsTestTsPacket) -> None:
		"""SCPI: [SOURce<HW>]:BB:ATSM:TSPacket \n
		Snippet: driver.source.bb.atsm.set_ts_packet(ts_packet = enums.SettingsTestTsPacket.H184) \n
		Specifies the structure of the test transport stream packet that is fed to the modulator. \n
			:param ts_packet: H184| S187
		"""
		param = Conversions.enum_scalar_to_str(ts_packet, enums.SettingsTestTsPacket)
		self._core.io.write(f'SOURce<HwInstance>:BB:ATSM:TSPacket {param}')

	def get_watermark(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ATSM:WATermark \n
		Snippet: value: bool = driver.source.bb.atsm.get_watermark() \n
		Enables/disables the RF watermark. \n
			:return: watermark: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ATSM:WATermark?')
		return Conversions.str_to_bool(response)

	def set_watermark(self, watermark: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:ATSM:WATermark \n
		Snippet: driver.source.bb.atsm.set_watermark(watermark = False) \n
		Enables/disables the RF watermark. \n
			:param watermark: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(watermark)
		self._core.io.write(f'SOURce<HwInstance>:BB:ATSM:WATermark {param}')

	def clone(self) -> 'Atsm':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Atsm(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
