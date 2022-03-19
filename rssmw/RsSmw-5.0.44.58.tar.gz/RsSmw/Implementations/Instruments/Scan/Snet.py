from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Snet:
	"""Snet commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("snet", core, parent)

	def get_ip_address(self) -> str:
		"""SCPI: INSTruments:SCAN:SNET:IPADdress \n
		Snippet: value: str = driver.instruments.scan.snet.get_ip_address() \n
		No command help available \n
			:return: address: No help available
		"""
		response = self._core.io.query_str('INSTruments:SCAN:SNET:IPADdress?')
		return trim_str_response(response)

	def set_ip_address(self, address: str) -> None:
		"""SCPI: INSTruments:SCAN:SNET:IPADdress \n
		Snippet: driver.instruments.scan.snet.set_ip_address(address = '1') \n
		No command help available \n
			:param address: No help available
		"""
		param = Conversions.value_to_quoted_str(address)
		self._core.io.write(f'INSTruments:SCAN:SNET:IPADdress {param}')

	def get_plength(self) -> int:
		"""SCPI: INSTruments:SCAN:SNET:PLENgth \n
		Snippet: value: int = driver.instruments.scan.snet.get_plength() \n
		No command help available \n
			:return: number: No help available
		"""
		response = self._core.io.query_str('INSTruments:SCAN:SNET:PLENgth?')
		return Conversions.str_to_int(response)

	def set_plength(self, number: int) -> None:
		"""SCPI: INSTruments:SCAN:SNET:PLENgth \n
		Snippet: driver.instruments.scan.snet.set_plength(number = 1) \n
		No command help available \n
			:param number: No help available
		"""
		param = Conversions.decimal_value_to_str(number)
		self._core.io.write(f'INSTruments:SCAN:SNET:PLENgth {param}')

	def get_state(self) -> bool:
		"""SCPI: INSTruments:SCAN:SNET:[STATe] \n
		Snippet: value: bool = driver.instruments.scan.snet.get_state() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('INSTruments:SCAN:SNET:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: INSTruments:SCAN:SNET:[STATe] \n
		Snippet: driver.instruments.scan.snet.set_state(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'INSTruments:SCAN:SNET:STATe {param}')
