from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dvbs2:
	"""Dvbs2 commands group definition. 41 total commands, 8 Subgroups, 10 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dvbs2", core, parent)

	@property
	def inputPy(self):
		"""inputPy commands group. 1 Sub-classes, 2 commands."""
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
	def s2X(self):
		"""s2X commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_s2X'):
			from .S2X import S2X
			self._s2X = S2X(self._core, self._cmd_group)
		return self._s2X

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
	def tsl(self):
		"""tsl commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_tsl'):
			from .Tsl import Tsl
			self._tsl = Tsl(self._core, self._cmd_group)
		return self._tsl

	@property
	def isPy(self):
		"""isPy commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_isPy'):
			from .IsPy import IsPy
			self._isPy = IsPy(self._core, self._cmd_group)
		return self._isPy

	@property
	def special(self):
		"""special commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_special'):
			from .Special import Special
			self._special = Special(self._core, self._cmd_group)
		return self._special

	def get_annm(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:ANNM \n
		Snippet: value: bool = driver.source.bb.dvbs2.get_annm() \n
		Enables the annex M features as specified in . Depending on this setting, a different PL header is used. \n
			:return: annex_n: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBS2:ANNM?')
		return Conversions.str_to_bool(response)

	def set_annm(self, annex_n: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:ANNM \n
		Snippet: driver.source.bb.dvbs2.set_annm(annex_n = False) \n
		Enables the annex M features as specified in . Depending on this setting, a different PL header is used. \n
			:param annex_n: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(annex_n)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS2:ANNM {param}')

	def get_ntsl(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:NTSL \n
		Snippet: value: float = driver.source.bb.dvbs2.get_ntsl() \n
		No command help available \n
			:return: num_time_slice: float Range: 1 to 8
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBS2:NTSL?')
		return Conversions.str_to_float(response)

	def set_ntsl(self, num_time_slice: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:NTSL \n
		Snippet: driver.source.bb.dvbs2.set_ntsl(num_time_slice = 1.0) \n
		No command help available \n
			:param num_time_slice: float Range: 1 to 8
		"""
		param = Conversions.decimal_value_to_str(num_time_slice)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS2:NTSL {param}')

	# noinspection PyTypeChecker
	def get_payload(self) -> enums.PayloadTestStuff:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:PAYLoad \n
		Snippet: value: enums.PayloadTestStuff = driver.source.bb.dvbs2.get_payload() \n
		Defines the payload area content of the packet. \n
			:return: payload: HFF| H00| PRBS
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBS2:PAYLoad?')
		return Conversions.str_to_scalar_enum(response, enums.PayloadTestStuff)

	def set_payload(self, payload: enums.PayloadTestStuff) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:PAYLoad \n
		Snippet: driver.source.bb.dvbs2.set_payload(payload = enums.PayloadTestStuff.H00) \n
		Defines the payload area content of the packet. \n
			:param payload: HFF| H00| PRBS
		"""
		param = Conversions.enum_scalar_to_str(payload, enums.PayloadTestStuff)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS2:PAYLoad {param}')

	def get_pid(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:PID \n
		Snippet: value: float = driver.source.bb.dvbs2.get_pid() \n
		Sets the . \n
			:return: pid: float Range: #H0 to #HFFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBS2:PID?')
		return Conversions.str_to_float(response)

	def set_pid(self, pid: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:PID \n
		Snippet: driver.source.bb.dvbs2.set_pid(pid = 1.0) \n
		Sets the . \n
			:param pid: float Range: #H0 to #HFFF
		"""
		param = Conversions.decimal_value_to_str(pid)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS2:PID {param}')

	# noinspection PyTypeChecker
	def get_pid_test_pack(self) -> enums.PidTestPacket:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:PIDTestpack \n
		Snippet: value: enums.PidTestPacket = driver.source.bb.dvbs2.get_pid_test_pack() \n
		If a header is present in the test packet ('Test TS Packet > Head/184 Payload') , you can specify a fixed or variable
		packet identifier (PID) . \n
			:return: pid_test_packet: VARiable| NULL
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBS2:PIDTestpack?')
		return Conversions.str_to_scalar_enum(response, enums.PidTestPacket)

	def set_pid_test_pack(self, pid_test_packet: enums.PidTestPacket) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:PIDTestpack \n
		Snippet: driver.source.bb.dvbs2.set_pid_test_pack(pid_test_packet = enums.PidTestPacket.NULL) \n
		If a header is present in the test packet ('Test TS Packet > Head/184 Payload') , you can specify a fixed or variable
		packet identifier (PID) . \n
			:param pid_test_packet: VARiable| NULL
		"""
		param = Conversions.enum_scalar_to_str(pid_test_packet, enums.PidTestPacket)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS2:PIDTestpack {param}')

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:PRESet \n
		Snippet: driver.source.bb.dvbs2.preset() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:DVBS2:STATe. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS2:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:PRESet \n
		Snippet: driver.source.bb.dvbs2.preset_with_opc() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:DVBS2:STATe. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmcv.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:DVBS2:PRESet', opc_timeout_ms)

	# noinspection PyTypeChecker
	def get_rolloff(self) -> enums.Dvbs2CodingRolloff:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:ROLLoff \n
		Snippet: value: enums.Dvbs2CodingRolloff = driver.source.bb.dvbs2.get_rolloff() \n
		Sets the roll-off alpha factor value. \n
			:return: rolloff: 0.35| 0.25| 0.20| 0.15| 0.10| 0.05
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBS2:ROLLoff?')
		return Conversions.str_to_scalar_enum(response, enums.Dvbs2CodingRolloff)

	def set_rolloff(self, rolloff: enums.Dvbs2CodingRolloff) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:ROLLoff \n
		Snippet: driver.source.bb.dvbs2.set_rolloff(rolloff = enums.Dvbs2CodingRolloff._0_dot_05) \n
		Sets the roll-off alpha factor value. \n
			:param rolloff: 0.35| 0.25| 0.20| 0.15| 0.10| 0.05
		"""
		param = Conversions.enum_scalar_to_str(rolloff, enums.Dvbs2CodingRolloff)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS2:ROLLoff {param}')

	# noinspection PyTypeChecker
	def get_source(self) -> enums.CodingInputSignalSource:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:SOURce \n
		Snippet: value: enums.CodingInputSignalSource = driver.source.bb.dvbs2.get_source() \n
		Sets the modulation source for the input signal. \n
			:return: source: EXTernal| TSPLayer| TESTsignal
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBS2:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.CodingInputSignalSource)

	def set_source(self, source: enums.CodingInputSignalSource) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:SOURce \n
		Snippet: driver.source.bb.dvbs2.set_source(source = enums.CodingInputSignalSource.EXTernal) \n
		Sets the modulation source for the input signal. \n
			:param source: EXTernal| TSPLayer| TESTsignal
		"""
		param = Conversions.enum_scalar_to_str(source, enums.CodingInputSignalSource)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS2:SOURce {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:STATe \n
		Snippet: value: bool = driver.source.bb.dvbs2.get_state() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBS2:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:STATe \n
		Snippet: driver.source.bb.dvbs2.set_state(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS2:STATe {param}')

	# noinspection PyTypeChecker
	def get_ts_packet(self) -> enums.SettingsTestTsPacket:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:TSPacket \n
		Snippet: value: enums.SettingsTestTsPacket = driver.source.bb.dvbs2.get_ts_packet() \n
		Specifies the structure of the test transport stream packet that is fed to the modulator. \n
			:return: ts_packet: H184| S187
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBS2:TSPacket?')
		return Conversions.str_to_scalar_enum(response, enums.SettingsTestTsPacket)

	def set_ts_packet(self, ts_packet: enums.SettingsTestTsPacket) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:TSPacket \n
		Snippet: driver.source.bb.dvbs2.set_ts_packet(ts_packet = enums.SettingsTestTsPacket.H184) \n
		Specifies the structure of the test transport stream packet that is fed to the modulator. \n
			:param ts_packet: H184| S187
		"""
		param = Conversions.enum_scalar_to_str(ts_packet, enums.SettingsTestTsPacket)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS2:TSPacket {param}')

	def clone(self) -> 'Dvbs2':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dvbs2(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
