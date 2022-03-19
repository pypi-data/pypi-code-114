from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Count:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def set(self, count: int, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:USER<ST>:PACKet:COUNt \n
		Snippet: driver.source.bb.evdo.user.packet.count.set(count = 1, userIx = repcap.UserIx.Default) \n
		Sets the number of packets to send to the selected user. The number of packets to be send depends on whether the
		parameter 'Infinite' is enabled or disabled. If 'Infinite' is enabled, there is no limit to the number of packets sent to
		the user. If 'Infinite' is disabled and a value is specified while packets are being sent, the new count value is used at
		the end of transmission of the current packet. If a value of zero is specified, the transmission to the user is stopped
		at the end of the current packet. \n
			:param count: integer Range: 0 to 65536
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.decimal_value_to_str(count)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:USER{userIx_cmd_val}:PACKet:COUNt {param}')

	def get(self, userIx=repcap.UserIx.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EVDO:USER<ST>:PACKet:COUNt \n
		Snippet: value: int = driver.source.bb.evdo.user.packet.count.get(userIx = repcap.UserIx.Default) \n
		Sets the number of packets to send to the selected user. The number of packets to be send depends on whether the
		parameter 'Infinite' is enabled or disabled. If 'Infinite' is enabled, there is no limit to the number of packets sent to
		the user. If 'Infinite' is disabled and a value is specified while packets are being sent, the new count value is used at
		the end of transmission of the current packet. If a value of zero is specified, the transmission to the user is stopped
		at the end of the current packet. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: count: integer Range: 0 to 65536"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EVDO:USER{userIx_cmd_val}:PACKet:COUNt?')
		return Conversions.str_to_int(response)
