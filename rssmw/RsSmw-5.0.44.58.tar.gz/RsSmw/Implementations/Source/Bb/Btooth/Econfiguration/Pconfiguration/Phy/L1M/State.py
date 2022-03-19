from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, channel=repcap.Channel.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:PHY:L1M<CH>:STATe \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.phy.l1M.state.set(state = False, channel = repcap.Channel.Default) \n
		Sets the LE 1M PHY in the CtrData field of the LL_PERIODIC_SYNC_IND PDU. \n
			:param state: 1| ON| 0| OFF
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'L1M')
		"""
		param = Conversions.bool_to_str(state)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:PHY:L1M{channel_cmd_val}:STATe {param}')

	def get(self, channel=repcap.Channel.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:PHY:L1M<CH>:STATe \n
		Snippet: value: bool = driver.source.bb.btooth.econfiguration.pconfiguration.phy.l1M.state.get(channel = repcap.Channel.Default) \n
		Sets the LE 1M PHY in the CtrData field of the LL_PERIODIC_SYNC_IND PDU. \n
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'L1M')
			:return: state: 1| ON| 0| OFF"""
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:PHY:L1M{channel_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
