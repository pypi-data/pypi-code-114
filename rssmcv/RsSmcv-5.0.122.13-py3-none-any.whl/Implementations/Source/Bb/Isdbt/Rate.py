from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rate:
	"""Rate commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rate", core, parent)

	# noinspection PyTypeChecker
	def get_a(self) -> enums.CodingCoderate:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:RATE:A \n
		Snippet: value: enums.CodingCoderate = driver.source.bb.isdbt.rate.get_a() \n
		Sets the code rate. \n
			:return: coderate_a: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:RATE:A?')
		return Conversions.str_to_scalar_enum(response, enums.CodingCoderate)

	def set_a(self, coderate_a: enums.CodingCoderate) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:RATE:A \n
		Snippet: driver.source.bb.isdbt.rate.set_a(coderate_a = enums.CodingCoderate.R1_2) \n
		Sets the code rate. \n
			:param coderate_a: R7_8| R5_6| R3_4| R2_3| R1_2
		"""
		param = Conversions.enum_scalar_to_str(coderate_a, enums.CodingCoderate)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:RATE:A {param}')

	# noinspection PyTypeChecker
	def get_b(self) -> enums.CodingCoderate:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:RATE:B \n
		Snippet: value: enums.CodingCoderate = driver.source.bb.isdbt.rate.get_b() \n
		Sets the code rate. \n
			:return: coderate_b: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:RATE:B?')
		return Conversions.str_to_scalar_enum(response, enums.CodingCoderate)

	def set_b(self, coderate_b: enums.CodingCoderate) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:RATE:B \n
		Snippet: driver.source.bb.isdbt.rate.set_b(coderate_b = enums.CodingCoderate.R1_2) \n
		Sets the code rate. \n
			:param coderate_b: R7_8| R5_6| R3_4| R2_3| R1_2
		"""
		param = Conversions.enum_scalar_to_str(coderate_b, enums.CodingCoderate)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:RATE:B {param}')

	# noinspection PyTypeChecker
	def get_c(self) -> enums.CodingCoderate:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:RATE:C \n
		Snippet: value: enums.CodingCoderate = driver.source.bb.isdbt.rate.get_c() \n
		Sets the code rate. \n
			:return: coderate_c: R7_8| R5_6| R3_4| R2_3| R1_2
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:RATE:C?')
		return Conversions.str_to_scalar_enum(response, enums.CodingCoderate)

	def set_c(self, coderate_c: enums.CodingCoderate) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:RATE:C \n
		Snippet: driver.source.bb.isdbt.rate.set_c(coderate_c = enums.CodingCoderate.R1_2) \n
		Sets the code rate. \n
			:param coderate_c: R7_8| R5_6| R3_4| R2_3| R1_2
		"""
		param = Conversions.enum_scalar_to_str(coderate_c, enums.CodingCoderate)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:RATE:C {param}')
