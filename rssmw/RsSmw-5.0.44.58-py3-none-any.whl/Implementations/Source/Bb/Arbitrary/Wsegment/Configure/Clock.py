from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Clock:
	"""Clock commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("clock", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.ArbWaveSegmClocMode:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:WSEGment:CONFigure:CLOCk:MODE \n
		Snippet: value: enums.ArbWaveSegmClocMode = driver.source.bb.arbitrary.wsegment.configure.clock.get_mode() \n
		Selects the clock rate mode for the multi segment waveform.
		Use the command [:SOURce<hw>]:BB:ARBitrary:WSEGment:CONFigure:CLOCk to define the clock in clock mode user. \n
			:return: mode: UNCHanged| HIGHest| USER
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:WSEGment:CONFigure:CLOCk:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.ArbWaveSegmClocMode)

	def set_mode(self, mode: enums.ArbWaveSegmClocMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:WSEGment:CONFigure:CLOCk:MODE \n
		Snippet: driver.source.bb.arbitrary.wsegment.configure.clock.set_mode(mode = enums.ArbWaveSegmClocMode.HIGHest) \n
		Selects the clock rate mode for the multi segment waveform.
		Use the command [:SOURce<hw>]:BB:ARBitrary:WSEGment:CONFigure:CLOCk to define the clock in clock mode user. \n
			:param mode: UNCHanged| HIGHest| USER
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.ArbWaveSegmClocMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:WSEGment:CONFigure:CLOCk:MODE {param}')

	def get_value(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:WSEGment:CONFigure:CLOCk \n
		Snippet: value: float = driver.source.bb.arbitrary.wsegment.configure.clock.get_value() \n
		Defines the clock rate used for multi-segment waveform output if the clock mode is USER. \n
			:return: clock: float
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:WSEGment:CONFigure:CLOCk?')
		return Conversions.str_to_float(response)

	def set_value(self, clock: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:WSEGment:CONFigure:CLOCk \n
		Snippet: driver.source.bb.arbitrary.wsegment.configure.clock.set_value(clock = 1.0) \n
		Defines the clock rate used for multi-segment waveform output if the clock mode is USER. \n
			:param clock: float
		"""
		param = Conversions.decimal_value_to_str(clock)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:WSEGment:CONFigure:CLOCk {param}')
