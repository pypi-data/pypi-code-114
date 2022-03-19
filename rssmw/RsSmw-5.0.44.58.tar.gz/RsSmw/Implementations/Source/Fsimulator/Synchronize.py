from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Synchronize:
	"""Synchronize commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("synchronize", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce]:FSIMulator:SYNChronize:STATe \n
		Snippet: value: bool = driver.source.fsimulator.synchronize.get_state() \n
		Couples the fading simulators so that if both blocks are active, a subsequent restart event in any of them causes a
		simultaneous restart of the other. Restart event can be caused by a start/stop alternation or a parameter change that
		results in a signal recalculation and therefore a process restart. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce:FSIMulator:SYNChronize:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce]:FSIMulator:SYNChronize:STATe \n
		Snippet: driver.source.fsimulator.synchronize.set_state(state = False) \n
		Couples the fading simulators so that if both blocks are active, a subsequent restart event in any of them causes a
		simultaneous restart of the other. Restart event can be caused by a start/stop alternation or a parameter change that
		results in a signal recalculation and therefore a process restart. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce:FSIMulator:SYNChronize:STATe {param}')
