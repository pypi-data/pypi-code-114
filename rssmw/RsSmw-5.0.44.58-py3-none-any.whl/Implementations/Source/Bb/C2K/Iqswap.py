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
		"""SCPI: [SOURce<HW>]:BB:C2K:IQSWap:[STATe] \n
		Snippet: value: bool = driver.source.bb.c2K.iqswap.get_state() \n
		This command inverts the Q-part of the baseband signal if set to ON. The signal on the baseband outputs meets the
		cdma2000 standard. In order to generate an RF signal that conforms to the standard, the 'I/Q Swap' function in the 'I/Q
		Modulator' menu must be enabled ('On') (SOURce:IQ:SWAP ON) . \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:C2K:IQSWap:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:IQSWap:[STATe] \n
		Snippet: driver.source.bb.c2K.iqswap.set_state(state = False) \n
		This command inverts the Q-part of the baseband signal if set to ON. The signal on the baseband outputs meets the
		cdma2000 standard. In order to generate an RF signal that conforms to the standard, the 'I/Q Swap' function in the 'I/Q
		Modulator' menu must be enabled ('On') (SOURce:IQ:SWAP ON) . \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:IQSWap:STATe {param}')
