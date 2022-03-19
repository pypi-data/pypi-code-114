from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gsm:
	"""Gsm commands group definition. 108 total commands, 19 Subgroups, 8 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gsm", core, parent)

	@property
	def aqPsk(self):
		"""aqPsk commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_aqPsk'):
			from .AqPsk import AqPsk
			self._aqPsk = AqPsk(self._core, self._cmd_group)
		return self._aqPsk

	@property
	def clock(self):
		"""clock commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_clock'):
			from .Clock import Clock
			self._clock = Clock(self._core, self._cmd_group)
		return self._clock

	@property
	def edge(self):
		"""edge commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_edge'):
			from .Edge import Edge
			self._edge = Edge(self._core, self._cmd_group)
		return self._edge

	@property
	def filterPy(self):
		"""filterPy commands group. 7 Sub-classes, 2 commands."""
		if not hasattr(self, '_filterPy'):
			from .FilterPy import FilterPy
			self._filterPy = FilterPy(self._core, self._cmd_group)
		return self._filterPy

	@property
	def foffset(self):
		"""foffset commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_foffset'):
			from .Foffset import Foffset
			self._foffset = Foffset(self._core, self._cmd_group)
		return self._foffset

	@property
	def frame(self):
		"""frame commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_frame'):
			from .Frame import Frame
			self._frame = Frame(self._core, self._cmd_group)
		return self._frame

	@property
	def fsk(self):
		"""fsk commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fsk'):
			from .Fsk import Fsk
			self._fsk = Fsk(self._core, self._cmd_group)
		return self._fsk

	@property
	def h16Qam(self):
		"""h16Qam commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_h16Qam'):
			from .H16Qam import H16Qam
			self._h16Qam = H16Qam(self._core, self._cmd_group)
		return self._h16Qam

	@property
	def h32Qam(self):
		"""h32Qam commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_h32Qam'):
			from .H32Qam import H32Qam
			self._h32Qam = H32Qam(self._core, self._cmd_group)
		return self._h32Qam

	@property
	def hqpsk(self):
		"""hqpsk commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hqpsk'):
			from .Hqpsk import Hqpsk
			self._hqpsk = Hqpsk(self._core, self._cmd_group)
		return self._hqpsk

	@property
	def mframe(self):
		"""mframe commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_mframe'):
			from .Mframe import Mframe
			self._mframe = Mframe(self._core, self._cmd_group)
		return self._mframe

	@property
	def n16Qam(self):
		"""n16Qam commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_n16Qam'):
			from .N16Qam import N16Qam
			self._n16Qam = N16Qam(self._core, self._cmd_group)
		return self._n16Qam

	@property
	def n32Qam(self):
		"""n32Qam commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_n32Qam'):
			from .N32Qam import N32Qam
			self._n32Qam = N32Qam(self._core, self._cmd_group)
		return self._n32Qam

	@property
	def pramp(self):
		"""pramp commands group. 1 Sub-classes, 4 commands."""
		if not hasattr(self, '_pramp'):
			from .Pramp import Pramp
			self._pramp = Pramp(self._core, self._cmd_group)
		return self._pramp

	@property
	def sattenuation(self):
		"""sattenuation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sattenuation'):
			from .Sattenuation import Sattenuation
			self._sattenuation = Sattenuation(self._core, self._cmd_group)
		return self._sattenuation

	@property
	def setting(self):
		"""setting commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_setting'):
			from .Setting import Setting
			self._setting = Setting(self._core, self._cmd_group)
		return self._setting

	@property
	def symbolRate(self):
		"""symbolRate commands group. 0 Sub-classes, 2 commands."""
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

	def get_flength(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:GSM:FLENgth \n
		Snippet: value: int = driver.source.bb.gsm.get_flength() \n
		Sets the sequence length of the generated arbitrary waveform file in number of frames. This parameter applies to GSM
		modes Single or Double framed. For GSM mode Framed Double, this command is query only, since the length of the generated
		ARB file is determined by the parameter Frame Repetition ([:SOURce<hw>]:BB:GSM:FRAMe<di>:REPetitions) for both frames:
		Sequence Length = Frame Repetition of Frame 1 + Frame Repetition of Frame 2. For GSM mode (BB:GSM:MODE) set to Unframed,
		the length of the generated ARB file is set in symbols with the command [:SOURce<hw>]:BB:GSM:SLENgth. \n
			:return: flength: integer Range: 1 to max
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GSM:FLENgth?')
		return Conversions.str_to_int(response)

	def set_flength(self, flength: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:GSM:FLENgth \n
		Snippet: driver.source.bb.gsm.set_flength(flength = 1) \n
		Sets the sequence length of the generated arbitrary waveform file in number of frames. This parameter applies to GSM
		modes Single or Double framed. For GSM mode Framed Double, this command is query only, since the length of the generated
		ARB file is determined by the parameter Frame Repetition ([:SOURce<hw>]:BB:GSM:FRAMe<di>:REPetitions) for both frames:
		Sequence Length = Frame Repetition of Frame 1 + Frame Repetition of Frame 2. For GSM mode (BB:GSM:MODE) set to Unframed,
		the length of the generated ARB file is set in symbols with the command [:SOURce<hw>]:BB:GSM:SLENgth. \n
			:param flength: integer Range: 1 to max
		"""
		param = Conversions.decimal_value_to_str(flength)
		self._core.io.write(f'SOURce<HwInstance>:BB:GSM:FLENgth {param}')

	def get_fone(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GSM:FONE \n
		Snippet: value: bool = driver.source.bb.gsm.get_fone() \n
		A modulating bit stream consisting of consecutive ones is used for inactive slots (according to GSM 05.04) .
		If this parameter is disabled, the inactive slots are filled in with 0. \n
			:return: fone: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GSM:FONE?')
		return Conversions.str_to_bool(response)

	def set_fone(self, fone: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GSM:FONE \n
		Snippet: driver.source.bb.gsm.set_fone(fone = False) \n
		A modulating bit stream consisting of consecutive ones is used for inactive slots (according to GSM 05.04) .
		If this parameter is disabled, the inactive slots are filled in with 0. \n
			:param fone: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(fone)
		self._core.io.write(f'SOURce<HwInstance>:BB:GSM:FONE {param}')

	# noinspection PyTypeChecker
	def get_format_py(self) -> enums.GsmModTypeGsm:
		"""SCPI: [SOURce<HW>]:BB:GSM:FORMat \n
		Snippet: value: enums.GsmModTypeGsm = driver.source.bb.gsm.get_format_py() \n
		The command selects the modulation type. \n
			:return: format_py: MSK| FSK2
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GSM:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.GsmModTypeGsm)

	def set_format_py(self, format_py: enums.GsmModTypeGsm) -> None:
		"""SCPI: [SOURce<HW>]:BB:GSM:FORMat \n
		Snippet: driver.source.bb.gsm.set_format_py(format_py = enums.GsmModTypeGsm.FSK2) \n
		The command selects the modulation type. \n
			:param format_py: MSK| FSK2
		"""
		param = Conversions.enum_scalar_to_str(format_py, enums.GsmModTypeGsm)
		self._core.io.write(f'SOURce<HwInstance>:BB:GSM:FORMat {param}')

	def get_is_length(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GSM:ISLength \n
		Snippet: value: bool = driver.source.bb.gsm.get_is_length() \n
		Selects constant slot length. \n
			:return: is_length: 1| ON| 0| OFF For normal symbol rate mode: The command selects whether the 1/4 symbol of a GSM slot is ignored or compensated for by an extra symbol every 4th slot. For higher symbol rate mode: The command selects whether the 1/2 symbol of an average slot with a length of 187.5 symbols are ignored or compensated for by an extra symbol every second slot. ON In normal symbol rate mode, all slots are 156 symbols long In higher symbol rate mode, all slots are 187 symbols long OFF In normal symbol rate mode, some slots are 157 symbols long In higher symbol rate mode, some slots are 188 symbols long
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GSM:ISLength?')
		return Conversions.str_to_bool(response)

	def set_is_length(self, is_length: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GSM:ISLength \n
		Snippet: driver.source.bb.gsm.set_is_length(is_length = False) \n
		Selects constant slot length. \n
			:param is_length: 1| ON| 0| OFF For normal symbol rate mode: The command selects whether the 1/4 symbol of a GSM slot is ignored or compensated for by an extra symbol every 4th slot. For higher symbol rate mode: The command selects whether the 1/2 symbol of an average slot with a length of 187.5 symbols are ignored or compensated for by an extra symbol every second slot. ON In normal symbol rate mode, all slots are 156 symbols long In higher symbol rate mode, all slots are 187 symbols long OFF In normal symbol rate mode, some slots are 157 symbols long In higher symbol rate mode, some slots are 188 symbols long
		"""
		param = Conversions.bool_to_str(is_length)
		self._core.io.write(f'SOURce<HwInstance>:BB:GSM:ISLength {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.GsmMode:
		"""SCPI: [SOURce<HW>]:BB:GSM:MODE \n
		Snippet: value: enums.GsmMode = driver.source.bb.gsm.get_mode() \n
		The command selects GSM mode. \n
			:return: mode: UNFRamed| SINGle| DOUBle| MULTiframe UNFRamed Modulation signal without slot and frame structure. SINGle Modulation signal consisting of one frame. DOUBle Modulation signal in which two frames are defined and then combined by some method into a single multiframe signal. MULTiframe Multiframe signal.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GSM:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.GsmMode)

	def set_mode(self, mode: enums.GsmMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:GSM:MODE \n
		Snippet: driver.source.bb.gsm.set_mode(mode = enums.GsmMode.DOUBle) \n
		The command selects GSM mode. \n
			:param mode: UNFRamed| SINGle| DOUBle| MULTiframe UNFRamed Modulation signal without slot and frame structure. SINGle Modulation signal consisting of one frame. DOUBle Modulation signal in which two frames are defined and then combined by some method into a single multiframe signal. MULTiframe Multiframe signal.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.GsmMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:GSM:MODE {param}')

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:GSM:PRESet \n
		Snippet: driver.source.bb.gsm.preset() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:GSM:STATe. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:GSM:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:GSM:PRESet \n
		Snippet: driver.source.bb.gsm.preset_with_opc() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:GSM:STATe. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:GSM:PRESet', opc_timeout_ms)

	# noinspection PyTypeChecker
	def get_smode(self) -> enums.GsmSimMode:
		"""SCPI: [SOURce<HW>]:BB:GSM:SMODe \n
		Snippet: value: enums.GsmSimMode = driver.source.bb.gsm.get_smode() \n
		Selects the modulation signal for the mode Unframed (BB:GSM:MODE UNFR) . The modulation type and filter type are set in
		accordance with the selection.
			INTRO_CMD_HELP: The available simulation modes depend on the selected symbol rate: \n
			- Normal Symbol Rate - GSM, EDGE (8PSK) , AQPSK, 16QAM and 32QAM
			- Higher Symbol Rate - HSR QPSK, HSR 16QAM and HSR 32QAM.
		Note:'Higher Symbol Rate' Mode and 'Simulation Modes' AQPSK, 16QAM, 32QAM, HSR QPSK, HSR 16QAM and HSR 32QAM are
		available for instruments equipped with option R&S SMW-K41 only. \n
			:return: smode: GSM| EDGE| N16Qam| N32Qam| HQPSk| H16Qam| H32Qam| AQPSk
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GSM:SMODe?')
		return Conversions.str_to_scalar_enum(response, enums.GsmSimMode)

	def set_smode(self, smode: enums.GsmSimMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:GSM:SMODe \n
		Snippet: driver.source.bb.gsm.set_smode(smode = enums.GsmSimMode.AQPSk) \n
		Selects the modulation signal for the mode Unframed (BB:GSM:MODE UNFR) . The modulation type and filter type are set in
		accordance with the selection.
			INTRO_CMD_HELP: The available simulation modes depend on the selected symbol rate: \n
			- Normal Symbol Rate - GSM, EDGE (8PSK) , AQPSK, 16QAM and 32QAM
			- Higher Symbol Rate - HSR QPSK, HSR 16QAM and HSR 32QAM.
		Note:'Higher Symbol Rate' Mode and 'Simulation Modes' AQPSK, 16QAM, 32QAM, HSR QPSK, HSR 16QAM and HSR 32QAM are
		available for instruments equipped with option R&S SMW-K41 only. \n
			:param smode: GSM| EDGE| N16Qam| N32Qam| HQPSk| H16Qam| H32Qam| AQPSk
		"""
		param = Conversions.enum_scalar_to_str(smode, enums.GsmSimMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:GSM:SMODe {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GSM:STATe \n
		Snippet: value: bool = driver.source.bb.gsm.get_state() \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GSM:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GSM:STATe \n
		Snippet: driver.source.bb.gsm.set_state(state = False) \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GSM:STATe {param}')

	def clone(self) -> 'Gsm':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Gsm(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
