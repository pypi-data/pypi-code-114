from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Name:
	"""Name commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("name", core, parent)

	def set(self, bbin_iq_hs_chan_nam: str, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BBIN:CHANnel<CH0>:NAME \n
		Snippet: driver.source.bbin.channel.name.set(bbin_iq_hs_chan_nam = '1', channelNull = repcap.ChannelNull.Default) \n
		Queries the channel name. \n
			:param bbin_iq_hs_chan_nam: string
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.value_to_quoted_str(bbin_iq_hs_chan_nam)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BBIN:CHANnel{channelNull_cmd_val}:NAME {param}')

	def get(self, channelNull=repcap.ChannelNull.Default) -> str:
		"""SCPI: [SOURce<HW>]:BBIN:CHANnel<CH0>:NAME \n
		Snippet: value: str = driver.source.bbin.channel.name.get(channelNull = repcap.ChannelNull.Default) \n
		Queries the channel name. \n
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: bbin_iq_hs_chan_nam: string"""
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BBIN:CHANnel{channelNull_cmd_val}:NAME?')
		return trim_str_response(response)
