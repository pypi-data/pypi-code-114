from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Offset:
	"""Offset commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	def get_icomponent(self) -> float:
		"""SCPI: TEST:BB:GENerator:OFFSet:I \n
		Snippet: value: float = driver.test.bb.generator.offset.get_icomponent() \n
		No command help available \n
			:return: test_gen_offset_i: No help available
		"""
		response = self._core.io.query_str('TEST:BB:GENerator:OFFSet:I?')
		return Conversions.str_to_float(response)

	def set_icomponent(self, test_gen_offset_i: float) -> None:
		"""SCPI: TEST:BB:GENerator:OFFSet:I \n
		Snippet: driver.test.bb.generator.offset.set_icomponent(test_gen_offset_i = 1.0) \n
		No command help available \n
			:param test_gen_offset_i: No help available
		"""
		param = Conversions.decimal_value_to_str(test_gen_offset_i)
		self._core.io.write(f'TEST:BB:GENerator:OFFSet:I {param}')

	def get_qcomponent(self) -> float:
		"""SCPI: TEST:BB:GENerator:OFFSet:Q \n
		Snippet: value: float = driver.test.bb.generator.offset.get_qcomponent() \n
		No command help available \n
			:return: test_gen_offset_q: No help available
		"""
		response = self._core.io.query_str('TEST:BB:GENerator:OFFSet:Q?')
		return Conversions.str_to_float(response)

	def set_qcomponent(self, test_gen_offset_q: float) -> None:
		"""SCPI: TEST:BB:GENerator:OFFSet:Q \n
		Snippet: driver.test.bb.generator.offset.set_qcomponent(test_gen_offset_q = 1.0) \n
		No command help available \n
			:param test_gen_offset_q: No help available
		"""
		param = Conversions.decimal_value_to_str(test_gen_offset_q)
		self._core.io.write(f'TEST:BB:GENerator:OFFSet:Q {param}')
