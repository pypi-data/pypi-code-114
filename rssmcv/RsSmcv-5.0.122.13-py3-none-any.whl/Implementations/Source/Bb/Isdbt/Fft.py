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
	def get_mode(self) -> enums.CodingIsdbtMode:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:FFT:MODE \n
		Snippet: value: enums.CodingIsdbtMode = driver.source.bb.isdbt.fft.get_mode() \n
		Sets the ISDB-T mode. \n
			:return: isdbt_mode: M3_8K| M2_4K| M1_2K
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:FFT:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.CodingIsdbtMode)

	def set_mode(self, isdbt_mode: enums.CodingIsdbtMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:FFT:MODE \n
		Snippet: driver.source.bb.isdbt.fft.set_mode(isdbt_mode = enums.CodingIsdbtMode.M1_2K) \n
		Sets the ISDB-T mode. \n
			:param isdbt_mode: M3_8K| M2_4K| M1_2K
		"""
		param = Conversions.enum_scalar_to_str(isdbt_mode, enums.CodingIsdbtMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:FFT:MODE {param}')
