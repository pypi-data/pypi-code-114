from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bbfs:
	"""Bbfs commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bbfs", core, parent)

	def get_dtime(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:BBFS:DTIMe \n
		Snippet: value: float = driver.source.bb.eutra.bbfs.get_dtime() \n
		Sets the dwell time for each frequency step of the sweep. \n
			:return: dwell_time: float Range: 0.0001 to 0.005, Unit: s
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:BBFS:DTIMe?')
		return Conversions.str_to_float(response)

	def set_dtime(self, dwell_time: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:BBFS:DTIMe \n
		Snippet: driver.source.bb.eutra.bbfs.set_dtime(dwell_time = 1.0) \n
		Sets the dwell time for each frequency step of the sweep. \n
			:param dwell_time: float Range: 0.0001 to 0.005, Unit: s
		"""
		param = Conversions.decimal_value_to_str(dwell_time)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:BBFS:DTIMe {param}')

	def get_max_shift(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:BBFS:MAXShift \n
		Snippet: value: float = driver.source.bb.eutra.bbfs.get_max_shift() \n
		Sets the maximal total frequency sweep (summary for all steps) . \n
			:return: max_shift: float Range: 10 to 100, Unit: Hz
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:BBFS:MAXShift?')
		return Conversions.str_to_float(response)

	def set_max_shift(self, max_shift: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:BBFS:MAXShift \n
		Snippet: driver.source.bb.eutra.bbfs.set_max_shift(max_shift = 1.0) \n
		Sets the maximal total frequency sweep (summary for all steps) . \n
			:param max_shift: float Range: 10 to 100, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(max_shift)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:BBFS:MAXShift {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.EutraBbFreqSweepMode:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:BBFS:MODE \n
		Snippet: value: enums.EutraBbFreqSweepMode = driver.source.bb.eutra.bbfs.get_mode() \n
		Disables or enables the frequency sweep. The frequency sweep can be enbled before or after filtering. \n
			:return: mode: OFF| BEFore| AFTer
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:BBFS:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.EutraBbFreqSweepMode)

	def set_mode(self, mode: enums.EutraBbFreqSweepMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:BBFS:MODE \n
		Snippet: driver.source.bb.eutra.bbfs.set_mode(mode = enums.EutraBbFreqSweepMode.AFTer) \n
		Disables or enables the frequency sweep. The frequency sweep can be enbled before or after filtering. \n
			:param mode: OFF| BEFore| AFTer
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.EutraBbFreqSweepMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:BBFS:MODE {param}')

	def get_steps(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:BBFS:STEPs \n
		Snippet: value: int = driver.source.bb.eutra.bbfs.get_steps() \n
		Sets the number of iteration for increasing the frequency using the step of 0.1171875 Hz (90/768 ms) . \n
			:return: num_steps: integer Range: 10 to 1000
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:BBFS:STEPs?')
		return Conversions.str_to_int(response)

	def set_steps(self, num_steps: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:BBFS:STEPs \n
		Snippet: driver.source.bb.eutra.bbfs.set_steps(num_steps = 1) \n
		Sets the number of iteration for increasing the frequency using the step of 0.1171875 Hz (90/768 ms) . \n
			:param num_steps: integer Range: 10 to 1000
		"""
		param = Conversions.decimal_value_to_str(num_steps)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:BBFS:STEPs {param}')
