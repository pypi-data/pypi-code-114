from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Test:
	"""Test commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("test", core, parent)

	def get_bytes(self) -> int:
		"""SCPI: SYSTem:COMMunicate:BB<HW>:QSFP:NETWork:DIAGnostic:TEST:BYTes \n
		Snippet: value: int = driver.system.communicate.bb.qsfp.network.diagnostic.test.get_bytes() \n
		No command help available \n
			:return: rx_bytes_count: No help available
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:BB<HwInstance>:QSFP:NETWork:DIAGnostic:TEST:BYTes?')
		return Conversions.str_to_int(response)

	def get_errors(self) -> int:
		"""SCPI: SYSTem:COMMunicate:BB<HW>:QSFP:NETWork:DIAGnostic:TEST:ERRors \n
		Snippet: value: int = driver.system.communicate.bb.qsfp.network.diagnostic.test.get_errors() \n
		No command help available \n
			:return: rx_errors_count: No help available
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:BB<HwInstance>:QSFP:NETWork:DIAGnostic:TEST:ERRors?')
		return Conversions.str_to_int(response)

	def get_value(self) -> bool:
		"""SCPI: SYSTem:COMMunicate:BB<HW>:QSFP:NETWork:DIAGnostic:TEST \n
		Snippet: value: bool = driver.system.communicate.bb.qsfp.network.diagnostic.test.get_value() \n
		No command help available \n
			:return: test_state: No help available
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:BB<HwInstance>:QSFP:NETWork:DIAGnostic:TEST?')
		return Conversions.str_to_bool(response)

	def set_value(self, test_state: bool) -> None:
		"""SCPI: SYSTem:COMMunicate:BB<HW>:QSFP:NETWork:DIAGnostic:TEST \n
		Snippet: driver.system.communicate.bb.qsfp.network.diagnostic.test.set_value(test_state = False) \n
		No command help available \n
			:param test_state: No help available
		"""
		param = Conversions.bool_to_str(test_state)
		self._core.io.write(f'SYSTem:COMMunicate:BB<HwInstance>:QSFP:NETWork:DIAGnostic:TEST {param}')
