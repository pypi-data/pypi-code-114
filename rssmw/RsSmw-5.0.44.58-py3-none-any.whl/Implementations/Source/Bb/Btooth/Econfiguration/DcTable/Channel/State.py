from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:DCTable:CHANnel<CH0>:STATe \n
		Snippet: driver.source.bb.btooth.econfiguration.dcTable.channel.state.set(state = False, channelNull = repcap.ChannelNull.Default) \n
		Indicates used and unused data channels. Note: The previously used syntax ..:SET<ch>:STATe has been replaced by ...
		:CHANnel<ch>:STATe. Compatibility to the previous commands is given. This parameter is relevant for data event and
		advertising frame configuration with the packet types LL_CHANNEL_MAP_IND, CONNECT_IND. Within the option R&S SMW-K117,
		the following packet types are also relevant for the setting: AUX_CONNECT_IND, AUX_EXT_IND, AUX_ADV_IND, AUX_CHAIN_IND,
		AUX_SYNC_IND, AUX_SCAN_RSP. \n
			:param state: 1| ON| 0| OFF
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.bool_to_str(state)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:DCTable:CHANnel{channelNull_cmd_val}:STATe {param}')

	def get(self, channelNull=repcap.ChannelNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:DCTable:CHANnel<CH0>:STATe \n
		Snippet: value: bool = driver.source.bb.btooth.econfiguration.dcTable.channel.state.get(channelNull = repcap.ChannelNull.Default) \n
		Indicates used and unused data channels. Note: The previously used syntax ..:SET<ch>:STATe has been replaced by ...
		:CHANnel<ch>:STATe. Compatibility to the previous commands is given. This parameter is relevant for data event and
		advertising frame configuration with the packet types LL_CHANNEL_MAP_IND, CONNECT_IND. Within the option R&S SMW-K117,
		the following packet types are also relevant for the setting: AUX_CONNECT_IND, AUX_EXT_IND, AUX_ADV_IND, AUX_CHAIN_IND,
		AUX_SYNC_IND, AUX_SCAN_RSP. \n
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: state: 1| ON| 0| OFF"""
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:DCTable:CHANnel{channelNull_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
