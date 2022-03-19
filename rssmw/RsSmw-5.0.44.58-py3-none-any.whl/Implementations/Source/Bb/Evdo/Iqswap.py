from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Iqswap:
	"""Iqswap commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iqswap", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EVDO:IQSWap:STATe \n
		Snippet: value: bool = driver.source.bb.evdo.iqswap.get_state() \n
		Inverts the Q-part of the baseband signal \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EVDO:IQSWap:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:IQSWap:STATe \n
		Snippet: driver.source.bb.evdo.iqswap.set_state(state = False) \n
		Inverts the Q-part of the baseband signal \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:IQSWap:STATe {param}')
