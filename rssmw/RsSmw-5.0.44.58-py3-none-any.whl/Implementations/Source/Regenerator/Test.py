from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Test:
	"""Test commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("test", core, parent)

	def get_sim_fsw(self) -> bool:
		"""SCPI: [SOURce<HW>]:REGenerator:TEST:SIMFsw \n
		Snippet: value: bool = driver.source.regenerator.test.get_sim_fsw() \n
		No command help available \n
			:return: test_fsw_state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:REGenerator:TEST:SIMFsw?')
		return Conversions.str_to_bool(response)

	def set_sim_fsw(self, test_fsw_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:TEST:SIMFsw \n
		Snippet: driver.source.regenerator.test.set_sim_fsw(test_fsw_state = False) \n
		No command help available \n
			:param test_fsw_state: No help available
		"""
		param = Conversions.bool_to_str(test_fsw_state)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:TEST:SIMFsw {param}')
