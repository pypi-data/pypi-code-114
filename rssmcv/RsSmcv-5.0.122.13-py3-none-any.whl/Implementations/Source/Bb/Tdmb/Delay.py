from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Delay:
	"""Delay commands group definition. 7 total commands, 0 Subgroups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("delay", core, parent)

	def get_compensation(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:TDMB:DELay:COMPensation \n
		Snippet: value: float = driver.source.bb.tdmb.delay.get_compensation() \n
		Displays the time span by which signal processing is artificially delayed in order to achieve a constant 'TX Delay'. \n
			:return: delay_comp: float Range: -1.0000000 to 1.0000000, Unit: s
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TDMB:DELay:COMPensation?')
		return Conversions.str_to_float(response)

	def get_delay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:TDMB:DELay:DELay \n
		Snippet: value: float = driver.source.bb.tdmb.delay.get_delay() \n
		Sets the signal turnaround time through the transmitter. \n
			:return: delay_tx: float Range: 0.0000000 to 1.0000000, Unit: s
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TDMB:DELay:DELay?')
		return Conversions.str_to_float(response)

	def set_delay(self, delay_tx: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDMB:DELay:DELay \n
		Snippet: driver.source.bb.tdmb.delay.set_delay(delay_tx = 1.0) \n
		Sets the signal turnaround time through the transmitter. \n
			:param delay_tx: float Range: 0.0000000 to 1.0000000, Unit: s
		"""
		param = Conversions.decimal_value_to_str(delay_tx)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDMB:DELay:DELay {param}')

	def get_deviation(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:TDMB:DELay:DEViation \n
		Snippet: value: int = driver.source.bb.tdmb.delay.get_deviation() \n
		Sets the maximum permitted deviation of the transmission time relative to the internally regulated reference frequency. \n
			:return: delay_dev: integer Range: 0.000001 to 0.0005000, Unit: s
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TDMB:DELay:DEViation?')
		return Conversions.str_to_int(response)

	def set_deviation(self, delay_dev: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDMB:DELay:DEViation \n
		Snippet: driver.source.bb.tdmb.delay.set_deviation(delay_dev = 1) \n
		Sets the maximum permitted deviation of the transmission time relative to the internally regulated reference frequency. \n
			:param delay_dev: integer Range: 0.000001 to 0.0005000, Unit: s
		"""
		param = Conversions.decimal_value_to_str(delay_dev)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDMB:DELay:DEViation {param}')

	def get_network(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:TDMB:DELay:NETWork \n
		Snippet: value: float = driver.source.bb.tdmb.delay.get_network() \n
		Queries the compensating delay. If the delay is added to the network path delay, the overall delay is constant and of
		known value. \n
			:return: network_delay: float Range: 0.0000000 to 1.0000000
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TDMB:DELay:NETWork?')
		return Conversions.str_to_float(response)

	def get_process(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:TDMB:DELay:PROCess \n
		Snippet: value: float = driver.source.bb.tdmb.delay.get_process() \n
		Queries the minimum signal turnaround time through the transmitter. \n
			:return: delay_proc: float Range: 0.0000000 to 1.0000000
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TDMB:DELay:PROCess?')
		return Conversions.str_to_float(response)

	def get_static(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:TDMB:DELay:STATic \n
		Snippet: value: float = driver.source.bb.tdmb.delay.get_static() \n
		Sets the delay in order to shift the time of transmission positively or negatively. \n
			:return: delay_static: float Range: -1.0000000 to 1.0000000, Unit: s
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TDMB:DELay:STATic?')
		return Conversions.str_to_float(response)

	def set_static(self, delay_static: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDMB:DELay:STATic \n
		Snippet: driver.source.bb.tdmb.delay.set_static(delay_static = 1.0) \n
		Sets the delay in order to shift the time of transmission positively or negatively. \n
			:param delay_static: float Range: -1.0000000 to 1.0000000, Unit: s
		"""
		param = Conversions.decimal_value_to_str(delay_static)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDMB:DELay:STATic {param}')

	def get_total(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:TDMB:DELay:TOTal \n
		Snippet: value: float = driver.source.bb.tdmb.delay.get_total() \n
		Queries the total cycle time of the signal through the transmitter. \n
			:return: delay_total: float Range: -1.0000000 to 3.0000000, Unit: s
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TDMB:DELay:TOTal?')
		return Conversions.str_to_float(response)
