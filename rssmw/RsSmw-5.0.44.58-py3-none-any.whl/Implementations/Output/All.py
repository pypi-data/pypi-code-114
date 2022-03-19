from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def get_state(self) -> bool:
		"""SCPI: OUTPut:ALL:[STATe] \n
		Snippet: value: bool = driver.output.all.get_state() \n
		Activates all RF output signals of the instrument. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('OUTPut:ALL:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: OUTPut:ALL:[STATe] \n
		Snippet: driver.output.all.set_state(state = False) \n
		Activates all RF output signals of the instrument. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'OUTPut:ALL:STATe {param}')
