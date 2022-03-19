from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	def get_cfactor(self) -> float:
		"""SCPI: [SOURce<HW>]:BBIN:POWer:CFACtor \n
		Snippet: value: float = driver.source.bbin.power.get_cfactor() \n
		Sets the crest factor of the external baseband signal. \n
			:return: cfactor: float Range: 0 to 30, Unit: dB
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BBIN:POWer:CFACtor?')
		return Conversions.str_to_float(response)

	def set_cfactor(self, cfactor: float) -> None:
		"""SCPI: [SOURce<HW>]:BBIN:POWer:CFACtor \n
		Snippet: driver.source.bbin.power.set_cfactor(cfactor = 1.0) \n
		Sets the crest factor of the external baseband signal. \n
			:param cfactor: float Range: 0 to 30, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(cfactor)
		self._core.io.write(f'SOURce<HwInstance>:BBIN:POWer:CFACtor {param}')

	def get_peak(self) -> float:
		"""SCPI: [SOURce<HW>]:BBIN:POWer:PEAK \n
		Snippet: value: float = driver.source.bbin.power.get_peak() \n
		Peak level of the external baseband signal relative to full scale of 0.5 V (in terms of dB full scale) . \n
			:return: peak: float Range: -60 to 3.02, Unit: dBfs
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BBIN:POWer:PEAK?')
		return Conversions.str_to_float(response)

	def set_peak(self, peak: float) -> None:
		"""SCPI: [SOURce<HW>]:BBIN:POWer:PEAK \n
		Snippet: driver.source.bbin.power.set_peak(peak = 1.0) \n
		Peak level of the external baseband signal relative to full scale of 0.5 V (in terms of dB full scale) . \n
			:param peak: float Range: -60 to 3.02, Unit: dBfs
		"""
		param = Conversions.decimal_value_to_str(peak)
		self._core.io.write(f'SOURce<HwInstance>:BBIN:POWer:PEAK {param}')

	def get_rms(self) -> float:
		"""SCPI: [SOURce<HW>]:BBIN:POWer:RMS \n
		Snippet: value: float = driver.source.bbin.power.get_rms() \n
		Queries the RMS level of the external digital baseband signal. \n
			:return: rms: float Range: -100 to 10
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BBIN:POWer:RMS?')
		return Conversions.str_to_float(response)
