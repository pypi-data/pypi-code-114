from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BsSignal:
	"""BsSignal commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bsSignal", core, parent)

	def get_frequency(self) -> float:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:BSSignal:FREQuency \n
		Snippet: value: float = driver.source.bb.w3Gpp.ts25141.bsSignal.get_frequency() \n
		Sets the RF frequency of the base station. \n
			:return: frequency: float Range: 100 kHz to 6 GHz
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:BSSignal:FREQuency?')
		return Conversions.str_to_float(response)

	def set_frequency(self, frequency: float) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:BSSignal:FREQuency \n
		Snippet: driver.source.bb.w3Gpp.ts25141.bsSignal.set_frequency(frequency = 1.0) \n
		Sets the RF frequency of the base station. \n
			:param frequency: float Range: 100 kHz to 6 GHz
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:BSSignal:FREQuency {param}')

	def get_power(self) -> float:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:BSSignal:POWer \n
		Snippet: value: float = driver.source.bb.w3Gpp.ts25141.bsSignal.get_power() \n
		Sets the RF power of the base station. \n
			:return: power: float Range: -145 to 20
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:BSSignal:POWer?')
		return Conversions.str_to_float(response)

	def set_power(self, power: float) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:BSSignal:POWer \n
		Snippet: driver.source.bb.w3Gpp.ts25141.bsSignal.set_power(power = 1.0) \n
		Sets the RF power of the base station. \n
			:param power: float Range: -145 to 20
		"""
		param = Conversions.decimal_value_to_str(power)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:BSSignal:POWer {param}')
