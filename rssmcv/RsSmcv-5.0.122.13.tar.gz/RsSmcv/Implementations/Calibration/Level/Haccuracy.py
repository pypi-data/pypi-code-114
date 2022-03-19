from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Haccuracy:
	"""Haccuracy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("haccuracy", core, parent)

	def get_state(self) -> bool:
		"""SCPI: CALibration<HW>:LEVel:HACCuracy:[STATe] \n
		Snippet: value: bool = driver.calibration.level.haccuracy.get_state() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('CALibration<HwInstance>:LEVel:HACCuracy:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: CALibration<HW>:LEVel:HACCuracy:[STATe] \n
		Snippet: driver.calibration.level.haccuracy.set_state(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CALibration<HwInstance>:LEVel:HACCuracy:STATe {param}')
