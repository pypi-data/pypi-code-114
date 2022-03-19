from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Test:
	"""Test commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("test", core, parent)

	def get_sequence(self) -> bytes:
		"""SCPI: SYSTem:INFormation:TEST:SEQuence \n
		Snippet: value: bytes = driver.system.information.test.get_sequence() \n
		No command help available \n
			:return: syst_info_test_sequence: No help available
		"""
		response = self._core.io.query_bin_block('SYSTem:INFormation:TEST:SEQuence?')
		return response

	def set_sequence(self, syst_info_test_sequence: bytes) -> None:
		"""SCPI: SYSTem:INFormation:TEST:SEQuence \n
		Snippet: driver.system.information.test.set_sequence(syst_info_test_sequence = b'ABCDEFGH') \n
		No command help available \n
			:param syst_info_test_sequence: No help available
		"""
		self._core.io.write_bin_block('SYSTem:INFormation:TEST:SEQuence ', syst_info_test_sequence)

	def get_state(self) -> bool:
		"""SCPI: SYSTem:INFormation:TEST:STATe \n
		Snippet: value: bool = driver.system.information.test.get_state() \n
		No command help available \n
			:return: test_state: No help available
		"""
		response = self._core.io.query_str('SYSTem:INFormation:TEST:STATe?')
		return Conversions.str_to_bool(response)
