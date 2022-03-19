from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPy:
	"""ListPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("listPy", core, parent)

	def get_state(self) -> bool:
		"""SCPI: OUTPut<HW>:BLANk:LIST:STATe \n
		Snippet: value: bool = driver.output.blank.listPy.get_state() \n
		Activates RF output blanking. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('OUTPut<HwInstance>:BLANk:LIST:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: OUTPut<HW>:BLANk:LIST:STATe \n
		Snippet: driver.output.blank.listPy.set_state(state = False) \n
		Activates RF output blanking. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'OUTPut<HwInstance>:BLANk:LIST:STATe {param}')
