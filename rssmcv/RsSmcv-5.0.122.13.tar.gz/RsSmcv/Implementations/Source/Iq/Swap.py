from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Swap:
	"""Swap commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("swap", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:IQ:SWAP:[STATe] \n
		Snippet: value: bool = driver.source.iq.swap.get_state() \n
		Swaps the I and Q channel. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:SWAP:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:IQ:SWAP:[STATe] \n
		Snippet: driver.source.iq.swap.set_state(state = False) \n
		Swaps the I and Q channel. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:IQ:SWAP:STATe {param}')
