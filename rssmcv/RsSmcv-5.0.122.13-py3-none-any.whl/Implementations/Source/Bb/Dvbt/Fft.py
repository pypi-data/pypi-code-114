from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fft:
	"""Fft commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fft", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.DvbtCodingFftMode:
		"""SCPI: [SOURce<HW>]:BB:DVBT:FFT:MODE \n
		Snippet: value: enums.DvbtCodingFftMode = driver.source.bb.dvbt.fft.get_mode() \n
		Sets the fast fourier transform (FFT) window to determine the number of carriers per OFDM symbol. To find out the number
		of carriers for a given FFT window, see Table 'Number of carriers'. \n
			:return: fft_mode: M8K| M4K| M2K
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBT:FFT:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.DvbtCodingFftMode)

	def set_mode(self, fft_mode: enums.DvbtCodingFftMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBT:FFT:MODE \n
		Snippet: driver.source.bb.dvbt.fft.set_mode(fft_mode = enums.DvbtCodingFftMode.M2K) \n
		Sets the fast fourier transform (FFT) window to determine the number of carriers per OFDM symbol. To find out the number
		of carriers for a given FFT window, see Table 'Number of carriers'. \n
			:param fft_mode: M8K| M4K| M2K
		"""
		param = Conversions.enum_scalar_to_str(fft_mode, enums.DvbtCodingFftMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBT:FFT:MODE {param}')
