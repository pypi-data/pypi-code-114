from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pilot:
	"""Pilot commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pilot", core, parent)

	def get_deviation(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:PILot:DEViation \n
		Snippet: value: float = driver.source.bb.radio.fm.pilot.get_deviation() \n
		Defines the resulting 19 kHz frequency deviation of the pilot tone irrespective of the audio signals. \n
			:return: freq_dev_pilot: float Range: 0 to 15, Unit: kHz
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:PILot:DEViation?')
		return Conversions.str_to_float(response)

	def set_deviation(self, freq_dev_pilot: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:PILot:DEViation \n
		Snippet: driver.source.bb.radio.fm.pilot.set_deviation(freq_dev_pilot = 1.0) \n
		Defines the resulting 19 kHz frequency deviation of the pilot tone irrespective of the audio signals. \n
			:param freq_dev_pilot: float Range: 0 to 15, Unit: kHz
		"""
		param = Conversions.decimal_value_to_str(freq_dev_pilot)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:PILot:DEViation {param}')
