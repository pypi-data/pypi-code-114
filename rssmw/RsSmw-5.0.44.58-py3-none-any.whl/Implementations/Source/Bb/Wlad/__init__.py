from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Wlad:
	"""Wlad commands group definition. 109 total commands, 8 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("wlad", core, parent)

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
	def pconfig(self):
		"""pconfig commands group. 11 Sub-classes, 9 commands."""
		if not hasattr(self, '_pconfig'):
			from .Pconfig import Pconfig
			self._pconfig = Pconfig(self._core, self._cmd_group)
		return self._pconfig

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
	def get_dp_mode(self) -> enums.WlanadDmgPhyMode:
		"""SCPI: [SOURce<HW>]:BB:WLAD:DPMode \n
		Snippet: value: enums.WlanadDmgPhyMode = driver.source.bb.wlad.get_dp_mode() \n
		Sets the DMG PHY mode. \n
			:return: dp_mode: CONTrol| SINGle
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:DPMode?')
		return Conversions.str_to_scalar_enum(response, enums.WlanadDmgPhyMode)

	def set_dp_mode(self, dp_mode: enums.WlanadDmgPhyMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:DPMode \n
		Snippet: driver.source.bb.wlad.set_dp_mode(dp_mode = enums.WlanadDmgPhyMode.CONTrol) \n
		Sets the DMG PHY mode. \n
			:param dp_mode: CONTrol| SINGle
		"""
		param = Conversions.enum_scalar_to_str(dp_mode, enums.WlanadDmgPhyMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:DPMode {param}')

	# noinspection PyTypeChecker
	def get_ftype(self) -> enums.WlanadFrameType:
		"""SCPI: [SOURce<HW>]:BB:WLAD:FTYPe \n
		Snippet: value: enums.WlanadFrameType = driver.source.bb.wlad.get_ftype() \n
		Sets the IEEE 802.11ad frame type. \n
			:return: ftype: DATA| BEACon
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:FTYPe?')
		return Conversions.str_to_scalar_enum(response, enums.WlanadFrameType)

	def set_ftype(self, ftype: enums.WlanadFrameType) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:FTYPe \n
		Snippet: driver.source.bb.wlad.set_ftype(ftype = enums.WlanadFrameType.BEACon) \n
		Sets the IEEE 802.11ad frame type. \n
			:param ftype: DATA| BEACon
		"""
		param = Conversions.enum_scalar_to_str(ftype, enums.WlanadFrameType)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:FTYPe {param}')

	def get_itime(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:WLAD:ITIMe \n
		Snippet: value: float = driver.source.bb.wlad.get_itime() \n
		Sets the idle time, the time delay between the frames. \n
			:return: itime: float Range: 0 to 0.01
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:ITIMe?')
		return Conversions.str_to_float(response)

	def set_itime(self, itime: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:ITIMe \n
		Snippet: driver.source.bb.wlad.set_itime(itime = 1.0) \n
		Sets the idle time, the time delay between the frames. \n
			:param itime: float Range: 0 to 0.01
		"""
		param = Conversions.decimal_value_to_str(itime)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:ITIMe {param}')

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PRESet \n
		Snippet: driver.source.bb.wlad.preset() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command BB:WLAD:STATe. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PRESet \n
		Snippet: driver.source.bb.wlad.preset_with_opc() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command BB:WLAD:STATe. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:WLAD:PRESet', opc_timeout_ms)

	def get_slength(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:WLAD:SLENgth \n
		Snippet: value: int = driver.source.bb.wlad.get_slength() \n
		Sets the sequence length. \n
			:return: slength: integer Range: 1 to 53687
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:SLENgth?')
		return Conversions.str_to_int(response)

	def set_slength(self, slength: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:SLENgth \n
		Snippet: driver.source.bb.wlad.set_slength(slength = 1) \n
		Sets the sequence length. \n
			:param slength: integer Range: 1 to 53687
		"""
		param = Conversions.decimal_value_to_str(slength)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:SLENgth {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:WLAD:STATe \n
		Snippet: value: bool = driver.source.bb.wlad.get_state() \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:return: state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:STATe \n
		Snippet: driver.source.bb.wlad.set_state(state = False) \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:param state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:STATe {param}')

	def clone(self) -> 'Wlad':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Wlad(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
