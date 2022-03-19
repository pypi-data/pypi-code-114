from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Source:
	"""Source commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("source", core, parent)

	# noinspection PyTypeChecker
	def get_low(self) -> enums.CodingInputSignalSource:
		"""SCPI: [SOURce<HW>]:BB:DVBT:SOURce:LOW \n
		Snippet: value: enums.CodingInputSignalSource = driver.source.bb.dvbt.source.get_low() \n
		Sets the modulation source for the input signal. \n
			:return: source_lp: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBT:SOURce:LOW?')
		return Conversions.str_to_scalar_enum(response, enums.CodingInputSignalSource)

	def set_low(self, source_lp: enums.CodingInputSignalSource) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBT:SOURce:LOW \n
		Snippet: driver.source.bb.dvbt.source.set_low(source_lp = enums.CodingInputSignalSource.EXTernal) \n
		Sets the modulation source for the input signal. \n
			:param source_lp: TSPLayer| EXTernal| TESTsignal
		"""
		param = Conversions.enum_scalar_to_str(source_lp, enums.CodingInputSignalSource)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBT:SOURce:LOW {param}')

	# noinspection PyTypeChecker
	def get_high(self) -> enums.CodingInputSignalSource:
		"""SCPI: [SOURce<HW>]:BB:DVBT:SOURce:[HIGH] \n
		Snippet: value: enums.CodingInputSignalSource = driver.source.bb.dvbt.source.get_high() \n
		Sets the modulation source for the input signal. \n
			:return: signal_source_hp: TSPLayer| EXTernal| TESTsignal
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBT:SOURce:HIGH?')
		return Conversions.str_to_scalar_enum(response, enums.CodingInputSignalSource)

	def set_high(self, signal_source_hp: enums.CodingInputSignalSource) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBT:SOURce:[HIGH] \n
		Snippet: driver.source.bb.dvbt.source.set_high(signal_source_hp = enums.CodingInputSignalSource.EXTernal) \n
		Sets the modulation source for the input signal. \n
			:param signal_source_hp: TSPLayer| EXTernal| TESTsignal
		"""
		param = Conversions.enum_scalar_to_str(signal_source_hp, enums.CodingInputSignalSource)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBT:SOURce:HIGH {param}')
