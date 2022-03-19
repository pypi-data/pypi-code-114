from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ota:
	"""Ota commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ota", core, parent)

	def get_offset(self) -> float:
		"""SCPI: [SOURce<HW>]:REGenerator:RADar:OTA:OFFSet \n
		Snippet: value: float = driver.source.regenerator.radar.ota.get_offset() \n
		Sets the OTA (over-the-air) distance. \n
			:return: ota_offset: float Range: 0.01 to 50E3
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:REGenerator:RADar:OTA:OFFSet?')
		return Conversions.str_to_float(response)

	def set_offset(self, ota_offset: float) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:RADar:OTA:OFFSet \n
		Snippet: driver.source.regenerator.radar.ota.set_offset(ota_offset = 1.0) \n
		Sets the OTA (over-the-air) distance. \n
			:param ota_offset: float Range: 0.01 to 50E3
		"""
		param = Conversions.decimal_value_to_str(ota_offset)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:RADar:OTA:OFFSet {param}')
