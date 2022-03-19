from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Network:
	"""Network commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("network", core, parent)

	def get_port(self) -> int:
		"""SCPI: SYSTem:COMMunicate:BB<HW>:NETWork:PORT \n
		Snippet: value: int = driver.system.communicate.bb.network.get_port() \n
		No command help available \n
			:return: port: No help available
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:BB<HwInstance>:NETWork:PORT?')
		return Conversions.str_to_int(response)

	def set_port(self, port: int) -> None:
		"""SCPI: SYSTem:COMMunicate:BB<HW>:NETWork:PORT \n
		Snippet: driver.system.communicate.bb.network.set_port(port = 1) \n
		No command help available \n
			:param port: No help available
		"""
		param = Conversions.decimal_value_to_str(port)
		self._core.io.write(f'SYSTem:COMMunicate:BB<HwInstance>:NETWork:PORT {param}')
