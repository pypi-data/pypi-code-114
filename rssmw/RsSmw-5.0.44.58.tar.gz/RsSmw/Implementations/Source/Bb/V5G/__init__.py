from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class V5G:
	"""V5G commands group definition. 663 total commands, 15 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("v5G", core, parent)

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
		"""downlink commands group. 22 Sub-classes, 15 commands."""
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
		"""uplink commands group. 12 Sub-classes, 13 commands."""
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
	def get_duplexing(self) -> enums.EutraDuplexMode:
		"""SCPI: [SOURce<HW>]:BB:V5G:DUPLexing \n
		Snippet: value: enums.EutraDuplexMode = driver.source.bb.v5G.get_duplexing() \n
		No command help available \n
			:return: duplexing: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DUPLexing?')
		return Conversions.str_to_scalar_enum(response, enums.EutraDuplexMode)

	def set_duplexing(self, duplexing: enums.EutraDuplexMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DUPLexing \n
		Snippet: driver.source.bb.v5G.set_duplexing(duplexing = enums.EutraDuplexMode.FDD) \n
		No command help available \n
			:param duplexing: No help available
		"""
		param = Conversions.enum_scalar_to_str(duplexing, enums.EutraDuplexMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DUPLexing {param}')

	# noinspection PyTypeChecker
	def get_link(self) -> enums.UpDownDirection:
		"""SCPI: [SOURce<HW>]:BB:V5G:LINK \n
		Snippet: value: enums.UpDownDirection = driver.source.bb.v5G.get_link() \n
		Defines the transmission direction. \n
			:return: link: UP| DOWN UP corresponds to a UE signal (uplink) DOWN corresponds to a 5GNB signal (downlink)
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:LINK?')
		return Conversions.str_to_scalar_enum(response, enums.UpDownDirection)

	def set_link(self, link: enums.UpDownDirection) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:LINK \n
		Snippet: driver.source.bb.v5G.set_link(link = enums.UpDownDirection.DOWN) \n
		Defines the transmission direction. \n
			:param link: UP| DOWN UP corresponds to a UE signal (uplink) DOWN corresponds to a 5GNB signal (downlink)
		"""
		param = Conversions.enum_scalar_to_str(link, enums.UpDownDirection)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:LINK {param}')

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:PRESet \n
		Snippet: driver.source.bb.v5G.preset() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:V5G:STATe. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:PRESet \n
		Snippet: driver.source.bb.v5G.preset_with_opc() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:V5G:STATe. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:V5G:PRESet', opc_timeout_ms)

	def get_slength(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:V5G:SLENgth \n
		Snippet: value: int = driver.source.bb.v5G.get_slength() \n
		Specifies the sequence length of the signal in number of frames. The signal is calculated in advance and output in the
		arbitrary waveform generator. \n
			:return: slength: integer Range: 1 to dynamic
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:SLENgth?')
		return Conversions.str_to_int(response)

	def set_slength(self, slength: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:SLENgth \n
		Snippet: driver.source.bb.v5G.set_slength(slength = 1) \n
		Specifies the sequence length of the signal in number of frames. The signal is calculated in advance and output in the
		arbitrary waveform generator. \n
			:param slength: integer Range: 1 to dynamic
		"""
		param = Conversions.decimal_value_to_str(slength)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:SLENgth {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:V5G:STATe \n
		Snippet: value: bool = driver.source.bb.v5G.get_state() \n
		Activates the standard. \n
			:return: v_5_gstate: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, v_5_gstate: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:STATe \n
		Snippet: driver.source.bb.v5G.set_state(v_5_gstate = False) \n
		Activates the standard. \n
			:param v_5_gstate: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(v_5_gstate)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:STATe {param}')

	def get_version(self) -> str:
		"""SCPI: [SOURce]:BB:V5G:VERSion \n
		Snippet: value: str = driver.source.bb.v5G.get_version() \n
		No command help available \n
			:return: version: No help available
		"""
		response = self._core.io.query_str('SOURce:BB:V5G:VERSion?')
		return trim_str_response(response)

	def clone(self) -> 'V5G':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = V5G(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
