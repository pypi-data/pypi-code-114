from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tdscdma:
	"""Tdscdma commands group definition. 357 total commands, 12 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tdscdma", core, parent)

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
	def copy(self):
		"""copy commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_copy'):
			from .Copy import Copy
			self._copy = Copy(self._core, self._cmd_group)
		return self._copy

	@property
	def crate(self):
		"""crate commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_crate'):
			from .Crate import Crate
			self._crate = Crate(self._core, self._cmd_group)
		return self._crate

	@property
	def down(self):
		"""down commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_down'):
			from .Down import Down
			self._down = Down(self._core, self._cmd_group)
		return self._down

	@property
	def filterPy(self):
		"""filterPy commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_filterPy'):
			from .FilterPy import FilterPy
			self._filterPy = FilterPy(self._core, self._cmd_group)
		return self._filterPy

	@property
	def power(self):
		"""power commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def pramp(self):
		"""pramp commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_pramp'):
			from .Pramp import Pramp
			self._pramp = Pramp(self._core, self._cmd_group)
		return self._pramp

	@property
	def setting(self):
		"""setting commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_setting'):
			from .Setting import Setting
			self._setting = Setting(self._core, self._cmd_group)
		return self._setting

	@property
	def trigger(self):
		"""trigger commands group. 5 Sub-classes, 5 commands."""
		if not hasattr(self, '_trigger'):
			from .Trigger import Trigger
			self._trigger = Trigger(self._core, self._cmd_group)
		return self._trigger

	@property
	def up(self):
		"""up commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_up'):
			from .Up import Up
			self._up = Up(self._core, self._cmd_group)
		return self._up

	@property
	def waveform(self):
		"""waveform commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_waveform'):
			from .Waveform import Waveform
			self._waveform = Waveform(self._core, self._cmd_group)
		return self._waveform

	# noinspection PyTypeChecker
	def get_link(self) -> enums.LinkDir:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:LINK \n
		Snippet: value: enums.LinkDir = driver.source.bb.tdscdma.get_link() \n
		Defines the transmission direction. \n
			:return: link: FORWard| DOWN | REVerse| UP
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TDSCdma:LINK?')
		return Conversions.str_to_scalar_enum(response, enums.LinkDir)

	def set_link(self, link: enums.LinkDir) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:LINK \n
		Snippet: driver.source.bb.tdscdma.set_link(link = enums.LinkDir.DOWN) \n
		Defines the transmission direction. \n
			:param link: FORWard| DOWN | REVerse| UP
		"""
		param = Conversions.enum_scalar_to_str(link, enums.LinkDir)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:LINK {param}')

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:PRESet \n
		Snippet: driver.source.bb.tdscdma.preset() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:TDSCdma:STATe. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:PRESet \n
		Snippet: driver.source.bb.tdscdma.preset_with_opc() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:TDSCdma:STATe. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:TDSCdma:PRESet', opc_timeout_ms)

	def reset(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:RESet \n
		Snippet: driver.source.bb.tdscdma.reset() \n
		Resets all cells to the predefined settings. The reset applies to the selected link direction. An overview is provided by
		table in 'Set to Default'. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:RESet')

	def reset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:RESet \n
		Snippet: driver.source.bb.tdscdma.reset_with_opc() \n
		Resets all cells to the predefined settings. The reset applies to the selected link direction. An overview is provided by
		table in 'Set to Default'. \n
		Same as reset, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:TDSCdma:RESet', opc_timeout_ms)

	def get_slength(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:SLENgth \n
		Snippet: value: int = driver.source.bb.tdscdma.get_slength() \n
		Sets the sequence length of the arbitrary waveform component of the TD-SCDMA signal in the number of frames.
		This component is calculated in advance and output in the arbitrary waveform generator. It is added to the realtime
		signal components. \n
			:return: slength: integer Range: 1 to 5000
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TDSCdma:SLENgth?')
		return Conversions.str_to_int(response)

	def set_slength(self, slength: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:SLENgth \n
		Snippet: driver.source.bb.tdscdma.set_slength(slength = 1) \n
		Sets the sequence length of the arbitrary waveform component of the TD-SCDMA signal in the number of frames.
		This component is calculated in advance and output in the arbitrary waveform generator. It is added to the realtime
		signal components. \n
			:param slength: integer Range: 1 to 5000
		"""
		param = Conversions.decimal_value_to_str(slength)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:SLENgth {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:STATe \n
		Snippet: value: bool = driver.source.bb.tdscdma.get_state() \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TDSCdma:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:STATe \n
		Snippet: driver.source.bb.tdscdma.set_state(state = False) \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:STATe {param}')

	def get_version(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:VERSion \n
		Snippet: value: str = driver.source.bb.tdscdma.get_version() \n
		Queries the version of the TD-SCDMA standard underlying the definitions. \n
			:return: version: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TDSCdma:VERSion?')
		return trim_str_response(response)

	def clone(self) -> 'Tdscdma':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tdscdma(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
