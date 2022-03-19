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
	def get_mode(self) -> enums.Dvbt2FramingFftSize:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:FFT:MODE \n
		Snippet: value: enums.Dvbt2FramingFftSize = driver.source.bb.t2Dvb.fft.get_mode() \n
		Defines the size. \n
			:return: fft_size: M1K| M2K| M4K| M8K| M8E| M16K| M16E| M32K| M32E M1K|M2K|M4K|M8K|M16K|M32K 1K/2K/4K/8K/16K/32K FFT size using normal carrier mode M8E|M16E|M32E 8K/16K/32K FFT size using extended carrier mode
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:FFT:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.Dvbt2FramingFftSize)

	def set_mode(self, fft_size: enums.Dvbt2FramingFftSize) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:FFT:MODE \n
		Snippet: driver.source.bb.t2Dvb.fft.set_mode(fft_size = enums.Dvbt2FramingFftSize.M16E) \n
		Defines the size. \n
			:param fft_size: M1K| M2K| M4K| M8K| M8E| M16K| M16E| M32K| M32E M1K|M2K|M4K|M8K|M16K|M32K 1K/2K/4K/8K/16K/32K FFT size using normal carrier mode M8E|M16E|M32E 8K/16K/32K FFT size using extended carrier mode
		"""
		param = Conversions.enum_scalar_to_str(fft_size, enums.Dvbt2FramingFftSize)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:FFT:MODE {param}')
