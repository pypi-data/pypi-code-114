from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pilot:
	"""Pilot commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pilot", core, parent)

	def get_phase(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:STEReo:PILot:PHASe \n
		Snippet: value: float = driver.source.bb.stereo.pilot.get_phase() \n
		No command help available \n
			:return: phase: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:STEReo:PILot:PHASe?')
		return Conversions.str_to_float(response)

	def set_phase(self, phase: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:STEReo:PILot:PHASe \n
		Snippet: driver.source.bb.stereo.pilot.set_phase(phase = 1.0) \n
		No command help available \n
			:param phase: No help available
		"""
		param = Conversions.decimal_value_to_str(phase)
		self._core.io.write(f'SOURce<HwInstance>:BB:STEReo:PILot:PHASe {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:STEReo:PILot:STATe \n
		Snippet: value: bool = driver.source.bb.stereo.pilot.get_state() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:STEReo:PILot:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:STEReo:PILot:STATe \n
		Snippet: driver.source.bb.stereo.pilot.set_state(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:STEReo:PILot:STATe {param}')

	def get_deviation(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:STEReo:PILot:[DEViation] \n
		Snippet: value: int = driver.source.bb.stereo.pilot.get_deviation() \n
		No command help available \n
			:return: deviation: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:STEReo:PILot:DEViation?')
		return Conversions.str_to_int(response)

	def set_deviation(self, deviation: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:STEReo:PILot:[DEViation] \n
		Snippet: driver.source.bb.stereo.pilot.set_deviation(deviation = 1) \n
		No command help available \n
			:param deviation: No help available
		"""
		param = Conversions.decimal_value_to_str(deviation)
		self._core.io.write(f'SOURce<HwInstance>:BB:STEReo:PILot:DEViation {param}')
