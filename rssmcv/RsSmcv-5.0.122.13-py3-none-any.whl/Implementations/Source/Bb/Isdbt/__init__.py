from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Isdbt:
	"""Isdbt commands group definition. 71 total commands, 17 Subgroups, 14 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("isdbt", core, parent)

	@property
	def channel(self):
		"""channel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_channel'):
			from .Channel import Channel
			self._channel = Channel(self._core, self._cmd_group)
		return self._channel

	@property
	def constel(self):
		"""constel commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_constel'):
			from .Constel import Constel
			self._constel = Constel(self._core, self._cmd_group)
		return self._constel

	@property
	def eew(self):
		"""eew commands group. 9 Sub-classes, 4 commands."""
		if not hasattr(self, '_eew'):
			from .Eew import Eew
			self._eew = Eew(self._core, self._cmd_group)
		return self._eew

	@property
	def fft(self):
		"""fft commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fft'):
			from .Fft import Fft
			self._fft = Fft(self._core, self._cmd_group)
		return self._fft

	@property
	def iip(self):
		"""iip commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_iip'):
			from .Iip import Iip
			self._iip = Iip(self._core, self._cmd_group)
		return self._iip

	@property
	def inputPy(self):
		"""inputPy commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_inputPy'):
			from .InputPy import InputPy
			self._inputPy = InputPy(self._core, self._cmd_group)
		return self._inputPy

	@property
	def payload(self):
		"""payload commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_payload'):
			from .Payload import Payload
			self._payload = Payload(self._core, self._cmd_group)
		return self._payload

	@property
	def prbs(self):
		"""prbs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_prbs'):
			from .Prbs import Prbs
			self._prbs = Prbs(self._core, self._cmd_group)
		return self._prbs

	@property
	def rate(self):
		"""rate commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_rate'):
			from .Rate import Rate
			self._rate = Rate(self._core, self._cmd_group)
		return self._rate

	@property
	def segments(self):
		"""segments commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_segments'):
			from .Segments import Segments
			self._segments = Segments(self._core, self._cmd_group)
		return self._segments

	@property
	def setting(self):
		"""setting commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_setting'):
			from .Setting import Setting
			self._setting = Setting(self._core, self._cmd_group)
		return self._setting

	@property
	def source(self):
		"""source commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_source'):
			from .Source import Source
			self._source = Source(self._core, self._cmd_group)
		return self._source

	@property
	def testSignal(self):
		"""testSignal commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_testSignal'):
			from .TestSignal import TestSignal
			self._testSignal = TestSignal(self._core, self._cmd_group)
		return self._testSignal

	@property
	def time(self):
		"""time commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_time'):
			from .Time import Time
			self._time = Time(self._core, self._cmd_group)
		return self._time

	@property
	def tsPackets(self):
		"""tsPackets commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tsPackets'):
			from .TsPackets import TsPackets
			self._tsPackets = TsPackets(self._core, self._cmd_group)
		return self._tsPackets

	@property
	def useful(self):
		"""useful commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_useful'):
			from .Useful import Useful
			self._useful = Useful(self._core, self._cmd_group)
		return self._useful

	@property
	def special(self):
		"""special commands group. 3 Sub-classes, 3 commands."""
		if not hasattr(self, '_special'):
			from .Special import Special
			self._special = Special(self._core, self._cmd_group)
		return self._special

	def get_bandwidth(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:BANDwidth \n
		Snippet: value: int = driver.source.bb.isdbt.get_bandwidth() \n
		Displays the used bandwidth. \n
			:return: used_bw: integer Range: 0 to 9999
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:BANDwidth?')
		return Conversions.str_to_int(response)

	# noinspection PyTypeChecker
	def get_control(self) -> enums.AutoManualMode:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:CONTrol \n
		Snippet: value: enums.AutoManualMode = driver.source.bb.isdbt.get_control() \n
		Defines the configuration mode of the coder. \n
			:return: control: AUTO| MANual
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:CONTrol?')
		return Conversions.str_to_scalar_enum(response, enums.AutoManualMode)

	def set_control(self, control: enums.AutoManualMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:CONTrol \n
		Snippet: driver.source.bb.isdbt.set_control(control = enums.AutoManualMode.AUTO) \n
		Defines the configuration mode of the coder. \n
			:param control: AUTO| MANual
		"""
		param = Conversions.enum_scalar_to_str(control, enums.AutoManualMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:CONTrol {param}')

	# noinspection PyTypeChecker
	def get_guard(self) -> enums.CodingGuardInterval:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:GUARd \n
		Snippet: value: enums.CodingGuardInterval = driver.source.bb.isdbt.get_guard() \n
		Sets the guard interval length. \n
			:return: guard_int: G1_32| G1_16| G1_8| G1_4
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:GUARd?')
		return Conversions.str_to_scalar_enum(response, enums.CodingGuardInterval)

	def set_guard(self, guard_int: enums.CodingGuardInterval) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:GUARd \n
		Snippet: driver.source.bb.isdbt.set_guard(guard_int = enums.CodingGuardInterval.G1_16) \n
		Sets the guard interval length. \n
			:param guard_int: G1_32| G1_16| G1_8| G1_4
		"""
		param = Conversions.enum_scalar_to_str(guard_int, enums.CodingGuardInterval)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:GUARd {param}')

	# noinspection PyTypeChecker
	def get_network_mode(self) -> enums.NetworkMode:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:NETWorkmode \n
		Snippet: value: enums.NetworkMode = driver.source.bb.isdbt.get_network_mode() \n
		No command help available \n
			:return: network_mode: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:NETWorkmode?')
		return Conversions.str_to_scalar_enum(response, enums.NetworkMode)

	def set_network_mode(self, network_mode: enums.NetworkMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:NETWorkmode \n
		Snippet: driver.source.bb.isdbt.set_network_mode(network_mode = enums.NetworkMode.MFN) \n
		No command help available \n
			:param network_mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(network_mode, enums.NetworkMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:NETWorkmode {param}')

	# noinspection PyTypeChecker
	def get_packet_length(self) -> enums.InputSignalPacketLength:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:PACKetlength \n
		Snippet: value: enums.InputSignalPacketLength = driver.source.bb.isdbt.get_packet_length() \n
		Queries the packet length of the external transport stream in bytes. \n
			:return: packet_length: P188| P204| INValid P188|P204 188/204 byte packets specified for serial input and parallel input. INValid Packet length does not match the specified length.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:PACKetlength?')
		return Conversions.str_to_scalar_enum(response, enums.InputSignalPacketLength)

	def get_pid(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:PID \n
		Snippet: value: int = driver.source.bb.isdbt.get_pid() \n
		Sets the . \n
			:return: pid: integer Range: #H000 to #H1FFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:PID?')
		return Conversions.str_to_int(response)

	def set_pid(self, pid: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:PID \n
		Snippet: driver.source.bb.isdbt.set_pid(pid = 1) \n
		Sets the . \n
			:param pid: integer Range: #H000 to #H1FFF
		"""
		param = Conversions.decimal_value_to_str(pid)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:PID {param}')

	# noinspection PyTypeChecker
	def get_pid_test_pack(self) -> enums.PidTestPacket:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:PIDTestpack \n
		Snippet: value: enums.PidTestPacket = driver.source.bb.isdbt.get_pid_test_pack() \n
		If a header is present in the test packet ('Test TS Packet > Head/184 Payload') , you can specify a fixed or variable
		packet identifier (PID) . \n
			:return: test_pack: VARiable| NULL
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:PIDTestpack?')
		return Conversions.str_to_scalar_enum(response, enums.PidTestPacket)

	def set_pid_test_pack(self, test_pack: enums.PidTestPacket) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:PIDTestpack \n
		Snippet: driver.source.bb.isdbt.set_pid_test_pack(test_pack = enums.PidTestPacket.NULL) \n
		If a header is present in the test packet ('Test TS Packet > Head/184 Payload') , you can specify a fixed or variable
		packet identifier (PID) . \n
			:param test_pack: VARiable| NULL
		"""
		param = Conversions.enum_scalar_to_str(test_pack, enums.PidTestPacket)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:PIDTestpack {param}')

	# noinspection PyTypeChecker
	def get_portion(self) -> enums.CodingPortions:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:PORTion \n
		Snippet: value: enums.CodingPortions = driver.source.bb.isdbt.get_portion() \n
		Sets the modulation types of the hierachical layers A, B and C. The first digit specifies the modulation type for layer A,
		the second digit for layer B and the third digit for layer C. \n
			:return: portion: PDD| PDC| PCC| DDD| DDC| DCC| CCC P Partial reception D Differential modulation C Coherent modulation
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:PORTion?')
		return Conversions.str_to_scalar_enum(response, enums.CodingPortions)

	def set_portion(self, portion: enums.CodingPortions) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:PORTion \n
		Snippet: driver.source.bb.isdbt.set_portion(portion = enums.CodingPortions.CCC) \n
		Sets the modulation types of the hierachical layers A, B and C. The first digit specifies the modulation type for layer A,
		the second digit for layer B and the third digit for layer C. \n
			:param portion: PDD| PDC| PCC| DDD| DDC| DCC| CCC P Partial reception D Differential modulation C Coherent modulation
		"""
		param = Conversions.enum_scalar_to_str(portion, enums.CodingPortions)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:PORTion {param}')

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:PRESet \n
		Snippet: driver.source.bb.isdbt.preset() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:ISDBt:STATe. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:PRESet \n
		Snippet: driver.source.bb.isdbt.preset_with_opc() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:ISDBt:STATe. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmcv.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:ISDBt:PRESet', opc_timeout_ms)

	def get_remux(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:REMux \n
		Snippet: value: bool = driver.source.bb.isdbt.get_remux() \n
		Enables/disables the built-in remultiplexer. \n
			:return: remux: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:REMux?')
		return Conversions.str_to_bool(response)

	def set_remux(self, remux: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:REMux \n
		Snippet: driver.source.bb.isdbt.set_remux(remux = False) \n
		Enables/disables the built-in remultiplexer. \n
			:param remux: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(remux)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:REMux {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:STATe \n
		Snippet: value: bool = driver.source.bb.isdbt.get_state() \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:STATe \n
		Snippet: driver.source.bb.isdbt.set_state(state = False) \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:STATe {param}')

	def get_stuffing(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:STUFfing \n
		Snippet: value: bool = driver.source.bb.isdbt.get_stuffing() \n
		Queries, if stuffing is enabled or disabled.
			INTRO_CMD_HELP: You can enable/disable stuffing via [:SOURce<hw>]:BB:ISDBt:CONTrol: \n
			- SOURce1:BB:ISDBt:CONTrol AUTO Stuffing is disabed.
			- SOURce1:BB:ISDBt:CONTrol MAN Stuffing is enabed. \n
			:return: stuffing: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:STUFfing?')
		return Conversions.str_to_bool(response)

	def get_sub_channel(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:SUBChannel \n
		Snippet: value: int = driver.source.bb.isdbt.get_sub_channel() \n
		Sets the subchannel of the ISDB-TSB signal. \n
			:return: sub_channel: integer Range: 0 to 41
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:SUBChannel?')
		return Conversions.str_to_int(response)

	def set_sub_channel(self, sub_channel: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:SUBChannel \n
		Snippet: driver.source.bb.isdbt.set_sub_channel(sub_channel = 1) \n
		Sets the subchannel of the ISDB-TSB signal. \n
			:param sub_channel: integer Range: 0 to 41
		"""
		param = Conversions.decimal_value_to_str(sub_channel)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:SUBChannel {param}')

	# noinspection PyTypeChecker
	def get_system(self) -> enums.IsdbtCodingSystem:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:SYSTem \n
		Snippet: value: enums.IsdbtCodingSystem = driver.source.bb.isdbt.get_system() \n
		Sets the ISDB-T system. \n
			:return: system: TSB3| TSB1| T
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:SYSTem?')
		return Conversions.str_to_scalar_enum(response, enums.IsdbtCodingSystem)

	def set_system(self, system: enums.IsdbtCodingSystem) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:SYSTem \n
		Snippet: driver.source.bb.isdbt.set_system(system = enums.IsdbtCodingSystem.T) \n
		Sets the ISDB-T system. \n
			:param system: TSB3| TSB1| T
		"""
		param = Conversions.enum_scalar_to_str(system, enums.IsdbtCodingSystem)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:SYSTem {param}')

	def clone(self) -> 'Isdbt':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Isdbt(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
