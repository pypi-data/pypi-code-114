from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Modeling:
	"""Modeling commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("modeling", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:ANTenna:MODeling:[STATe] \n
		Snippet: value: bool = driver.source.fsimulator.mimo.antenna.modeling.get_state() \n
		Enables/disables simulation of channel polarization. \n
			:return: antenna_state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:MIMO:ANTenna:MODeling:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, antenna_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:ANTenna:MODeling:[STATe] \n
		Snippet: driver.source.fsimulator.mimo.antenna.modeling.set_state(antenna_state = False) \n
		Enables/disables simulation of channel polarization. \n
			:param antenna_state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(antenna_state)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MIMO:ANTenna:MODeling:STATe {param}')
