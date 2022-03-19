from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Interleaving:
	"""Interleaving commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("interleaving", core, parent)

	# noinspection PyTypeChecker
	def get_a(self) -> enums.CodingTimeInterleaving:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:TIME:[INTerleaving]:A \n
		Snippet: value: enums.CodingTimeInterleaving = driver.source.bb.isdbt.time.interleaving.get_a() \n
		Sets the time interleaving depth of each layer separately. \n
			:return: time_int_a: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:TIME:INTerleaving:A?')
		return Conversions.str_to_scalar_enum(response, enums.CodingTimeInterleaving)

	def set_a(self, time_int_a: enums.CodingTimeInterleaving) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:TIME:[INTerleaving]:A \n
		Snippet: driver.source.bb.isdbt.time.interleaving.set_a(time_int_a = enums.CodingTimeInterleaving._0) \n
		Sets the time interleaving depth of each layer separately. \n
			:param time_int_a: 0| 1| 16| 2| 32| 4| 8
		"""
		param = Conversions.enum_scalar_to_str(time_int_a, enums.CodingTimeInterleaving)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:TIME:INTerleaving:A {param}')

	# noinspection PyTypeChecker
	def get_b(self) -> enums.CodingTimeInterleaving:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:TIME:[INTerleaving]:B \n
		Snippet: value: enums.CodingTimeInterleaving = driver.source.bb.isdbt.time.interleaving.get_b() \n
		Sets the time interleaving depth of each layer separately. \n
			:return: time_int_b: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:TIME:INTerleaving:B?')
		return Conversions.str_to_scalar_enum(response, enums.CodingTimeInterleaving)

	def set_b(self, time_int_b: enums.CodingTimeInterleaving) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:TIME:[INTerleaving]:B \n
		Snippet: driver.source.bb.isdbt.time.interleaving.set_b(time_int_b = enums.CodingTimeInterleaving._0) \n
		Sets the time interleaving depth of each layer separately. \n
			:param time_int_b: 0| 1| 16| 2| 32| 4| 8
		"""
		param = Conversions.enum_scalar_to_str(time_int_b, enums.CodingTimeInterleaving)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:TIME:INTerleaving:B {param}')

	# noinspection PyTypeChecker
	def get_c(self) -> enums.CodingTimeInterleaving:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:TIME:[INTerleaving]:C \n
		Snippet: value: enums.CodingTimeInterleaving = driver.source.bb.isdbt.time.interleaving.get_c() \n
		Sets the time interleaving depth of each layer separately. \n
			:return: time_int_c: 0| 1| 16| 2| 32| 4| 8
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:TIME:INTerleaving:C?')
		return Conversions.str_to_scalar_enum(response, enums.CodingTimeInterleaving)

	def set_c(self, time_int_c: enums.CodingTimeInterleaving) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:TIME:[INTerleaving]:C \n
		Snippet: driver.source.bb.isdbt.time.interleaving.set_c(time_int_c = enums.CodingTimeInterleaving._0) \n
		Sets the time interleaving depth of each layer separately. \n
			:param time_int_c: 0| 1| 16| 2| 32| 4| 8
		"""
		param = Conversions.enum_scalar_to_str(time_int_c, enums.CodingTimeInterleaving)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:TIME:INTerleaving:C {param}')
