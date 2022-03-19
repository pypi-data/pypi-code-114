from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gain:
	"""Gain commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gain", core, parent)

	def get_icomponent(self) -> float:
		"""SCPI: TEST:BB:GENerator:GAIN:I \n
		Snippet: value: float = driver.test.bb.generator.gain.get_icomponent() \n
		No command help available \n
			:return: test_gen_gain_i: No help available
		"""
		response = self._core.io.query_str('TEST:BB:GENerator:GAIN:I?')
		return Conversions.str_to_float(response)

	def set_icomponent(self, test_gen_gain_i: float) -> None:
		"""SCPI: TEST:BB:GENerator:GAIN:I \n
		Snippet: driver.test.bb.generator.gain.set_icomponent(test_gen_gain_i = 1.0) \n
		No command help available \n
			:param test_gen_gain_i: No help available
		"""
		param = Conversions.decimal_value_to_str(test_gen_gain_i)
		self._core.io.write(f'TEST:BB:GENerator:GAIN:I {param}')

	def get_qcomponent(self) -> float:
		"""SCPI: TEST:BB:GENerator:GAIN:Q \n
		Snippet: value: float = driver.test.bb.generator.gain.get_qcomponent() \n
		No command help available \n
			:return: test_gen_gain_q: No help available
		"""
		response = self._core.io.query_str('TEST:BB:GENerator:GAIN:Q?')
		return Conversions.str_to_float(response)

	def set_qcomponent(self, test_gen_gain_q: float) -> None:
		"""SCPI: TEST:BB:GENerator:GAIN:Q \n
		Snippet: driver.test.bb.generator.gain.set_qcomponent(test_gen_gain_q = 1.0) \n
		No command help available \n
			:param test_gen_gain_q: No help available
		"""
		param = Conversions.decimal_value_to_str(test_gen_gain_q)
		self._core.io.write(f'TEST:BB:GENerator:GAIN:Q {param}')

	def get_value(self) -> float:
		"""SCPI: TEST:BB:GENerator:GAIN \n
		Snippet: value: float = driver.test.bb.generator.gain.get_value() \n
		No command help available \n
			:return: gain: No help available
		"""
		response = self._core.io.query_str('TEST:BB:GENerator:GAIN?')
		return Conversions.str_to_float(response)

	def set_value(self, gain: float) -> None:
		"""SCPI: TEST:BB:GENerator:GAIN \n
		Snippet: driver.test.bb.generator.gain.set_value(gain = 1.0) \n
		No command help available \n
			:param gain: No help available
		"""
		param = Conversions.decimal_value_to_str(gain)
		self._core.io.write(f'TEST:BB:GENerator:GAIN {param}')
