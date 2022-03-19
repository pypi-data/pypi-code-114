from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Infinite:
	"""Infinite commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("infinite", core, parent)

	def set(self, infinite: bool, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:USER<ST>:PACKet:INFinite \n
		Snippet: driver.source.bb.evdo.user.packet.infinite.set(infinite = False, userIx = repcap.UserIx.Default) \n
		Enables or disables sending an unlimited number of packets to the selected user. \n
			:param infinite: 1| ON| 0| OFF ON Enables sending of an unlimited number of packets to the user. OFF Disables sending of an unlimited number of packets to the user. The number of packets to be sent can be specified.
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.bool_to_str(infinite)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:USER{userIx_cmd_val}:PACKet:INFinite {param}')

	def get(self, userIx=repcap.UserIx.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EVDO:USER<ST>:PACKet:INFinite \n
		Snippet: value: bool = driver.source.bb.evdo.user.packet.infinite.get(userIx = repcap.UserIx.Default) \n
		Enables or disables sending an unlimited number of packets to the selected user. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: infinite: 1| ON| 0| OFF ON Enables sending of an unlimited number of packets to the user. OFF Disables sending of an unlimited number of packets to the user. The number of packets to be sent can be specified."""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EVDO:USER{userIx_cmd_val}:PACKet:INFinite?')
		return Conversions.str_to_bool(response)
