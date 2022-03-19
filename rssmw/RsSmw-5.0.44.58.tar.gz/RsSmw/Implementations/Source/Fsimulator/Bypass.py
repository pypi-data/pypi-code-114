from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bypass:
	"""Bypass commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bypass", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce]:FSIMulator:BYPass:STATe \n
		Snippet: value: bool = driver.source.fsimulator.bypass.get_state() \n
		Enables/disables bypassing of the fading simulator if the simulator is deactivated. \n
			:return: byp_state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce:FSIMulator:BYPass:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, byp_state: bool) -> None:
		"""SCPI: [SOURce]:FSIMulator:BYPass:STATe \n
		Snippet: driver.source.fsimulator.bypass.set_state(byp_state = False) \n
		Enables/disables bypassing of the fading simulator if the simulator is deactivated. \n
			:param byp_state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(byp_state)
		self._core.io.write(f'SOURce:FSIMulator:BYPass:STATe {param}')
