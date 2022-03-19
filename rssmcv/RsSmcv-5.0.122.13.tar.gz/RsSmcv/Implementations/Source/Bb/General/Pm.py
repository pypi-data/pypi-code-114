from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pm:
	"""Pm commands group definition. 5 total commands, 0 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pm", core, parent)

	def get_deviation(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GENeral:PM:DEViation \n
		Snippet: value: float = driver.source.bb.general.pm.get_deviation() \n
		Sets the phase modulation deviation in radians or degrees. \n
			:return: pm_deviation: float Range: 0 to 6, Unit: rad
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GENeral:PM:DEViation?')
		return Conversions.str_to_float(response)

	def set_deviation(self, pm_deviation: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:GENeral:PM:DEViation \n
		Snippet: driver.source.bb.general.pm.set_deviation(pm_deviation = 1.0) \n
		Sets the phase modulation deviation in radians or degrees. \n
			:param pm_deviation: float Range: 0 to 6, Unit: rad
		"""
		param = Conversions.decimal_value_to_str(pm_deviation)
		self._core.io.write(f'SOURce<HwInstance>:BB:GENeral:PM:DEViation {param}')

	def get_frequency(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GENeral:PM:FREQuency \n
		Snippet: value: float = driver.source.bb.general.pm.get_frequency() \n
		Sets the frequency of the modulation signal. \n
			:return: phase_freq: float Range: 0.1 to 100E3
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GENeral:PM:FREQuency?')
		return Conversions.str_to_float(response)

	def set_frequency(self, phase_freq: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:GENeral:PM:FREQuency \n
		Snippet: driver.source.bb.general.pm.set_frequency(phase_freq = 1.0) \n
		Sets the frequency of the modulation signal. \n
			:param phase_freq: float Range: 0.1 to 100E3
		"""
		param = Conversions.decimal_value_to_str(phase_freq)
		self._core.io.write(f'SOURce<HwInstance>:BB:GENeral:PM:FREQuency {param}')

	def get_period(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GENeral:PM:PERiod \n
		Snippet: value: float = driver.source.bb.general.pm.get_period() \n
		Queries the period of the modulation signal. \n
			:return: phase_per: float Range: 100E-9 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GENeral:PM:PERiod?')
		return Conversions.str_to_float(response)

	def set_period(self, phase_per: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:GENeral:PM:PERiod \n
		Snippet: driver.source.bb.general.pm.set_period(phase_per = 1.0) \n
		Queries the period of the modulation signal. \n
			:param phase_per: float Range: 100E-9 to 100
		"""
		param = Conversions.decimal_value_to_str(phase_per)
		self._core.io.write(f'SOURce<HwInstance>:BB:GENeral:PM:PERiod {param}')

	# noinspection PyTypeChecker
	def get_shape(self) -> enums.BasebandModShape:
		"""SCPI: [SOURce<HW>]:BB:GENeral:PM:SHAPe \n
		Snippet: value: enums.BasebandModShape = driver.source.bb.general.pm.get_shape() \n
		Queries the shape of the modulation signal. \n
			:return: pm_shape: SINE
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GENeral:PM:SHAPe?')
		return Conversions.str_to_scalar_enum(response, enums.BasebandModShape)

	def set_shape(self, pm_shape: enums.BasebandModShape) -> None:
		"""SCPI: [SOURce<HW>]:BB:GENeral:PM:SHAPe \n
		Snippet: driver.source.bb.general.pm.set_shape(pm_shape = enums.BasebandModShape.SINE) \n
		Queries the shape of the modulation signal. \n
			:param pm_shape: SINE
		"""
		param = Conversions.enum_scalar_to_str(pm_shape, enums.BasebandModShape)
		self._core.io.write(f'SOURce<HwInstance>:BB:GENeral:PM:SHAPe {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GENeral:PM:[STATe] \n
		Snippet: value: bool = driver.source.bb.general.pm.get_state() \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:return: phim_mod_state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GENeral:PM:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, phim_mod_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GENeral:PM:[STATe] \n
		Snippet: driver.source.bb.general.pm.set_state(phim_mod_state = False) \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:param phim_mod_state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(phim_mod_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GENeral:PM:STATe {param}')
