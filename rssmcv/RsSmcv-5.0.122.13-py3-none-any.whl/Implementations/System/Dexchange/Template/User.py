from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class User:
	"""User commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("user", core, parent)

	def get_catalog(self) -> List[str]:
		"""SCPI: SYSTem:DEXChange:TEMPlate:USER:CATalog \n
		Snippet: value: List[str] = driver.system.dexchange.template.user.get_catalog() \n
		No command help available \n
			:return: catalog: No help available
		"""
		response = self._core.io.query_str('SYSTem:DEXChange:TEMPlate:USER:CATalog?')
		return Conversions.str_to_str_list(response)

	def delete(self, filename: str) -> None:
		"""SCPI: SYSTem:DEXChange:TEMPlate:USER:DELete \n
		Snippet: driver.system.dexchange.template.user.delete(filename = '1') \n
		No command help available \n
			:param filename: No help available
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SYSTem:DEXChange:TEMPlate:USER:DELete {param}')

	def get_select(self) -> str:
		"""SCPI: SYSTem:DEXChange:TEMPlate:USER:SELect \n
		Snippet: value: str = driver.system.dexchange.template.user.get_select() \n
		No command help available \n
			:return: filename: No help available
		"""
		response = self._core.io.query_str('SYSTem:DEXChange:TEMPlate:USER:SELect?')
		return trim_str_response(response)

	def set_select(self, filename: str) -> None:
		"""SCPI: SYSTem:DEXChange:TEMPlate:USER:SELect \n
		Snippet: driver.system.dexchange.template.user.set_select(filename = '1') \n
		No command help available \n
			:param filename: No help available
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SYSTem:DEXChange:TEMPlate:USER:SELect {param}')
