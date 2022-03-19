from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ip:
	"""Ip commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ip", core, parent)

	def get_address(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:INPut:DESTination:IP:ADDRess \n
		Snippet: value: str = driver.source.bb.a3Tsc.inputPy.destination.ip.get_address() \n
		Sets the destination IP address of the IP connection for external or internal IP data. \n
			:return: dest_ip_address: string Range: 224.0.0.0 to 239..255.255.255
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:INPut:DESTination:IP:ADDRess?')
		return trim_str_response(response)

	def set_address(self, dest_ip_address: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:INPut:DESTination:IP:ADDRess \n
		Snippet: driver.source.bb.a3Tsc.inputPy.destination.ip.set_address(dest_ip_address = '1') \n
		Sets the destination IP address of the IP connection for external or internal IP data. \n
			:param dest_ip_address: string Range: 224.0.0.0 to 239..255.255.255
		"""
		param = Conversions.value_to_quoted_str(dest_ip_address)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:INPut:DESTination:IP:ADDRess {param}')

	def get_port(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:INPut:DESTination:IP:PORT \n
		Snippet: value: int = driver.source.bb.a3Tsc.inputPy.destination.ip.get_port() \n
		Sets the destination IP port of the IP connection for external or internal IP data. \n
			:return: dest_ip_port: integer Range: 0 to 65535
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:INPut:DESTination:IP:PORT?')
		return Conversions.str_to_int(response)

	def set_port(self, dest_ip_port: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:INPut:DESTination:IP:PORT \n
		Snippet: driver.source.bb.a3Tsc.inputPy.destination.ip.set_port(dest_ip_port = 1) \n
		Sets the destination IP port of the IP connection for external or internal IP data. \n
			:param dest_ip_port: integer Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(dest_ip_port)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:INPut:DESTination:IP:PORT {param}')
