from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Audio:
	"""Audio commands group definition. 7 total commands, 0 Subgroups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("audio", core, parent)

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:STEReo:AUDio:CATalog \n
		Snippet: value: List[str] = driver.source.bb.stereo.audio.get_catalog() \n
		No command help available \n
			:return: catalog: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:STEReo:AUDio:CATalog?')
		return Conversions.str_to_str_list(response)

	def set_dselect(self, dselect: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:STEReo:AUDio:DSELect \n
		Snippet: driver.source.bb.stereo.audio.set_dselect(dselect = '1') \n
		No command help available \n
			:param dselect: No help available
		"""
		param = Conversions.value_to_quoted_str(dselect)
		self._core.io.write(f'SOURce<HwInstance>:BB:STEReo:AUDio:DSELect {param}')

	# noinspection PyTypeChecker
	def get_ext_clock(self) -> enums.FmStereoAudExtClk:
		"""SCPI: [SOURce<HW>]:BB:STEReo:AUDio:EXTClock \n
		Snippet: value: enums.FmStereoAudExtClk = driver.source.bb.stereo.audio.get_ext_clock() \n
		No command help available \n
			:return: ext_clock: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:STEReo:AUDio:EXTClock?')
		return Conversions.str_to_scalar_enum(response, enums.FmStereoAudExtClk)

	def set_ext_clock(self, ext_clock: enums.FmStereoAudExtClk) -> None:
		"""SCPI: [SOURce<HW>]:BB:STEReo:AUDio:EXTClock \n
		Snippet: driver.source.bb.stereo.audio.set_ext_clock(ext_clock = enums.FmStereoAudExtClk._44100) \n
		No command help available \n
			:param ext_clock: No help available
		"""
		param = Conversions.enum_scalar_to_str(ext_clock, enums.FmStereoAudExtClk)
		self._core.io.write(f'SOURce<HwInstance>:BB:STEReo:AUDio:EXTClock {param}')

	def get_level(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:STEReo:AUDio:LEVel \n
		Snippet: value: float = driver.source.bb.stereo.audio.get_level() \n
		No command help available \n
			:return: level: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:STEReo:AUDio:LEVel?')
		return Conversions.str_to_float(response)

	def set_level(self, level: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:STEReo:AUDio:LEVel \n
		Snippet: driver.source.bb.stereo.audio.set_level(level = 1.0) \n
		No command help available \n
			:param level: No help available
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'SOURce<HwInstance>:BB:STEReo:AUDio:LEVel {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.FmStereoMode:
		"""SCPI: [SOURce<HW>]:BB:STEReo:AUDio:MODE \n
		Snippet: value: enums.FmStereoMode = driver.source.bb.stereo.audio.get_mode() \n
		No command help available \n
			:return: mode: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:STEReo:AUDio:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.FmStereoMode)

	def set_mode(self, mode: enums.FmStereoMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:STEReo:AUDio:MODE \n
		Snippet: driver.source.bb.stereo.audio.set_mode(mode = enums.FmStereoMode.LEFT) \n
		No command help available \n
			:param mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.FmStereoMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:STEReo:AUDio:MODE {param}')

	# noinspection PyTypeChecker
	def get_preemphasis(self) -> enums.FmStereoPreEmph:
		"""SCPI: [SOURce<HW>]:BB:STEReo:AUDio:PREemphasis \n
		Snippet: value: enums.FmStereoPreEmph = driver.source.bb.stereo.audio.get_preemphasis() \n
		No command help available \n
			:return: preemphasis: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:STEReo:AUDio:PREemphasis?')
		return Conversions.str_to_scalar_enum(response, enums.FmStereoPreEmph)

	def set_preemphasis(self, preemphasis: enums.FmStereoPreEmph) -> None:
		"""SCPI: [SOURce<HW>]:BB:STEReo:AUDio:PREemphasis \n
		Snippet: driver.source.bb.stereo.audio.set_preemphasis(preemphasis = enums.FmStereoPreEmph._50) \n
		No command help available \n
			:param preemphasis: No help available
		"""
		param = Conversions.enum_scalar_to_str(preemphasis, enums.FmStereoPreEmph)
		self._core.io.write(f'SOURce<HwInstance>:BB:STEReo:AUDio:PREemphasis {param}')

	def get_frequency(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:STEReo:AUDio:[FREQuency] \n
		Snippet: value: float = driver.source.bb.stereo.audio.get_frequency() \n
		No command help available \n
			:return: frequency: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:STEReo:AUDio:FREQuency?')
		return Conversions.str_to_float(response)

	def set_frequency(self, frequency: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:STEReo:AUDio:[FREQuency] \n
		Snippet: driver.source.bb.stereo.audio.set_frequency(frequency = 1.0) \n
		No command help available \n
			:param frequency: No help available
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'SOURce<HwInstance>:BB:STEReo:AUDio:FREQuency {param}')
