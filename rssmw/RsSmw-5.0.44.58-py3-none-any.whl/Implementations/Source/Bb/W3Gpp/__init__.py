from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class W3Gpp:
	"""W3Gpp commands group definition. 561 total commands, 14 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("w3Gpp", core, parent)

	@property
	def bstation(self):
		"""bstation commands group. 13 Sub-classes, 1 commands."""
		if not hasattr(self, '_bstation'):
			from .Bstation import Bstation
			self._bstation = Bstation(self._core, self._cmd_group)
		return self._bstation

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
		"""copy commands group. 1 Sub-classes, 3 commands."""
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
	def filterPy(self):
		"""filterPy commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_filterPy'):
			from .FilterPy import FilterPy
			self._filterPy = FilterPy(self._core, self._cmd_group)
		return self._filterPy

	@property
	def gpp3(self):
		"""gpp3 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gpp3'):
			from .Gpp3 import Gpp3
			self._gpp3 = Gpp3(self._core, self._cmd_group)
		return self._gpp3

	@property
	def mstation(self):
		"""mstation commands group. 14 Sub-classes, 1 commands."""
		if not hasattr(self, '_mstation'):
			from .Mstation import Mstation
			self._mstation = Mstation(self._core, self._cmd_group)
		return self._mstation

	@property
	def power(self):
		"""power commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def pparameter(self):
		"""pparameter commands group. 3 Sub-classes, 2 commands."""
		if not hasattr(self, '_pparameter'):
			from .Pparameter import Pparameter
			self._pparameter = Pparameter(self._core, self._cmd_group)
		return self._pparameter

	@property
	def setting(self):
		"""setting commands group. 2 Sub-classes, 4 commands."""
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
	def ts25141(self):
		"""ts25141 commands group. 8 Sub-classes, 4 commands."""
		if not hasattr(self, '_ts25141'):
			from .Ts25141 import Ts25141
			self._ts25141 = Ts25141(self._core, self._cmd_group)
		return self._ts25141

	@property
	def waveform(self):
		"""waveform commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_waveform'):
			from .Waveform import Waveform
			self._waveform = Waveform(self._core, self._cmd_group)
		return self._waveform

	# noinspection PyTypeChecker
	def get_link(self) -> enums.LinkDir:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:LINK \n
		Snippet: value: enums.LinkDir = driver.source.bb.w3Gpp.get_link() \n
		The command defines the transmission direction. The signal either corresponds to that of a base station (FORWard|DOWN) or
		that of a user equipment (REVerse|UP) . \n
			:return: link: DOWN| UP| FORWard| REVerse
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:W3GPp:LINK?')
		return Conversions.str_to_scalar_enum(response, enums.LinkDir)

	def set_link(self, link: enums.LinkDir) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:LINK \n
		Snippet: driver.source.bb.w3Gpp.set_link(link = enums.LinkDir.DOWN) \n
		The command defines the transmission direction. The signal either corresponds to that of a base station (FORWard|DOWN) or
		that of a user equipment (REVerse|UP) . \n
			:param link: DOWN| UP| FORWard| REVerse
		"""
		param = Conversions.enum_scalar_to_str(link, enums.LinkDir)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:LINK {param}')

	# noinspection PyTypeChecker
	def get_lreference(self) -> enums.WcdmaLevRef:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:LREFerence \n
		Snippet: value: enums.WcdmaLevRef = driver.source.bb.w3Gpp.get_lreference() \n
		Determines the power reference for the calculation of the output signal power in uplink direction. \n
			:return: reference: RMS| DPCC| PMP| LPP| EDCH| HACK| PCQI RMS = RMS Power, DPCC = First DPCCH, PMP = PRACH Message Part, LPP = Last PRACH Preamble, EDCH = First E-DCH, HACK = First HARQ-ACK, PCQI = First PCI/CQI
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:W3GPp:LREFerence?')
		return Conversions.str_to_scalar_enum(response, enums.WcdmaLevRef)

	def set_lreference(self, reference: enums.WcdmaLevRef) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:LREFerence \n
		Snippet: driver.source.bb.w3Gpp.set_lreference(reference = enums.WcdmaLevRef.DPCC) \n
		Determines the power reference for the calculation of the output signal power in uplink direction. \n
			:param reference: RMS| DPCC| PMP| LPP| EDCH| HACK| PCQI RMS = RMS Power, DPCC = First DPCCH, PMP = PRACH Message Part, LPP = Last PRACH Preamble, EDCH = First E-DCH, HACK = First HARQ-ACK, PCQI = First PCI/CQI
		"""
		param = Conversions.enum_scalar_to_str(reference, enums.WcdmaLevRef)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:LREFerence {param}')

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:PRESet \n
		Snippet: driver.source.bb.w3Gpp.preset() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:W3GPp:STATe. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:PRESet \n
		Snippet: driver.source.bb.w3Gpp.preset_with_opc() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:W3GPp:STATe. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:W3GPp:PRESet', opc_timeout_ms)

	def get_slength(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:SLENgth \n
		Snippet: value: int = driver.source.bb.w3Gpp.get_slength() \n
		Defines the sequence length of the arbitrary waveform component of the 3GPP signal in the number of frames.
		This component is calculated in advance and output in the arbitrary waveform generator. It is added to the realtime
		signal components (Enhanced Channels) . When working in Advanced Mode (W3GP:BST1:CHAN:HSDP:HSET:AMOD ON) , it is
		recommended to adjust the current ARB sequence length to the suggested one. \n
			:return: slength: integer Range: 1 to Max. No. of Frames = Arbitrary waveform memory size/(3.84 Mcps x 10 ms) .
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:W3GPp:SLENgth?')
		return Conversions.str_to_int(response)

	def set_slength(self, slength: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:SLENgth \n
		Snippet: driver.source.bb.w3Gpp.set_slength(slength = 1) \n
		Defines the sequence length of the arbitrary waveform component of the 3GPP signal in the number of frames.
		This component is calculated in advance and output in the arbitrary waveform generator. It is added to the realtime
		signal components (Enhanced Channels) . When working in Advanced Mode (W3GP:BST1:CHAN:HSDP:HSET:AMOD ON) , it is
		recommended to adjust the current ARB sequence length to the suggested one. \n
			:param slength: integer Range: 1 to Max. No. of Frames = Arbitrary waveform memory size/(3.84 Mcps x 10 ms) .
		"""
		param = Conversions.decimal_value_to_str(slength)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:SLENgth {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:STATe \n
		Snippet: value: bool = driver.source.bb.w3Gpp.get_state() \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:W3GPp:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:STATe \n
		Snippet: driver.source.bb.w3Gpp.set_state(state = False) \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:STATe {param}')

	def clone(self) -> 'W3Gpp':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = W3Gpp(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
