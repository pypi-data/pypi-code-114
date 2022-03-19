from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fm:
	"""Fm commands group definition. 5 total commands, 0 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fm", core, parent)

	def get_deviation(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GENeral:FM:DEViation \n
		Snippet: value: float = driver.source.bb.general.fm.get_deviation() \n
		Sets the frequency modulation deviation in Hz. \n
			:return: fm_deviation: float Range: 0 to 4E6
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GENeral:FM:DEViation?')
		return Conversions.str_to_float(response)

	def set_deviation(self, fm_deviation: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:GENeral:FM:DEViation \n
		Snippet: driver.source.bb.general.fm.set_deviation(fm_deviation = 1.0) \n
		Sets the frequency modulation deviation in Hz. \n
			:param fm_deviation: float Range: 0 to 4E6
		"""
		param = Conversions.decimal_value_to_str(fm_deviation)
		self._core.io.write(f'SOURce<HwInstance>:BB:GENeral:FM:DEViation {param}')

	def get_frequency(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GENeral:FM:FREQuency \n
		Snippet: value: float = driver.source.bb.general.fm.get_frequency() \n
		Sets the frequency of the modulation signal. \n
			:return: freq_mod_freq: float Range: 0.1 to 100E3
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GENeral:FM:FREQuency?')
		return Conversions.str_to_float(response)

	def set_frequency(self, freq_mod_freq: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:GENeral:FM:FREQuency \n
		Snippet: driver.source.bb.general.fm.set_frequency(freq_mod_freq = 1.0) \n
		Sets the frequency of the modulation signal. \n
			:param freq_mod_freq: float Range: 0.1 to 100E3
		"""
		param = Conversions.decimal_value_to_str(freq_mod_freq)
		self._core.io.write(f'SOURce<HwInstance>:BB:GENeral:FM:FREQuency {param}')

	def get_period(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GENeral:FM:PERiod \n
		Snippet: value: float = driver.source.bb.general.fm.get_period() \n
		Queries the period of the modulation signal. \n
			:return: fm_per: float Range: 100E-9 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GENeral:FM:PERiod?')
		return Conversions.str_to_float(response)

	def set_period(self, fm_per: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:GENeral:FM:PERiod \n
		Snippet: driver.source.bb.general.fm.set_period(fm_per = 1.0) \n
		Queries the period of the modulation signal. \n
			:param fm_per: float Range: 100E-9 to 100
		"""
		param = Conversions.decimal_value_to_str(fm_per)
		self._core.io.write(f'SOURce<HwInstance>:BB:GENeral:FM:PERiod {param}')

	# noinspection PyTypeChecker
	def get_shape(self) -> enums.BasebandModShape:
		"""SCPI: [SOURce<HW>]:BB:GENeral:FM:SHAPe \n
		Snippet: value: enums.BasebandModShape = driver.source.bb.general.fm.get_shape() \n
		Queries the shape of the modulation signal. \n
			:return: fm_shape: SINE
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GENeral:FM:SHAPe?')
		return Conversions.str_to_scalar_enum(response, enums.BasebandModShape)

	def set_shape(self, fm_shape: enums.BasebandModShape) -> None:
		"""SCPI: [SOURce<HW>]:BB:GENeral:FM:SHAPe \n
		Snippet: driver.source.bb.general.fm.set_shape(fm_shape = enums.BasebandModShape.SINE) \n
		Queries the shape of the modulation signal. \n
			:param fm_shape: SINE
		"""
		param = Conversions.enum_scalar_to_str(fm_shape, enums.BasebandModShape)
		self._core.io.write(f'SOURce<HwInstance>:BB:GENeral:FM:SHAPe {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GENeral:FM:[STATe] \n
		Snippet: value: bool = driver.source.bb.general.fm.get_state() \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:return: fm_mod_state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GENeral:FM:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, fm_mod_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GENeral:FM:[STATe] \n
		Snippet: driver.source.bb.general.fm.set_state(fm_mod_state = False) \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:param fm_mod_state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(fm_mod_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GENeral:FM:STATe {param}')
