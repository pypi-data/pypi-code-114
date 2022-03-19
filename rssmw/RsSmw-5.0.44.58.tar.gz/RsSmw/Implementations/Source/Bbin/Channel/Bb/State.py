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

	def set(self, bbin_iq_hs_chan_sta: bool, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BBIN:CHANnel<CH0>:BB:STATe \n
		Snippet: driver.source.bbin.channel.bb.state.set(bbin_iq_hs_chan_sta = False, channelNull = repcap.ChannelNull.Default) \n
		Activates the channel. \n
			:param bbin_iq_hs_chan_sta: 1| ON| 0| OFF
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.bool_to_str(bbin_iq_hs_chan_sta)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BBIN:CHANnel{channelNull_cmd_val}:BB:STATe {param}')

	def get(self, channelNull=repcap.ChannelNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BBIN:CHANnel<CH0>:BB:STATe \n
		Snippet: value: bool = driver.source.bbin.channel.bb.state.get(channelNull = repcap.ChannelNull.Default) \n
		Activates the channel. \n
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: bbin_iq_hs_chan_sta: 1| ON| 0| OFF"""
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BBIN:CHANnel{channelNull_cmd_val}:BB:STATe?')
		return Conversions.str_to_bool(response)
