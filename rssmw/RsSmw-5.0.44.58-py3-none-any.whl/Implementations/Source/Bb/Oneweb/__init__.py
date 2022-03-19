from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Oneweb:
	"""Oneweb commands group definition. 654 total commands, 16 Subgroups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("oneweb", core, parent)

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
		"""downlink commands group. 19 Sub-classes, 15 commands."""
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
	def refSignal(self):
		"""refSignal commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_refSignal'):
			from .RefSignal import RefSignal
			self._refSignal = RefSignal(self._core, self._cmd_group)
		return self._refSignal

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
	def tdd(self):
		"""tdd commands group. 0 Sub-classes, 2 commands."""
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
		"""uplink commands group. 11 Sub-classes, 13 commands."""
		if not hasattr(self, '_uplink'):
			from .Uplink import Uplink
			self._uplink = Uplink(self._core, self._cmd_group)
		return self._uplink

	@property
	def waveform(self):
		"""waveform commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_waveform'):
			from .Waveform import Waveform
			self._waveform = Waveform(self._core, self._cmd_group)
		return self._waveform

	# noinspection PyTypeChecker
	def get_cmod(self) -> enums.OneWebConfMode:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:CMOD \n
		Snippet: value: enums.OneWebConfMode = driver.source.bb.oneweb.get_cmod() \n
		Sets the configuration mode. \n
			:return: config_mode: PREDefined| USER
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:CMOD?')
		return Conversions.str_to_scalar_enum(response, enums.OneWebConfMode)

	def set_cmod(self, config_mode: enums.OneWebConfMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:CMOD \n
		Snippet: driver.source.bb.oneweb.set_cmod(config_mode = enums.OneWebConfMode.PREDefined) \n
		Sets the configuration mode. \n
			:param config_mode: PREDefined| USER
		"""
		param = Conversions.enum_scalar_to_str(config_mode, enums.OneWebConfMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:CMOD {param}')

	# noinspection PyTypeChecker
	def get_duplexing(self) -> enums.OneWebDuplexModeRange:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DUPLexing \n
		Snippet: value: enums.OneWebDuplexModeRange = driver.source.bb.oneweb.get_duplexing() \n
		Queries the duplexing mode. \n
			:return: duplexing: FDD
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DUPLexing?')
		return Conversions.str_to_scalar_enum(response, enums.OneWebDuplexModeRange)

	# noinspection PyTypeChecker
	def get_link(self) -> enums.UpDownDirection:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:LINK \n
		Snippet: value: enums.UpDownDirection = driver.source.bb.oneweb.get_link() \n
		Sets the transmission direction. \n
			:return: link: UP| DOWN
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:LINK?')
		return Conversions.str_to_scalar_enum(response, enums.UpDownDirection)

	def set_link(self, link: enums.UpDownDirection) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:LINK \n
		Snippet: driver.source.bb.oneweb.set_link(link = enums.UpDownDirection.DOWN) \n
		Sets the transmission direction. \n
			:param link: UP| DOWN
		"""
		param = Conversions.enum_scalar_to_str(link, enums.UpDownDirection)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:LINK {param}')

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:PRESet \n
		Snippet: driver.source.bb.oneweb.preset() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:ONEWeb:STATe. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:PRESet \n
		Snippet: driver.source.bb.oneweb.preset_with_opc() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:ONEWeb:STATe. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:ONEWeb:PRESet', opc_timeout_ms)

	def get_slength(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:SLENgth \n
		Snippet: value: int = driver.source.bb.oneweb.get_slength() \n
		Sets the sequence length of the signal in number of frames. The signal is calculated in advance and output in the
		arbitrary waveform generator. The maximum number of frames is calculated as follows: Max. No. of Frames = Arbitrary
		waveform memory size/(sampling rate x 10 ms) . \n
			:return: slength: integer Range: 1 to dynamic
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:SLENgth?')
		return Conversions.str_to_int(response)

	def set_slength(self, slength: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:SLENgth \n
		Snippet: driver.source.bb.oneweb.set_slength(slength = 1) \n
		Sets the sequence length of the signal in number of frames. The signal is calculated in advance and output in the
		arbitrary waveform generator. The maximum number of frames is calculated as follows: Max. No. of Frames = Arbitrary
		waveform memory size/(sampling rate x 10 ms) . \n
			:param slength: integer Range: 1 to dynamic
		"""
		param = Conversions.decimal_value_to_str(slength)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:SLENgth {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:STATe \n
		Snippet: value: bool = driver.source.bb.oneweb.get_state() \n
		Activates the standard. \n
			:return: one_web_state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, one_web_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:STATe \n
		Snippet: driver.source.bb.oneweb.set_state(one_web_state = False) \n
		Activates the standard. \n
			:param one_web_state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(one_web_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:STATe {param}')

	def get_version(self) -> str:
		"""SCPI: [SOURce]:BB:ONEWeb:VERSion \n
		Snippet: value: str = driver.source.bb.oneweb.get_version() \n
		No command help available \n
			:return: version: No help available
		"""
		response = self._core.io.query_str('SOURce:BB:ONEWeb:VERSion?')
		return trim_str_response(response)

	def clone(self) -> 'Oneweb':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Oneweb(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
