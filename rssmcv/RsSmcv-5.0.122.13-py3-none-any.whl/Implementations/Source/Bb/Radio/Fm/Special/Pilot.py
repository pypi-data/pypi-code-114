from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pilot:
	"""Pilot commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pilot", core, parent)

	def get_phase(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:[SPECial]:PILot:PHASe \n
		Snippet: value: float = driver.source.bb.radio.fm.special.pilot.get_phase() \n
		Sets the phase offset of the 19 kHz pilot tone. \n
			:return: offset_pilot: float Range: -180 to 180
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:SPECial:PILot:PHASe?')
		return Conversions.str_to_float(response)

	def set_phase(self, offset_pilot: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:[SPECial]:PILot:PHASe \n
		Snippet: driver.source.bb.radio.fm.special.pilot.set_phase(offset_pilot = 1.0) \n
		Sets the phase offset of the 19 kHz pilot tone. \n
			:param offset_pilot: float Range: -180 to 180
		"""
		param = Conversions.decimal_value_to_str(offset_pilot)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:SPECial:PILot:PHASe {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:[SPECial]:PILot:[STATe] \n
		Snippet: value: bool = driver.source.bb.radio.fm.special.pilot.get_state() \n
		Enables/disables the 19 kHz pilot tone. \n
			:return: pilot: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:SPECial:PILot:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, pilot: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:[SPECial]:PILot:[STATe] \n
		Snippet: driver.source.bb.radio.fm.special.pilot.set_state(pilot = False) \n
		Enables/disables the 19 kHz pilot tone. \n
			:param pilot: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(pilot)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:SPECial:PILot:STATe {param}')
