from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:MODulation:[ALL]:[STATe] \n
		Snippet: value: bool = driver.source.modulation.all.get_state() \n
		Activates all modulations that were active before the last switching off. \n
			:return: state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:MODulation:ALL:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:MODulation:[ALL]:[STATe] \n
		Snippet: driver.source.modulation.all.set_state(state = False) \n
		Activates all modulations that were active before the last switching off. \n
			:param state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:MODulation:ALL:STATe {param}')
