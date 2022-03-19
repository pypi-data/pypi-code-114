from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Source:
	"""Source commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("source", core, parent)

	# noinspection PyTypeChecker
	def get_a(self) -> enums.CodingInputSignalSource:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:SOURce:A \n
		Snippet: value: enums.CodingInputSignalSource = driver.source.bb.isdbt.source.get_a() \n
		Sets the modulation source for layer A, B or C. \n
			:return: source_a: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:SOURce:A?')
		return Conversions.str_to_scalar_enum(response, enums.CodingInputSignalSource)

	def set_a(self, source_a: enums.CodingInputSignalSource) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:SOURce:A \n
		Snippet: driver.source.bb.isdbt.source.set_a(source_a = enums.CodingInputSignalSource.EXTernal) \n
		Sets the modulation source for layer A, B or C. \n
			:param source_a: TESTsignal| TSPLayer| EXTernal
		"""
		param = Conversions.enum_scalar_to_str(source_a, enums.CodingInputSignalSource)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:SOURce:A {param}')

	# noinspection PyTypeChecker
	def get_b(self) -> enums.CodingInputSignalSource:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:SOURce:B \n
		Snippet: value: enums.CodingInputSignalSource = driver.source.bb.isdbt.source.get_b() \n
		Sets the modulation source for layer A, B or C. \n
			:return: source_b: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:SOURce:B?')
		return Conversions.str_to_scalar_enum(response, enums.CodingInputSignalSource)

	def set_b(self, source_b: enums.CodingInputSignalSource) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:SOURce:B \n
		Snippet: driver.source.bb.isdbt.source.set_b(source_b = enums.CodingInputSignalSource.EXTernal) \n
		Sets the modulation source for layer A, B or C. \n
			:param source_b: TESTsignal| TSPLayer| EXTernal
		"""
		param = Conversions.enum_scalar_to_str(source_b, enums.CodingInputSignalSource)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:SOURce:B {param}')

	# noinspection PyTypeChecker
	def get_c(self) -> enums.CodingInputSignalSource:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:SOURce:C \n
		Snippet: value: enums.CodingInputSignalSource = driver.source.bb.isdbt.source.get_c() \n
		Sets the modulation source for layer A, B or C. \n
			:return: source_c: TESTsignal| TSPLayer| EXTernal
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:SOURce:C?')
		return Conversions.str_to_scalar_enum(response, enums.CodingInputSignalSource)

	def set_c(self, source_c: enums.CodingInputSignalSource) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:SOURce:C \n
		Snippet: driver.source.bb.isdbt.source.set_c(source_c = enums.CodingInputSignalSource.EXTernal) \n
		Sets the modulation source for layer A, B or C. \n
			:param source_c: TESTsignal| TSPLayer| EXTernal
		"""
		param = Conversions.enum_scalar_to_str(source_c, enums.CodingInputSignalSource)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:SOURce:C {param}')
