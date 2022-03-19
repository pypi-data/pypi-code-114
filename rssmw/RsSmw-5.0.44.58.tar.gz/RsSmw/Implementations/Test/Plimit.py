from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Plimit:
	"""Plimit commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("plimit", core, parent)

	def get_frequency(self) -> float:
		"""SCPI: TEST:PLIMit:FREQuency \n
		Snippet: value: float = driver.test.plimit.get_frequency() \n
		No command help available \n
			:return: freq: No help available
		"""
		response = self._core.io.query_str('TEST:PLIMit:FREQuency?')
		return Conversions.str_to_float(response)

	def set_frequency(self, freq: float) -> None:
		"""SCPI: TEST:PLIMit:FREQuency \n
		Snippet: driver.test.plimit.set_frequency(freq = 1.0) \n
		No command help available \n
			:param freq: No help available
		"""
		param = Conversions.decimal_value_to_str(freq)
		self._core.io.write(f'TEST:PLIMit:FREQuency {param}')
