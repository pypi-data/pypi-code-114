from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fft:
	"""Fft commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fft", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.Atsc30FftSize:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:INFO:BOOTstrap:FFT:MODE \n
		Snippet: value: enums.Atsc30FftSize = driver.source.bb.a3Tsc.info.bootstrap.fft.get_mode() \n
		Queries the FFT size of the preamble symbols. \n
			:return: fft_mode: M8K| M16K| M32K
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:INFO:BOOTstrap:FFT:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.Atsc30FftSize)
