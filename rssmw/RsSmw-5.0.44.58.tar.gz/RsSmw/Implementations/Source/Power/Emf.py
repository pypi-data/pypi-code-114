from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Emf:
	"""Emf commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("emf", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:POWer:EMF:STATe \n
		Snippet: value: bool = driver.source.power.emf.get_state() \n
		Displays the signal level as voltage of the EMF. The displayed value represents the voltage over a 50 Ohm load. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:POWer:EMF:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:POWer:EMF:STATe \n
		Snippet: driver.source.power.emf.set_state(state = False) \n
		Displays the signal level as voltage of the EMF. The displayed value represents the voltage over a 50 Ohm load. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:POWer:EMF:STATe {param}')
