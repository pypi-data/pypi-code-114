from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Segments:
	"""Segments commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("segments", core, parent)

	def get_a(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:SEGMents:A \n
		Snippet: value: int = driver.source.bb.isdbt.segments.get_a() \n
		Sets the number of segments for layers A, B and C. \n
			:return: segments_a: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:SEGMents:A?')
		return Conversions.str_to_int(response)

	def set_a(self, segments_a: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:SEGMents:A \n
		Snippet: driver.source.bb.isdbt.segments.set_a(segments_a = 1) \n
		Sets the number of segments for layers A, B and C. \n
			:param segments_a: integer Range: 0 to 11
		"""
		param = Conversions.decimal_value_to_str(segments_a)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:SEGMents:A {param}')

	def get_b(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:SEGMents:B \n
		Snippet: value: int = driver.source.bb.isdbt.segments.get_b() \n
		Sets the number of segments for layers A, B and C. \n
			:return: segments_b: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:SEGMents:B?')
		return Conversions.str_to_int(response)

	def set_b(self, segments_b: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:SEGMents:B \n
		Snippet: driver.source.bb.isdbt.segments.set_b(segments_b = 1) \n
		Sets the number of segments for layers A, B and C. \n
			:param segments_b: integer Range: 0 to 11
		"""
		param = Conversions.decimal_value_to_str(segments_b)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:SEGMents:B {param}')

	def get_c(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:SEGMents:C \n
		Snippet: value: int = driver.source.bb.isdbt.segments.get_c() \n
		Sets the number of segments for layers A, B and C. \n
			:return: segments_c: integer Range: 0 to 11
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:SEGMents:C?')
		return Conversions.str_to_int(response)

	def set_c(self, segments_c: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:SEGMents:C \n
		Snippet: driver.source.bb.isdbt.segments.set_c(segments_c = 1) \n
		Sets the number of segments for layers A, B and C. \n
			:param segments_c: integer Range: 0 to 11
		"""
		param = Conversions.decimal_value_to_str(segments_c)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:SEGMents:C {param}')
