from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Synchronize:
	"""Synchronize commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("synchronize", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:REGenerator:RESTart:SYNChronize:[STATe] \n
		Snippet: value: bool = driver.source.regenerator.restart.synchronize.get_state() \n
		Couples the REG blocks so that if both blocks are active, a subsequent restart event in any of them causes a simultaneous
		restart of the other. Restart event can be caused by a start/stop alternation or a parameter change that results in a
		signal recalculation and therefore a process restart. \n
			:return: reg_sync_state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:REGenerator:RESTart:SYNChronize:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, reg_sync_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:RESTart:SYNChronize:[STATe] \n
		Snippet: driver.source.regenerator.restart.synchronize.set_state(reg_sync_state = False) \n
		Couples the REG blocks so that if both blocks are active, a subsequent restart event in any of them causes a simultaneous
		restart of the other. Restart event can be caused by a start/stop alternation or a parameter change that results in a
		signal recalculation and therefore a process restart. \n
			:param reg_sync_state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(reg_sync_state)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:RESTart:SYNChronize:STATe {param}')
