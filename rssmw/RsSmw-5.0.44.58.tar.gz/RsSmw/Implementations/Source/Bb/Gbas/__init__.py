from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gbas:
	"""Gbas commands group definition. 190 total commands, 8 Subgroups, 9 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gbas", core, parent)

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
	def filterPy(self):
		"""filterPy commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_filterPy'):
			from .FilterPy import FilterPy
			self._filterPy = FilterPy(self._core, self._cmd_group)
		return self._filterPy

	@property
	def mset(self):
		"""mset commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_mset'):
			from .Mset import Mset
			self._mset = Mset(self._core, self._cmd_group)
		return self._mset

	@property
	def setting(self):
		"""setting commands group. 0 Sub-classes, 4 commands."""
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
	def vdb(self):
		"""vdb commands group. 12 Sub-classes, 1 commands."""
		if not hasattr(self, '_vdb'):
			from .Vdb import Vdb
			self._vdb = Vdb(self._core, self._cmd_group)
		return self._vdb

	@property
	def waveform(self):
		"""waveform commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_waveform'):
			from .Waveform import Waveform
			self._waveform = Waveform(self._core, self._cmd_group)
		return self._waveform

	def get_gpow(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GBAS:GPOW \n
		Snippet: value: bool = driver.source.bb.gbas.get_gpow() \n
		Enables gated power mode. \n
			:return: gpow: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GBAS:GPOW?')
		return Conversions.str_to_bool(response)

	def set_gpow(self, gpow: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:GPOW \n
		Snippet: driver.source.bb.gbas.set_gpow(gpow = False) \n
		Enables gated power mode. \n
			:param gpow: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(gpow)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:GPOW {param}')

	def get_mf_channels(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GBAS:MFCHannels \n
		Snippet: value: bool = driver.source.bb.gbas.get_mf_channels() \n
		No command help available \n
			:return: mfch: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GBAS:MFCHannels?')
		return Conversions.str_to_bool(response)

	def set_mf_channels(self, mfch: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:MFCHannels \n
		Snippet: driver.source.bb.gbas.set_mf_channels(mfch = False) \n
		No command help available \n
			:param mfch: No help available
		"""
		param = Conversions.bool_to_str(mfch)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:MFCHannels {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.GbasMode:
		"""SCPI: [SOURce<HW>]:BB:GBAS:MODE \n
		Snippet: value: enums.GbasMode = driver.source.bb.gbas.get_mode() \n
		Sets GBAS mode. Select between GBAS (LAAS) header information or SCAT-I header information. \n
			:return: scat: GBAS| SCAT
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GBAS:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.GbasMode)

	def set_mode(self, scat: enums.GbasMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:MODE \n
		Snippet: driver.source.bb.gbas.set_mode(scat = enums.GbasMode.GBAS) \n
		Sets GBAS mode. Select between GBAS (LAAS) header information or SCAT-I header information. \n
			:param scat: GBAS| SCAT
		"""
		param = Conversions.enum_scalar_to_str(scat, enums.GbasMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:MODE {param}')

	def get_no_frames(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:GBAS:NOFRames \n
		Snippet: value: int = driver.source.bb.gbas.get_no_frames() \n
		Queries the number of VDB frames. \n
			:return: no_frame: integer Range: 1 to 12500
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GBAS:NOFRames?')
		return Conversions.str_to_int(response)

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:PRESet \n
		Snippet: driver.source.bb.gbas.preset() \n
		Sets all parameters to their default values (*RST values specified for the commands) . Not affected is the state set with
		the command SOURce<hw>:BB:GBAS:STATe \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:PRESet \n
		Snippet: driver.source.bb.gbas.preset_with_opc() \n
		Sets all parameters to their default values (*RST values specified for the commands) . Not affected is the state set with
		the command SOURce<hw>:BB:GBAS:STATe \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:GBAS:PRESet', opc_timeout_ms)

	def get_scati(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GBAS:SCATi \n
		Snippet: value: bool = driver.source.bb.gbas.get_scati() \n
		No command help available \n
			:return: scat: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GBAS:SCATi?')
		return Conversions.str_to_bool(response)

	def set_scati(self, scat: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:SCATi \n
		Snippet: driver.source.bb.gbas.set_scati(scat = False) \n
		No command help available \n
			:param scat: No help available
		"""
		param = Conversions.bool_to_str(scat)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:SCATi {param}')

	def get_sr_info(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:GBAS:SRINfo \n
		Snippet: value: str = driver.source.bb.gbas.get_sr_info() \n
		Queries the used sample rate. \n
			:return: sr_info: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GBAS:SRINfo?')
		return trim_str_response(response)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GBAS:STATe \n
		Snippet: value: bool = driver.source.bb.gbas.get_state() \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:return: state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GBAS:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:STATe \n
		Snippet: driver.source.bb.gbas.set_state(state = False) \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:param state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:STATe {param}')

	def get_version(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VERSion \n
		Snippet: value: str = driver.source.bb.gbas.get_version() \n
		Queries the GBAS specification for that the commands are valid. \n
			:return: version: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GBAS:VERSion?')
		return trim_str_response(response)

	def clone(self) -> 'Gbas':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Gbas(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
