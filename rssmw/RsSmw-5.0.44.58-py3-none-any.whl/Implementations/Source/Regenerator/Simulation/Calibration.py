from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Calibration:
	"""Calibration commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("calibration", core, parent)

	def get_correction(self) -> float:
		"""SCPI: [SOURce<HW>]:REGenerator:SIMulation:CALibration:CORRection \n
		Snippet: value: float = driver.source.regenerator.simulation.calibration.get_correction() \n
		Adds a correction to the automatically estimated system latency value. \n
			:return: corr_value: float Range: -100 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:REGenerator:SIMulation:CALibration:CORRection?')
		return Conversions.str_to_float(response)

	def set_correction(self, corr_value: float) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:SIMulation:CALibration:CORRection \n
		Snippet: driver.source.regenerator.simulation.calibration.set_correction(corr_value = 1.0) \n
		Adds a correction to the automatically estimated system latency value. \n
			:param corr_value: float Range: -100 to 100
		"""
		param = Conversions.decimal_value_to_str(corr_value)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:SIMulation:CALibration:CORRection {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.RegSimCalibrationMode:
		"""SCPI: [SOURce<HW>]:REGenerator:SIMulation:CALibration:MODE \n
		Snippet: value: enums.RegSimCalibrationMode = driver.source.regenerator.simulation.calibration.get_mode() \n
		Sets how the system latency is estimated. \n
			:return: cal_mode: MANual| AUTomatic AUTomatic mode can be used only if a R&S FSW is connected to the R&S SMW.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:REGenerator:SIMulation:CALibration:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.RegSimCalibrationMode)

	def set_mode(self, cal_mode: enums.RegSimCalibrationMode) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:SIMulation:CALibration:MODE \n
		Snippet: driver.source.regenerator.simulation.calibration.set_mode(cal_mode = enums.RegSimCalibrationMode.AUTomatic) \n
		Sets how the system latency is estimated. \n
			:param cal_mode: MANual| AUTomatic AUTomatic mode can be used only if a R&S FSW is connected to the R&S SMW.
		"""
		param = Conversions.enum_scalar_to_str(cal_mode, enums.RegSimCalibrationMode)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:SIMulation:CALibration:MODE {param}')

	def get_urange(self) -> bool:
		"""SCPI: [SOURce<HW>]:REGenerator:SIMulation:CALibration:URANge \n
		Snippet: value: bool = driver.source.regenerator.simulation.calibration.get_urange() \n
		Allows you to simulate objects at a range closer than 2.1 km. \n
			:return: use_under_range: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:REGenerator:SIMulation:CALibration:URANge?')
		return Conversions.str_to_bool(response)

	def set_urange(self, use_under_range: bool) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:SIMulation:CALibration:URANge \n
		Snippet: driver.source.regenerator.simulation.calibration.set_urange(use_under_range = False) \n
		Allows you to simulate objects at a range closer than 2.1 km. \n
			:param use_under_range: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(use_under_range)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:SIMulation:CALibration:URANge {param}')

	# noinspection PyTypeChecker
	def get_state(self) -> enums.RegSimCalibrationState:
		"""SCPI: [SOURce<HW>]:REGenerator:SIMulation:CALibration:[STATe] \n
		Snippet: value: enums.RegSimCalibrationState = driver.source.regenerator.simulation.calibration.get_state() \n
		Queries the status of the automatic system calibration process. \n
			:return: calibration_stat: FAILed| SUCCess
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:REGenerator:SIMulation:CALibration:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.RegSimCalibrationState)
