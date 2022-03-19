from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Huwb:
	"""Huwb commands group definition. 127 total commands, 12 Subgroups, 12 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("huwb", core, parent)

	@property
	def clipping(self):
		"""clipping commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_clipping'):
			from .Clipping import Clipping
			self._clipping = Clipping(self._core, self._cmd_group)
		return self._clipping

	@property
	def clock(self):
		"""clock commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_clock'):
			from .Clock import Clock
			self._clock = Clock(self._core, self._cmd_group)
		return self._clock

	@property
	def fconfig(self):
		"""fconfig commands group. 3 Sub-classes, 14 commands."""
		if not hasattr(self, '_fconfig'):
			from .Fconfig import Fconfig
			self._fconfig = Fconfig(self._core, self._cmd_group)
		return self._fconfig

	@property
	def filterPy(self):
		"""filterPy commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_filterPy'):
			from .FilterPy import FilterPy
			self._filterPy = FilterPy(self._core, self._cmd_group)
		return self._filterPy

	@property
	def impairments(self):
		"""impairments commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_impairments'):
			from .Impairments import Impairments
			self._impairments = Impairments(self._core, self._cmd_group)
		return self._impairments

	@property
	def macHeader(self):
		"""macHeader commands group. 0 Sub-classes, 31 commands."""
		if not hasattr(self, '_macHeader'):
			from .MacHeader import MacHeader
			self._macHeader = MacHeader(self._core, self._cmd_group)
		return self._macHeader

	@property
	def phr(self):
		"""phr commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_phr'):
			from .Phr import Phr
			self._phr = Phr(self._core, self._cmd_group)
		return self._phr

	@property
	def setting(self):
		"""setting commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_setting'):
			from .Setting import Setting
			self._setting = Setting(self._core, self._cmd_group)
		return self._setting

	@property
	def symbolRate(self):
		"""symbolRate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_symbolRate'):
			from .SymbolRate import SymbolRate
			self._symbolRate = SymbolRate(self._core, self._cmd_group)
		return self._symbolRate

	@property
	def sts(self):
		"""sts commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_sts'):
			from .Sts import Sts
			self._sts = Sts(self._core, self._cmd_group)
		return self._sts

	@property
	def trigger(self):
		"""trigger commands group. 6 Sub-classes, 5 commands."""
		if not hasattr(self, '_trigger'):
			from .Trigger import Trigger
			self._trigger = Trigger(self._core, self._cmd_group)
		return self._trigger

	@property
	def waveform(self):
		"""waveform commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_waveform'):
			from .Waveform import Waveform
			self._waveform = Waveform(self._core, self._cmd_group)
		return self._waveform

	# noinspection PyTypeChecker
	def get_asl(self) -> enums.HrpUwbActSegmentLength:
		"""SCPI: [SOURce<HW>]:BB:HUWB:ASL \n
		Snippet: value: enums.HrpUwbActSegmentLength = driver.source.bb.huwb.get_asl() \n
		Sets the active segment length. \n
			:return: act_seg_length: ASL_16| ASL_32| ASL_64| ASL_128| ASL_256| ASL_512| ASL_1024| ASL_2048
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:ASL?')
		return Conversions.str_to_scalar_enum(response, enums.HrpUwbActSegmentLength)

	def set_asl(self, act_seg_length: enums.HrpUwbActSegmentLength) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:ASL \n
		Snippet: driver.source.bb.huwb.set_asl(act_seg_length = enums.HrpUwbActSegmentLength.ASL_1024) \n
		Sets the active segment length. \n
			:param act_seg_length: ASL_16| ASL_32| ASL_64| ASL_128| ASL_256| ASL_512| ASL_1024| ASL_2048
		"""
		param = Conversions.enum_scalar_to_str(act_seg_length, enums.HrpUwbActSegmentLength)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:ASL {param}')

	# noinspection PyTypeChecker
	def get_asn(self) -> enums.HrpUwbActSegmentNum:
		"""SCPI: [SOURce<HW>]:BB:HUWB:ASN \n
		Snippet: value: enums.HrpUwbActSegmentNum = driver.source.bb.huwb.get_asn() \n
		Sets the number of active segments. \n
			:return: acg_seg_number: ASN_1| ASN_2| ASN_3| ASN_4
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:ASN?')
		return Conversions.str_to_scalar_enum(response, enums.HrpUwbActSegmentNum)

	def set_asn(self, acg_seg_number: enums.HrpUwbActSegmentNum) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:ASN \n
		Snippet: driver.source.bb.huwb.set_asn(acg_seg_number = enums.HrpUwbActSegmentNum.ASN_1) \n
		Sets the number of active segments. \n
			:param acg_seg_number: ASN_1| ASN_2| ASN_3| ASN_4
		"""
		param = Conversions.enum_scalar_to_str(acg_seg_number, enums.HrpUwbActSegmentNum)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:ASN {param}')

	def get_bandwidth(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:HUWB:BWIDth \n
		Snippet: value: float = driver.source.bb.huwb.get_bandwidth() \n
		Queries the channel bandwidth. \n
			:return: hrp_uwb_band_width: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:BWIDth?')
		return Conversions.str_to_float(response)

	# noinspection PyTypeChecker
	def get_cccl(self) -> enums.HrpUwbConvConsLen:
		"""SCPI: [SOURce<HW>]:BB:HUWB:CCCL \n
		Snippet: value: enums.HrpUwbConvConsLen = driver.source.bb.huwb.get_cccl() \n
		Sets the constraint length of the convolutional code. \n
			:return: cccl: CL3| CL7
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:CCCL?')
		return Conversions.str_to_scalar_enum(response, enums.HrpUwbConvConsLen)

	def set_cccl(self, cccl: enums.HrpUwbConvConsLen) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:CCCL \n
		Snippet: driver.source.bb.huwb.set_cccl(cccl = enums.HrpUwbConvConsLen.CL3) \n
		Sets the constraint length of the convolutional code. \n
			:param cccl: CL3| CL7
		"""
		param = Conversions.enum_scalar_to_str(cccl, enums.HrpUwbConvConsLen)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:CCCL {param}')

	def get_cnumber(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:HUWB:CNUMber \n
		Snippet: value: int = driver.source.bb.huwb.get_cnumber() \n
		Sets the channel number. \n
			:return: channel_number: integer Range: 0 to 15
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:CNUMber?')
		return Conversions.str_to_int(response)

	def set_cnumber(self, channel_number: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:CNUMber \n
		Snippet: driver.source.bb.huwb.set_cnumber(channel_number = 1) \n
		Sets the channel number. \n
			:param channel_number: integer Range: 0 to 15
		"""
		param = Conversions.decimal_value_to_str(channel_number)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:CNUMber {param}')

	def get_f_2_ms(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:HUWB:F2MS \n
		Snippet: value: bool = driver.source.bb.huwb.get_f_2_ms() \n
		No command help available \n
			:return: fixed_2_ms_frame: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:F2MS?')
		return Conversions.str_to_bool(response)

	def set_f_2_ms(self, fixed_2_ms_frame: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:F2MS \n
		Snippet: driver.source.bb.huwb.set_f_2_ms(fixed_2_ms_frame = False) \n
		No command help available \n
			:param fixed_2_ms_frame: No help available
		"""
		param = Conversions.bool_to_str(fixed_2_ms_frame)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:F2MS {param}')

	def get_iinterval(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:HUWB:IINTerval \n
		Snippet: value: float = driver.source.bb.huwb.get_iinterval() \n
		Sets the time of the interval separating two frames. \n
			:return: iinterval: float Range: 0 to 1000000, Unit: µs
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:IINTerval?')
		return Conversions.str_to_float(response)

	def set_iinterval(self, iinterval: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:IINTerval \n
		Snippet: driver.source.bb.huwb.set_iinterval(iinterval = 1.0) \n
		Sets the time of the interval separating two frames. \n
			:param iinterval: float Range: 0 to 1000000, Unit: µs
		"""
		param = Conversions.decimal_value_to_str(iinterval)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:IINTerval {param}')

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:PRESet \n
		Snippet: driver.source.bb.huwb.preset() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:HUWB:STATe. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:PRESet \n
		Snippet: driver.source.bb.huwb.preset_with_opc() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:HUWB:STATe. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:HUWB:PRESet', opc_timeout_ms)

	# noinspection PyTypeChecker
	def get_sfd(self) -> enums.HrpUwbSfdIndex:
		"""SCPI: [SOURce<HW>]:BB:HUWB:SFD \n
		Snippet: value: enums.HrpUwbSfdIndex = driver.source.bb.huwb.get_sfd() \n
		Sets the start-of-frame delimiter (SFD) . \n
			:return: sfd_index: SFD_0| SFD_1| SFD_2| SFD_3| SFD_4
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:SFD?')
		return Conversions.str_to_scalar_enum(response, enums.HrpUwbSfdIndex)

	def set_sfd(self, sfd_index: enums.HrpUwbSfdIndex) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:SFD \n
		Snippet: driver.source.bb.huwb.set_sfd(sfd_index = enums.HrpUwbSfdIndex.SFD_0) \n
		Sets the start-of-frame delimiter (SFD) . \n
			:param sfd_index: SFD_0| SFD_1| SFD_2| SFD_3| SFD_4
		"""
		param = Conversions.enum_scalar_to_str(sfd_index, enums.HrpUwbSfdIndex)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:SFD {param}')

	def get_slength(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:HUWB:SLENgth \n
		Snippet: value: int = driver.source.bb.huwb.get_slength() \n
		Sets the sequence length of the signal in number of frames. The signal is calculated in advance and output in the
		arbitrary waveform generator. The maximum number of frames is calculated as follows: Max. No. of Frames = Arbitrary
		waveform memory size/(sampling rate x 10 ms) . \n
			:return: slength: integer Range: 1 to 1024
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:SLENgth?')
		return Conversions.str_to_int(response)

	def set_slength(self, slength: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:SLENgth \n
		Snippet: driver.source.bb.huwb.set_slength(slength = 1) \n
		Sets the sequence length of the signal in number of frames. The signal is calculated in advance and output in the
		arbitrary waveform generator. The maximum number of frames is calculated as follows: Max. No. of Frames = Arbitrary
		waveform memory size/(sampling rate x 10 ms) . \n
			:param slength: integer Range: 1 to 1024
		"""
		param = Conversions.decimal_value_to_str(slength)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:SLENgth {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:HUWB:STATe \n
		Snippet: value: bool = driver.source.bb.huwb.get_state() \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:return: hrp_uwb_state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, hrp_uwb_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:STATe \n
		Snippet: driver.source.bb.huwb.set_state(hrp_uwb_state = False) \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:param hrp_uwb_state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(hrp_uwb_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:STATe {param}')

	# noinspection PyTypeChecker
	def get_std(self) -> enums.HrpUwbMode:
		"""SCPI: [SOURce<HW>]:BB:HUWB:STD \n
		Snippet: value: enums.HrpUwbMode = driver.source.bb.huwb.get_std() \n
		Sets the HRP UWB mode. \n
			:return: mode: NONHRP| HPRF| BPRF NONHRP Enables HRP non-ERDEV mode. BPRF Enables HRP-ERDEV base pulse repetition frequency (BPRF) mode. HPRF Enables HRP-ERDEV higher pulse repetition frequency (HPRF) mode.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:STD?')
		return Conversions.str_to_scalar_enum(response, enums.HrpUwbMode)

	def set_std(self, mode: enums.HrpUwbMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:STD \n
		Snippet: driver.source.bb.huwb.set_std(mode = enums.HrpUwbMode.BPRF) \n
		Sets the HRP UWB mode. \n
			:param mode: NONHRP| HPRF| BPRF NONHRP Enables HRP non-ERDEV mode. BPRF Enables HRP-ERDEV base pulse repetition frequency (BPRF) mode. HPRF Enables HRP-ERDEV higher pulse repetition frequency (HPRF) mode.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.HrpUwbMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:STD {param}')

	def clone(self) -> 'Huwb':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Huwb(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
