from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AudGen:
	"""AudGen commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("audGen", core, parent)

	def get_frq_1(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:AUDGen:FRQ1 \n
		Snippet: value: int = driver.source.bb.radio.fm.audGen.get_frq_1() \n
		Sets the frequency. \n
			:return: freq_left: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:AUDGen:FRQ1?')
		return Conversions.str_to_int(response)

	def set_frq_1(self, freq_left: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:AUDGen:FRQ1 \n
		Snippet: driver.source.bb.radio.fm.audGen.set_frq_1(freq_left = 1) \n
		Sets the frequency. \n
			:param freq_left: integer Range: 30 to 15000, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(freq_left)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:AUDGen:FRQ1 {param}')

	def get_frq_2(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:AUDGen:FRQ2 \n
		Snippet: value: int = driver.source.bb.radio.fm.audGen.get_frq_2() \n
		Sets the frequency. \n
			:return: freq_right: integer Range: 30 to 15000, Unit: Hz
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:AUDGen:FRQ2?')
		return Conversions.str_to_int(response)

	def set_frq_2(self, freq_right: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:AUDGen:FRQ2 \n
		Snippet: driver.source.bb.radio.fm.audGen.set_frq_2(freq_right = 1) \n
		Sets the frequency. \n
			:param freq_right: integer Range: 30 to 15000, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(freq_right)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:AUDGen:FRQ2 {param}')

	def get_lev_1(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:AUDGen:LEV1 \n
		Snippet: value: float = driver.source.bb.radio.fm.audGen.get_lev_1() \n
		Sets the level. \n
			:return: level_left: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:AUDGen:LEV1?')
		return Conversions.str_to_float(response)

	def set_lev_1(self, level_left: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:AUDGen:LEV1 \n
		Snippet: driver.source.bb.radio.fm.audGen.set_lev_1(level_left = 1.0) \n
		Sets the level. \n
			:param level_left: float Range: -60 to 12, Unit: dBu
		"""
		param = Conversions.decimal_value_to_str(level_left)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:AUDGen:LEV1 {param}')

	def get_lev_2(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:AUDGen:LEV2 \n
		Snippet: value: float = driver.source.bb.radio.fm.audGen.get_lev_2() \n
		Sets the level. \n
			:return: level_right: float Range: -60 to 12, Unit: dBu
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:AUDGen:LEV2?')
		return Conversions.str_to_float(response)

	def set_lev_2(self, level_right: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:AUDGen:LEV2 \n
		Snippet: driver.source.bb.radio.fm.audGen.set_lev_2(level_right = 1.0) \n
		Sets the level. \n
			:param level_right: float Range: -60 to 12, Unit: dBu
		"""
		param = Conversions.decimal_value_to_str(level_right)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:AUDGen:LEV2 {param}')
