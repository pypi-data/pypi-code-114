from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tetra:
	"""Tetra commands group definition. 105 total commands, 11 Subgroups, 9 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tetra", core, parent)

	@property
	def bbncht(self):
		"""bbncht commands group. 0 Sub-classes, 26 commands."""
		if not hasattr(self, '_bbncht'):
			from .Bbncht import Bbncht
			self._bbncht = Bbncht(self._core, self._cmd_group)
		return self._bbncht

	@property
	def clipping(self):
		"""clipping commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_clipping'):
			from .Clipping import Clipping
			self._clipping = Clipping(self._core, self._cmd_group)
		return self._clipping

	@property
	def clock(self):
		"""clock commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_clock'):
			from .Clock import Clock
			self._clock = Clock(self._core, self._cmd_group)
		return self._clock

	@property
	def filterPy(self):
		"""filterPy commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_filterPy'):
			from .FilterPy import FilterPy
			self._filterPy = FilterPy(self._core, self._cmd_group)
		return self._filterPy

	@property
	def pramping(self):
		"""pramping commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_pramping'):
			from .Pramping import Pramping
			self._pramping = Pramping(self._core, self._cmd_group)
		return self._pramping

	@property
	def sattenuation(self):
		"""sattenuation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sattenuation'):
			from .Sattenuation import Sattenuation
			self._sattenuation = Sattenuation(self._core, self._cmd_group)
		return self._sattenuation

	@property
	def sconfiguration(self):
		"""sconfiguration commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_sconfiguration'):
			from .Sconfiguration import Sconfiguration
			self._sconfiguration = Sconfiguration(self._core, self._cmd_group)
		return self._sconfiguration

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
	def trigger(self):
		"""trigger commands group. 5 Sub-classes, 5 commands."""
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
	def get_ctype(self) -> enums.TetraChnnlType:
		"""SCPI: [SOURce<HW>]:BB:TETRa:CTYPe \n
		Snippet: value: enums.TetraChnnlType = driver.source.bb.tetra.get_ctype() \n
		(for 'Test Model' set to T1 or T4) Determines the channel type. \n
			:return: ctype: CH0| CH1| CH2| CH3| CH4| CH7| CH8| CH9| CH10| CH11| CH21| CH22| CH23| CH24| CH25| CH26| CH27
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TETRa:CTYPe?')
		return Conversions.str_to_scalar_enum(response, enums.TetraChnnlType)

	def set_ctype(self, ctype: enums.TetraChnnlType) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:CTYPe \n
		Snippet: driver.source.bb.tetra.set_ctype(ctype = enums.TetraChnnlType.CH0) \n
		(for 'Test Model' set to T1 or T4) Determines the channel type. \n
			:param ctype: CH0| CH1| CH2| CH3| CH4| CH7| CH8| CH9| CH10| CH11| CH21| CH22| CH23| CH24| CH25| CH26| CH27
		"""
		param = Conversions.enum_scalar_to_str(ctype, enums.TetraChnnlType)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:CTYPe {param}')

	# noinspection PyTypeChecker
	def get_db_type(self) -> enums.TetraDwnBrstType:
		"""SCPI: [SOURce<HW>]:BB:TETRa:DBTYpe \n
		Snippet: value: enums.TetraDwnBrstType = driver.source.bb.tetra.get_db_type() \n
		(in Downlink 'Link Direction' and for 'Test Model' set to T2 or User Defined) Determines the downlink burst type. \n
			:return: db_type: CONTinuous| DCONtinuous
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TETRa:DBTYpe?')
		return Conversions.str_to_scalar_enum(response, enums.TetraDwnBrstType)

	def set_db_type(self, db_type: enums.TetraDwnBrstType) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:DBTYpe \n
		Snippet: driver.source.bb.tetra.set_db_type(db_type = enums.TetraDwnBrstType.CONTinuous) \n
		(in Downlink 'Link Direction' and for 'Test Model' set to T2 or User Defined) Determines the downlink burst type. \n
			:param db_type: CONTinuous| DCONtinuous
		"""
		param = Conversions.enum_scalar_to_str(db_type, enums.TetraDwnBrstType)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:DBTYpe {param}')

	# noinspection PyTypeChecker
	def get_ldirection(self) -> enums.UpDownDirection:
		"""SCPI: [SOURce<HW>]:BB:TETRa:LDIRection \n
		Snippet: value: enums.UpDownDirection = driver.source.bb.tetra.get_ldirection() \n
		Selects the transmission direction. This parameter determines the available 'Channel Types'. \n
			:return: ldirection: DOWN| UP DOWN The transmission direction selected is from the base station (BS) to the terminal (MS) . The signal corresponds to that of a BS. UP The transmission direction selected is from MS to the BS. The signal corresponds to that of a terminal.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TETRa:LDIRection?')
		return Conversions.str_to_scalar_enum(response, enums.UpDownDirection)

	def set_ldirection(self, ldirection: enums.UpDownDirection) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:LDIRection \n
		Snippet: driver.source.bb.tetra.set_ldirection(ldirection = enums.UpDownDirection.DOWN) \n
		Selects the transmission direction. This parameter determines the available 'Channel Types'. \n
			:param ldirection: DOWN| UP DOWN The transmission direction selected is from the base station (BS) to the terminal (MS) . The signal corresponds to that of a BS. UP The transmission direction selected is from MS to the BS. The signal corresponds to that of a terminal.
		"""
		param = Conversions.enum_scalar_to_str(ldirection, enums.UpDownDirection)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:LDIRection {param}')

	# noinspection PyTypeChecker
	def get_mtype(self) -> enums.TetraModulType:
		"""SCPI: [SOURce<HW>]:BB:TETRa:MTYPe \n
		Snippet: value: enums.TetraModulType = driver.source.bb.tetra.get_mtype() \n
		(for 'Test Model' set to User Defined) Determines the modulation type, 'Phase' or 'QAM.' \n
			:return: mtype: PHASe| QAM PHASe The T2 test signal is a pi/4-DQPSK modulated continuous radio signal. QAM The T2 test signal is 4-QAM, 16-QAM or 64-QAM modulated and spans a bandwidth of 25kHz, 50kHz, 100kHz or 150kHz.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TETRa:MTYPe?')
		return Conversions.str_to_scalar_enum(response, enums.TetraModulType)

	def set_mtype(self, mtype: enums.TetraModulType) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:MTYPe \n
		Snippet: driver.source.bb.tetra.set_mtype(mtype = enums.TetraModulType.PHASe) \n
		(for 'Test Model' set to User Defined) Determines the modulation type, 'Phase' or 'QAM.' \n
			:param mtype: PHASe| QAM PHASe The T2 test signal is a pi/4-DQPSK modulated continuous radio signal. QAM The T2 test signal is 4-QAM, 16-QAM or 64-QAM modulated and spans a bandwidth of 25kHz, 50kHz, 100kHz or 150kHz.
		"""
		param = Conversions.enum_scalar_to_str(mtype, enums.TetraModulType)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:MTYPe {param}')

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:PRESet \n
		Snippet: driver.source.bb.tetra.preset() \n
		Sets the parameters of the digital standard to their (*RST values specified for the commands) . Not affected is the state
		set with the command [:SOURce<hw>]:BB:TETRa:STATe. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:PRESet \n
		Snippet: driver.source.bb.tetra.preset_with_opc() \n
		Sets the parameters of the digital standard to their (*RST values specified for the commands) . Not affected is the state
		set with the command [:SOURce<hw>]:BB:TETRa:STATe. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:TETRa:PRESet', opc_timeout_ms)

	def get_slength(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:TETRa:SLENgth \n
		Snippet: value: int = driver.source.bb.tetra.get_slength() \n
		Selects the sequence length of the arbitrary waveform file in the number of multiframes. One multiframe is the minimum
		sequence length for a T1 signal. \n
			:return: slength: integer Range: 1 to depends on carrier bandwidth
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TETRa:SLENgth?')
		return Conversions.str_to_int(response)

	def set_slength(self, slength: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:SLENgth \n
		Snippet: driver.source.bb.tetra.set_slength(slength = 1) \n
		Selects the sequence length of the arbitrary waveform file in the number of multiframes. One multiframe is the minimum
		sequence length for a T1 signal. \n
			:param slength: integer Range: 1 to depends on carrier bandwidth
		"""
		param = Conversions.decimal_value_to_str(slength)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:SLENgth {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:TETRa:STATe \n
		Snippet: value: bool = driver.source.bb.tetra.get_state() \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TETRa:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:STATe \n
		Snippet: driver.source.bb.tetra.set_state(state = False) \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:STATe {param}')

	# noinspection PyTypeChecker
	def get_tmode(self) -> enums.TetraTestMode:
		"""SCPI: [SOURce<HW>]:BB:TETRa:TMODe \n
		Snippet: value: enums.TetraTestMode = driver.source.bb.tetra.get_tmode() \n
		Selects the test mode. Several settings depend on the selected test mode. \n
			:return: tmode: T1| T4| USER| T2| T3
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TETRa:TMODe?')
		return Conversions.str_to_scalar_enum(response, enums.TetraTestMode)

	def set_tmode(self, tmode: enums.TetraTestMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:TMODe \n
		Snippet: driver.source.bb.tetra.set_tmode(tmode = enums.TetraTestMode.T1) \n
		Selects the test mode. Several settings depend on the selected test mode. \n
			:param tmode: T1| T4| USER| T2| T3
		"""
		param = Conversions.enum_scalar_to_str(tmode, enums.TetraTestMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:TMODe {param}')

	def get_version(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:TETRa:VERSion \n
		Snippet: value: str = driver.source.bb.tetra.get_version() \n
		Queries the tetra standard version. \n
			:return: version: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TETRa:VERSion?')
		return trim_str_response(response)

	def clone(self) -> 'Tetra':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tetra(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
