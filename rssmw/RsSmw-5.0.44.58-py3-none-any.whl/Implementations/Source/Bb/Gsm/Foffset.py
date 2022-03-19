from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Foffset:
	"""Foffset commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("foffset", core, parent)

	def get_mean(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GSM:FOFFset:MEAN \n
		Snippet: value: float = driver.source.bb.gsm.foffset.get_mean() \n
		Sets the frequency offset parameter μ. \n
			:return: mean_freq_offset: float Range: 0 to 9999.9
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GSM:FOFFset:MEAN?')
		return Conversions.str_to_float(response)

	def set_mean(self, mean_freq_offset: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:GSM:FOFFset:MEAN \n
		Snippet: driver.source.bb.gsm.foffset.set_mean(mean_freq_offset = 1.0) \n
		Sets the frequency offset parameter μ. \n
			:param mean_freq_offset: float Range: 0 to 9999.9
		"""
		param = Conversions.decimal_value_to_str(mean_freq_offset)
		self._core.io.write(f'SOURce<HwInstance>:BB:GSM:FOFFset:MEAN {param}')

	def get_standard(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GSM:FOFFset:STANdard \n
		Snippet: value: float = driver.source.bb.gsm.foffset.get_standard() \n
		Sets the frequency offset parameter σ. \n
			:return: standard_freq_off: float Range: 0 to 9999.9
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GSM:FOFFset:STANdard?')
		return Conversions.str_to_float(response)

	def set_standard(self, standard_freq_off: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:GSM:FOFFset:STANdard \n
		Snippet: driver.source.bb.gsm.foffset.set_standard(standard_freq_off = 1.0) \n
		Sets the frequency offset parameter σ. \n
			:param standard_freq_off: float Range: 0 to 9999.9
		"""
		param = Conversions.decimal_value_to_str(standard_freq_off)
		self._core.io.write(f'SOURce<HwInstance>:BB:GSM:FOFFset:STANdard {param}')
