from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Generator:
	"""Generator commands group definition. 5 total commands, 0 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("generator", core, parent)

	def get_frequency(self) -> float:
		"""SCPI: TEST<HW>:GENerator:FREQuency \n
		Snippet: value: float = driver.test.generator.get_frequency() \n
		No command help available \n
			:return: sine_frequency: No help available
		"""
		response = self._core.io.query_str('TEST<HwInstance>:GENerator:FREQuency?')
		return Conversions.str_to_float(response)

	def set_frequency(self, sine_frequency: float) -> None:
		"""SCPI: TEST<HW>:GENerator:FREQuency \n
		Snippet: driver.test.generator.set_frequency(sine_frequency = 1.0) \n
		No command help available \n
			:param sine_frequency: No help available
		"""
		param = Conversions.decimal_value_to_str(sine_frequency)
		self._core.io.write(f'TEST<HwInstance>:GENerator:FREQuency {param}')

	def get_gain(self) -> float:
		"""SCPI: TEST<HW>:GENerator:GAIN \n
		Snippet: value: float = driver.test.generator.get_gain() \n
		No command help available \n
			:return: gain: No help available
		"""
		response = self._core.io.query_str('TEST<HwInstance>:GENerator:GAIN?')
		return Conversions.str_to_float(response)

	def set_gain(self, gain: float) -> None:
		"""SCPI: TEST<HW>:GENerator:GAIN \n
		Snippet: driver.test.generator.set_gain(gain = 1.0) \n
		No command help available \n
			:param gain: No help available
		"""
		param = Conversions.decimal_value_to_str(gain)
		self._core.io.write(f'TEST<HwInstance>:GENerator:GAIN {param}')

	def get_select(self) -> str:
		"""SCPI: TEST<HW>:GENerator:SELect \n
		Snippet: value: str = driver.test.generator.get_select() \n
		No command help available \n
			:return: wave_sel: No help available
		"""
		response = self._core.io.query_str('TEST<HwInstance>:GENerator:SELect?')
		return trim_str_response(response)

	def set_select(self, wave_sel: str) -> None:
		"""SCPI: TEST<HW>:GENerator:SELect \n
		Snippet: driver.test.generator.set_select(wave_sel = '1') \n
		No command help available \n
			:param wave_sel: No help available
		"""
		param = Conversions.value_to_quoted_str(wave_sel)
		self._core.io.write(f'TEST<HwInstance>:GENerator:SELect {param}')

	# noinspection PyTypeChecker
	def get_source(self) -> enums.TestGenIqSour:
		"""SCPI: TEST<HW>:GENerator:SOURce \n
		Snippet: value: enums.TestGenIqSour = driver.test.generator.get_source() \n
		No command help available \n
			:return: source: No help available
		"""
		response = self._core.io.query_str('TEST<HwInstance>:GENerator:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.TestGenIqSour)

	def set_source(self, source: enums.TestGenIqSour) -> None:
		"""SCPI: TEST<HW>:GENerator:SOURce \n
		Snippet: driver.test.generator.set_source(source = enums.TestGenIqSour.ARB) \n
		No command help available \n
			:param source: No help available
		"""
		param = Conversions.enum_scalar_to_str(source, enums.TestGenIqSour)
		self._core.io.write(f'TEST<HwInstance>:GENerator:SOURce {param}')

	def get_state(self) -> bool:
		"""SCPI: TEST<HW>:GENerator:STATe \n
		Snippet: value: bool = driver.test.generator.get_state() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('TEST<HwInstance>:GENerator:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: TEST<HW>:GENerator:STATe \n
		Snippet: driver.test.generator.set_state(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'TEST<HwInstance>:GENerator:STATe {param}')
