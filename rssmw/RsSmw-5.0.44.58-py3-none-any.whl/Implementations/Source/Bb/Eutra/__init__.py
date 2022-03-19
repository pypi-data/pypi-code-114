from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Eutra:
	"""Eutra commands group definition. 1288 total commands, 20 Subgroups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("eutra", core, parent)

	@property
	def bbfs(self):
		"""bbfs commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_bbfs'):
			from .Bbfs import Bbfs
			self._bbfs = Bbfs(self._core, self._cmd_group)
		return self._bbfs

	@property
	def clipping(self):
		"""clipping commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_clipping'):
			from .Clipping import Clipping
			self._clipping = Clipping(self._core, self._cmd_group)
		return self._clipping

	@property
	def clock(self):
		"""clock commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_clock'):
			from .Clock import Clock
			self._clock = Clock(self._core, self._cmd_group)
		return self._clock

	@property
	def downlink(self):
		"""downlink commands group. 25 Sub-classes, 14 commands."""
		if not hasattr(self, '_downlink'):
			from .Downlink import Downlink
			self._downlink = Downlink(self._core, self._cmd_group)
		return self._downlink

	@property
	def filterPy(self):
		"""filterPy commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_filterPy'):
			from .FilterPy import FilterPy
			self._filterPy = FilterPy(self._core, self._cmd_group)
		return self._filterPy

	@property
	def logGen(self):
		"""logGen commands group. 2 Sub-classes, 4 commands."""
		if not hasattr(self, '_logGen'):
			from .LogGen import LogGen
			self._logGen = LogGen(self._core, self._cmd_group)
		return self._logGen

	@property
	def noise(self):
		"""noise commands group. 0 Sub-classes, 6 commands."""
		if not hasattr(self, '_noise'):
			from .Noise import Noise
			self._noise = Noise(self._core, self._cmd_group)
		return self._noise

	@property
	def notch(self):
		"""notch commands group. 4 Sub-classes, 3 commands."""
		if not hasattr(self, '_notch'):
			from .Notch import Notch
			self._notch = Notch(self._core, self._cmd_group)
		return self._notch

	@property
	def powc(self):
		"""powc commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_powc'):
			from .Powc import Powc
			self._powc = Powc(self._core, self._cmd_group)
		return self._powc

	@property
	def setting(self):
		"""setting commands group. 1 Sub-classes, 4 commands."""
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
	def tcw(self):
		"""tcw commands group. 12 Sub-classes, 1 commands."""
		if not hasattr(self, '_tcw'):
			from .Tcw import Tcw
			self._tcw = Tcw(self._core, self._cmd_group)
		return self._tcw

	@property
	def tdd(self):
		"""tdd commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_tdd'):
			from .Tdd import Tdd
			self._tdd = Tdd(self._core, self._cmd_group)
		return self._tdd

	@property
	def tdw(self):
		"""tdw commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_tdw'):
			from .Tdw import Tdw
			self._tdw = Tdw(self._core, self._cmd_group)
		return self._tdw

	@property
	def timc(self):
		"""timc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_timc'):
			from .Timc import Timc
			self._timc = Timc(self._core, self._cmd_group)
		return self._timc

	@property
	def trigger(self):
		"""trigger commands group. 6 Sub-classes, 5 commands."""
		if not hasattr(self, '_trigger'):
			from .Trigger import Trigger
			self._trigger = Trigger(self._core, self._cmd_group)
		return self._trigger

	@property
	def udt(self):
		"""udt commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_udt'):
			from .Udt import Udt
			self._udt = Udt(self._core, self._cmd_group)
		return self._udt

	@property
	def uplink(self):
		"""uplink commands group. 15 Sub-classes, 13 commands."""
		if not hasattr(self, '_uplink'):
			from .Uplink import Uplink
			self._uplink = Uplink(self._core, self._cmd_group)
		return self._uplink

	@property
	def uplane(self):
		"""uplane commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_uplane'):
			from .Uplane import Uplane
			self._uplane = Uplane(self._core, self._cmd_group)
		return self._uplane

	@property
	def waveform(self):
		"""waveform commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_waveform'):
			from .Waveform import Waveform
			self._waveform = Waveform(self._core, self._cmd_group)
		return self._waveform

	# noinspection PyTypeChecker
	def get_duplexing(self) -> enums.EutraDuplexMode:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DUPLexing \n
		Snippet: value: enums.EutraDuplexMode = driver.source.bb.eutra.get_duplexing() \n
		Sets the duplexing mode. \n
			:return: duplexing: TDD| FDD
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DUPLexing?')
		return Conversions.str_to_scalar_enum(response, enums.EutraDuplexMode)

	def set_duplexing(self, duplexing: enums.EutraDuplexMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DUPLexing \n
		Snippet: driver.source.bb.eutra.set_duplexing(duplexing = enums.EutraDuplexMode.FDD) \n
		Sets the duplexing mode. \n
			:param duplexing: TDD| FDD
		"""
		param = Conversions.enum_scalar_to_str(duplexing, enums.EutraDuplexMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DUPLexing {param}')

	# noinspection PyTypeChecker
	def get_link(self) -> enums.UpDownDirection:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:LINK \n
		Snippet: value: enums.UpDownDirection = driver.source.bb.eutra.get_link() \n
		Sets the transmission direction. \n
			:return: link: UP| DOWN
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:LINK?')
		return Conversions.str_to_scalar_enum(response, enums.UpDownDirection)

	def set_link(self, link: enums.UpDownDirection) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:LINK \n
		Snippet: driver.source.bb.eutra.set_link(link = enums.UpDownDirection.DOWN) \n
		Sets the transmission direction. \n
			:param link: UP| DOWN
		"""
		param = Conversions.enum_scalar_to_str(link, enums.UpDownDirection)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:LINK {param}')

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:PRESet \n
		Snippet: driver.source.bb.eutra.preset() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:EUTRa:STATe. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:PRESet \n
		Snippet: driver.source.bb.eutra.preset_with_opc() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:EUTRa:STATe. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:EUTRa:PRESet', opc_timeout_ms)

	def get_slength(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:SLENgth \n
		Snippet: value: int = driver.source.bb.eutra.get_slength() \n
		Sets the sequence length of the signal in number of frames. The signal is calculated in advance and output in the
		arbitrary waveform generator. The maximum number of frames is calculated as follows: Max. No. of Frames = Arbitrary
		waveform memory size/(sampling rate x 10 ms) . \n
			:return: slength: integer Range: 1 to dynamic
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:SLENgth?')
		return Conversions.str_to_int(response)

	def set_slength(self, slength: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:SLENgth \n
		Snippet: driver.source.bb.eutra.set_slength(slength = 1) \n
		Sets the sequence length of the signal in number of frames. The signal is calculated in advance and output in the
		arbitrary waveform generator. The maximum number of frames is calculated as follows: Max. No. of Frames = Arbitrary
		waveform memory size/(sampling rate x 10 ms) . \n
			:param slength: integer Range: 1 to dynamic
		"""
		param = Conversions.decimal_value_to_str(slength)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:SLENgth {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:STATe \n
		Snippet: value: bool = driver.source.bb.eutra.get_state() \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:STATe \n
		Snippet: driver.source.bb.eutra.set_state(state = False) \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:STATe {param}')

	# noinspection PyTypeChecker
	def get_std_mode(self) -> enums.EutraStdMode:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:STDMode \n
		Snippet: value: enums.EutraStdMode = driver.source.bb.eutra.get_std_mode() \n
		Sets the supported 3GPP standard. \n
			:return: standard_mode: LTE| IOT| LIOT LTE Standalone LTE mode. IoT-specific commands containing the keywords EMTC or NIOT are discarded. IOT Standalone IoT mode. The commands related to LTE-specific features like carrier aggregation or MBSFN are discarded. LIOT Mixed LTE and IoT configuration, for example for interoperability tests.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:STDMode?')
		return Conversions.str_to_scalar_enum(response, enums.EutraStdMode)

	def set_std_mode(self, standard_mode: enums.EutraStdMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:STDMode \n
		Snippet: driver.source.bb.eutra.set_std_mode(standard_mode = enums.EutraStdMode.IOT) \n
		Sets the supported 3GPP standard. \n
			:param standard_mode: LTE| IOT| LIOT LTE Standalone LTE mode. IoT-specific commands containing the keywords EMTC or NIOT are discarded. IOT Standalone IoT mode. The commands related to LTE-specific features like carrier aggregation or MBSFN are discarded. LIOT Mixed LTE and IoT configuration, for example for interoperability tests.
		"""
		param = Conversions.enum_scalar_to_str(standard_mode, enums.EutraStdMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:STDMode {param}')

	def get_version(self) -> str:
		"""SCPI: [SOURce]:BB:EUTRa:VERSion \n
		Snippet: value: str = driver.source.bb.eutra.get_version() \n
		Queries the version of the 3GPP standard underlying the definitions. \n
			:return: version: string
		"""
		response = self._core.io.query_str('SOURce:BB:EUTRa:VERSion?')
		return trim_str_response(response)

	def clone(self) -> 'Eutra':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Eutra(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
