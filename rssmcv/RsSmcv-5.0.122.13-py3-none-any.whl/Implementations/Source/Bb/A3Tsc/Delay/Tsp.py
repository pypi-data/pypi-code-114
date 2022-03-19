from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tsp:
	"""Tsp commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tsp", core, parent)

	def get_ltt(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:DELay:TSP:LTT \n
		Snippet: value: str = driver.source.bb.a3Tsc.delay.tsp.get_ltt() \n
		No command help available \n
			:return: ltt: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:DELay:TSP:LTT?')
		return trim_str_response(response)

	def get_ltu(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:DELay:TSP:LTU \n
		Snippet: value: str = driver.source.bb.a3Tsc.delay.tsp.get_ltu() \n
		No command help available \n
			:return: ltu: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:DELay:TSP:LTU?')
		return trim_str_response(response)

	def get_toet(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:DELay:TSP:TOET \n
		Snippet: value: str = driver.source.bb.a3Tsc.delay.tsp.get_toet() \n
		No command help available \n
			:return: toet: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:DELay:TSP:TOET?')
		return trim_str_response(response)

	def get_uto(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:DELay:TSP:UTO \n
		Snippet: value: int = driver.source.bb.a3Tsc.delay.tsp.get_uto() \n
		No command help available \n
			:return: uto: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:DELay:TSP:UTO?')
		return Conversions.str_to_int(response)

	def set_uto(self, uto: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:DELay:TSP:UTO \n
		Snippet: driver.source.bb.a3Tsc.delay.tsp.set_uto(uto = 1) \n
		No command help available \n
			:param uto: No help available
		"""
		param = Conversions.decimal_value_to_str(uto)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:DELay:TSP:UTO {param}')
