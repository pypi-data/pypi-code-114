from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Audio:
	"""Audio commands group definition. 7 total commands, 0 Subgroups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("audio", core, parent)

	def get_af_1(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:AUDio:AF1 \n
		Snippet: value: bool = driver.source.bb.radio.fm.audio.get_af_1() \n
		Enables or disables the audio channel. \n
			:return: audio_l: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:AUDio:AF1?')
		return Conversions.str_to_bool(response)

	def set_af_1(self, audio_l: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:AUDio:AF1 \n
		Snippet: driver.source.bb.radio.fm.audio.set_af_1(audio_l = False) \n
		Enables or disables the audio channel. \n
			:param audio_l: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(audio_l)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:AUDio:AF1 {param}')

	def get_af_2(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:AUDio:AF2 \n
		Snippet: value: bool = driver.source.bb.radio.fm.audio.get_af_2() \n
		Enables or disables the audio channel. \n
			:return: audio_r: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:AUDio:AF2?')
		return Conversions.str_to_bool(response)

	def set_af_2(self, audio_r: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:AUDio:AF2 \n
		Snippet: driver.source.bb.radio.fm.audio.set_af_2(audio_r = False) \n
		Enables or disables the audio channel. \n
			:param audio_r: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(audio_r)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:AUDio:AF2 {param}')

	def get_deviation(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:AUDio:DEViation \n
		Snippet: value: float = driver.source.bb.radio.fm.audio.get_deviation() \n
		Queries the actual frequency deviation. \n
			:return: freq_dev_audio: float Range: 0 to 999.99, Unit: kHz
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:AUDio:DEViation?')
		return Conversions.str_to_float(response)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.AudioBcFmInputSignalAfMode:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:AUDio:MODE \n
		Snippet: value: enums.AudioBcFmInputSignalAfMode = driver.source.bb.radio.fm.audio.get_mode() \n
		Sets the relationship of the two audio channels with respect to each other. \n
			:return: af_mode: LEFT| RIGHt| RELeft| REMLeft| RNELeft
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:AUDio:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.AudioBcFmInputSignalAfMode)

	def set_mode(self, af_mode: enums.AudioBcFmInputSignalAfMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:AUDio:MODE \n
		Snippet: driver.source.bb.radio.fm.audio.set_mode(af_mode = enums.AudioBcFmInputSignalAfMode.LEFT) \n
		Sets the relationship of the two audio channels with respect to each other. \n
			:param af_mode: LEFT| RIGHt| RELeft| REMLeft| RNELeft
		"""
		param = Conversions.enum_scalar_to_str(af_mode, enums.AudioBcFmInputSignalAfMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:AUDio:MODE {param}')

	def get_ndeviation(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:AUDio:NDEViation \n
		Snippet: value: float = driver.source.bb.radio.fm.audio.get_ndeviation() \n
		Defines the signal deviation, that is the deviation only caused by the audio signals. \n
			:return: mon_freq_dev_audio: float Range: 0 to 100, Unit: kHz
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:AUDio:NDEViation?')
		return Conversions.str_to_float(response)

	def set_ndeviation(self, mon_freq_dev_audio: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:AUDio:NDEViation \n
		Snippet: driver.source.bb.radio.fm.audio.set_ndeviation(mon_freq_dev_audio = 1.0) \n
		Defines the signal deviation, that is the deviation only caused by the audio signals. \n
			:param mon_freq_dev_audio: float Range: 0 to 100, Unit: kHz
		"""
		param = Conversions.decimal_value_to_str(mon_freq_dev_audio)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:AUDio:NDEViation {param}')

	# noinspection PyTypeChecker
	def get_preemphasis(self) -> enums.AudioBcFmModulationPreemphasis:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:AUDio:PREemphasis \n
		Snippet: value: enums.AudioBcFmModulationPreemphasis = driver.source.bb.radio.fm.audio.get_preemphasis() \n
		Sets the preemphasis factor for the signal to noise ratio improvement. \n
			:return: preemphasis: OFF| D50us| D75us
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:AUDio:PREemphasis?')
		return Conversions.str_to_scalar_enum(response, enums.AudioBcFmModulationPreemphasis)

	def set_preemphasis(self, preemphasis: enums.AudioBcFmModulationPreemphasis) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:AUDio:PREemphasis \n
		Snippet: driver.source.bb.radio.fm.audio.set_preemphasis(preemphasis = enums.AudioBcFmModulationPreemphasis.D50us) \n
		Sets the preemphasis factor for the signal to noise ratio improvement. \n
			:param preemphasis: OFF| D50us| D75us
		"""
		param = Conversions.enum_scalar_to_str(preemphasis, enums.AudioBcFmModulationPreemphasis)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:AUDio:PREemphasis {param}')

	# noinspection PyTypeChecker
	def get_source(self) -> enums.BcInputSignalSource:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:AUDio:SOURce \n
		Snippet: value: enums.BcInputSignalSource = driver.source.bb.radio.fm.audio.get_source() \n
		Queries the audio source. \n
			:return: source: SPDif is fixed.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:AUDio:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.BcInputSignalSource)
