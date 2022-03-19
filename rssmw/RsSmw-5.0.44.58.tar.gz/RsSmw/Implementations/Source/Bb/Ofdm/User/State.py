from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, userNull=repcap.UserNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:USER<CH0>:STATe \n
		Snippet: driver.source.bb.ofdm.user.state.set(state = False, userNull = repcap.UserNull.Default) \n
		Activates the user. \n
			:param state: 0| 1| OFF| ON
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
		"""
		param = Conversions.bool_to_str(state)
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:USER{userNull_cmd_val}:STATe {param}')

	def get(self, userNull=repcap.UserNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:OFDM:USER<CH0>:STATe \n
		Snippet: value: bool = driver.source.bb.ofdm.user.state.get(userNull = repcap.UserNull.Default) \n
		Activates the user. \n
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:return: state: 0| 1| OFF| ON"""
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:OFDM:USER{userNull_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
