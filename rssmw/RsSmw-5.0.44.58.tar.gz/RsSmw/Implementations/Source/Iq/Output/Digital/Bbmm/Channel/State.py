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

	def set(self, dig_iq_hs_out_ch_sta: bool, iqConnector=repcap.IqConnector.Default, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:BBMM<CH>:CHANnel<ST0>:STATe \n
		Snippet: driver.source.iq.output.digital.bbmm.channel.state.set(dig_iq_hs_out_ch_sta = False, iqConnector = repcap.IqConnector.Default, channelNull = repcap.ChannelNull.Default) \n
		Enables the channel. \n
			:param dig_iq_hs_out_ch_sta: 1| ON| 0| OFF
			:param iqConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bbmm')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.bool_to_str(dig_iq_hs_out_ch_sta)
		iqConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(iqConnector, repcap.IqConnector)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce:IQ:OUTPut:DIGital:BBMM{iqConnector_cmd_val}:CHANnel{channelNull_cmd_val}:STATe {param}')

	def get(self, iqConnector=repcap.IqConnector.Default, channelNull=repcap.ChannelNull.Default) -> bool:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:BBMM<CH>:CHANnel<ST0>:STATe \n
		Snippet: value: bool = driver.source.iq.output.digital.bbmm.channel.state.get(iqConnector = repcap.IqConnector.Default, channelNull = repcap.ChannelNull.Default) \n
		Enables the channel. \n
			:param iqConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bbmm')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: dig_iq_hs_out_ch_sta: 1| ON| 0| OFF"""
		iqConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(iqConnector, repcap.IqConnector)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce:IQ:OUTPut:DIGital:BBMM{iqConnector_cmd_val}:CHANnel{channelNull_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
