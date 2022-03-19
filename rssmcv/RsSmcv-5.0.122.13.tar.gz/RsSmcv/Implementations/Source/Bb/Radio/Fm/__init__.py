from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fm:
	"""Fm commands group definition. 167 total commands, 8 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fm", core, parent)

	@property
	def apLayer(self):
		"""apLayer commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_apLayer'):
			from .ApLayer import ApLayer
			self._apLayer = ApLayer(self._core, self._cmd_group)
		return self._apLayer

	@property
	def audGen(self):
		"""audGen commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_audGen'):
			from .AudGen import AudGen
			self._audGen = AudGen(self._core, self._cmd_group)
		return self._audGen

	@property
	def audio(self):
		"""audio commands group. 0 Sub-classes, 7 commands."""
		if not hasattr(self, '_audio'):
			from .Audio import Audio
			self._audio = Audio(self._core, self._cmd_group)
		return self._audio

	@property
	def darc(self):
		"""darc commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_darc'):
			from .Darc import Darc
			self._darc = Darc(self._core, self._cmd_group)
		return self._darc

	@property
	def pilot(self):
		"""pilot commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pilot'):
			from .Pilot import Pilot
			self._pilot = Pilot(self._core, self._cmd_group)
		return self._pilot

	@property
	def rds(self):
		"""rds commands group. 7 Sub-classes, 11 commands."""
		if not hasattr(self, '_rds'):
			from .Rds import Rds
			self._rds = Rds(self._core, self._cmd_group)
		return self._rds

	@property
	def setting(self):
		"""setting commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_setting'):
			from .Setting import Setting
			self._setting = Setting(self._core, self._cmd_group)
		return self._setting

	@property
	def special(self):
		"""special commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_special'):
			from .Special import Special
			self._special = Special(self._core, self._cmd_group)
		return self._special

	# noinspection PyTypeChecker
	def get_input_py(self) -> enums.AudioBcInputSignal:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:INPut \n
		Snippet: value: enums.AudioBcInputSignal = driver.source.bb.radio.fm.get_input_py() \n
		Sets the audio source for the FM modulator signal. \n
			:return: input_py: EXTernal| AGENerator| APLayer| OFF EXTernal Uses an external audio signal input at the 'User 2' connector. The audio source is fixed to 'Source S/PDIF', see [:SOURcehw]:BB:RADio:FM:AUDio:SOURce?. AGENerator Uses an internal audio generator as the signal source. APLayer Uses an audio player file, that is saved to the memory of the R&S SMCV100B. OFF Disables the audio source for the FM modulator.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:INPut?')
		return Conversions.str_to_scalar_enum(response, enums.AudioBcInputSignal)

	def set_input_py(self, input_py: enums.AudioBcInputSignal) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:INPut \n
		Snippet: driver.source.bb.radio.fm.set_input_py(input_py = enums.AudioBcInputSignal.AGENerator) \n
		Sets the audio source for the FM modulator signal. \n
			:param input_py: EXTernal| AGENerator| APLayer| OFF EXTernal Uses an external audio signal input at the 'User 2' connector. The audio source is fixed to 'Source S/PDIF', see [:SOURcehw]:BB:RADio:FM:AUDio:SOURce?. AGENerator Uses an internal audio generator as the signal source. APLayer Uses an audio player file, that is saved to the memory of the R&S SMCV100B. OFF Disables the audio source for the FM modulator.
		"""
		param = Conversions.enum_scalar_to_str(input_py, enums.AudioBcInputSignal)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:INPut {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.AudioBcFmModulationMode:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:MODE \n
		Snippet: value: enums.AudioBcFmModulationMode = driver.source.bb.radio.fm.get_mode() \n
		Sets the mode. \n
			:return: mode: MONO| STEReo MONO Feeds a mono signal to the modulator with band limitation 15 kHz. STEReo Feeds a stereo signal to the modulator.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.AudioBcFmModulationMode)

	def set_mode(self, mode: enums.AudioBcFmModulationMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:MODE \n
		Snippet: driver.source.bb.radio.fm.set_mode(mode = enums.AudioBcFmModulationMode.MONO) \n
		Sets the mode. \n
			:param mode: MONO| STEReo MONO Feeds a mono signal to the modulator with band limitation 15 kHz. STEReo Feeds a stereo signal to the modulator.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.AudioBcFmModulationMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:MODE {param}')

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:PRESet \n
		Snippet: driver.source.bb.radio.fm.preset() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:AM|FM|FM:RDS:STATe. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:PRESet \n
		Snippet: driver.source.bb.radio.fm.preset_with_opc() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:AM|FM|FM:RDS:STATe. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmcv.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:RADio:FM:PRESet', opc_timeout_ms)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:STATe \n
		Snippet: value: bool = driver.source.bb.radio.fm.get_state() \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:STATe \n
		Snippet: driver.source.bb.radio.fm.set_state(state = False) \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:STATe {param}')

	def clone(self) -> 'Fm':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Fm(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
