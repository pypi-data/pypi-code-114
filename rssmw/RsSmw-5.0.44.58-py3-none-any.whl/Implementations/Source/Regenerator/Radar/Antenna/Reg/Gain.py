from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gain:
	"""Gain commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gain", core, parent)

	def get_rx(self) -> float:
		"""SCPI: [SOURce<HW>]:REGenerator:RADar:ANTenna:REG:GAIN:RX \n
		Snippet: value: float = driver.source.regenerator.radar.antenna.reg.gain.get_rx() \n
		Sets the antenna gain. \n
			:return: gain_rx: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:REGenerator:RADar:ANTenna:REG:GAIN:RX?')
		return Conversions.str_to_float(response)

	def set_rx(self, gain_rx: float) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:RADar:ANTenna:REG:GAIN:RX \n
		Snippet: driver.source.regenerator.radar.antenna.reg.gain.set_rx(gain_rx = 1.0) \n
		Sets the antenna gain. \n
			:param gain_rx: float Range: 0 to 100
		"""
		param = Conversions.decimal_value_to_str(gain_rx)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:RADar:ANTenna:REG:GAIN:RX {param}')

	def get_tx(self) -> float:
		"""SCPI: [SOURce<HW>]:REGenerator:RADar:ANTenna:REG:GAIN:TX \n
		Snippet: value: float = driver.source.regenerator.radar.antenna.reg.gain.get_tx() \n
		Sets the antenna gain. \n
			:return: gain_tx: float Range: 0 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:REGenerator:RADar:ANTenna:REG:GAIN:TX?')
		return Conversions.str_to_float(response)

	def set_tx(self, gain_tx: float) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:RADar:ANTenna:REG:GAIN:TX \n
		Snippet: driver.source.regenerator.radar.antenna.reg.gain.set_tx(gain_tx = 1.0) \n
		Sets the antenna gain. \n
			:param gain_tx: float Range: 0 to 100
		"""
		param = Conversions.decimal_value_to_str(gain_tx)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:RADar:ANTenna:REG:GAIN:TX {param}')
