from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Center:
	"""Center commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("center", core, parent)

	def get_offset(self) -> float:
		"""SCPI: [SOURce<HW>]:AWGN:FREQuency:CENTer:OFFSet \n
		Snippet: value: float = driver.source.awgn.frequency.center.get_offset() \n
		Defines the frequency offset of the noise signal relative to the carrier center frequency. \n
			:return: center_freq_offset: float Range: -40E6 to 40E6
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AWGN:FREQuency:CENTer:OFFSet?')
		return Conversions.str_to_float(response)

	def set_offset(self, center_freq_offset: float) -> None:
		"""SCPI: [SOURce<HW>]:AWGN:FREQuency:CENTer:OFFSet \n
		Snippet: driver.source.awgn.frequency.center.set_offset(center_freq_offset = 1.0) \n
		Defines the frequency offset of the noise signal relative to the carrier center frequency. \n
			:param center_freq_offset: float Range: -40E6 to 40E6
		"""
		param = Conversions.decimal_value_to_str(center_freq_offset)
		self._core.io.write(f'SOURce<HwInstance>:AWGN:FREQuency:CENTer:OFFSet {param}')
