from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	def get_peak(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:POWer:PEAK \n
		Snippet: value: float = driver.source.bb.power.get_peak() \n
		Queries the peak level of the baseband signal relative to full scale of 0.5 V (in terms of dB full scale) . \n
			:return: peak: float Range: -145 to 30, Unit: dBfs
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:POWer:PEAK?')
		return Conversions.str_to_float(response)

	def get_rms(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:POWer:RMS \n
		Snippet: value: float = driver.source.bb.power.get_rms() \n
		Queries the RMS level of the baseband signal relative to full scale of 0.5V (in terms of dB full scale) . \n
			:return: rms: float Range: -145 to 30, Unit: dBfs
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:POWer:RMS?')
		return Conversions.str_to_float(response)
