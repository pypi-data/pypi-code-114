from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Name:
	"""Name commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("name", core, parent)

	def set(self, dig_iq_hs_ch_name: str, iqConnector=repcap.IqConnector.Default, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:BBMM<CH>:CHANnel<ST0>:NAME \n
		Snippet: driver.source.iq.output.digital.bbmm.channel.name.set(dig_iq_hs_ch_name = '1', iqConnector = repcap.IqConnector.Default, channelNull = repcap.ChannelNull.Default) \n
		Sets the channel name. \n
			:param dig_iq_hs_ch_name: string
			:param iqConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bbmm')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.value_to_quoted_str(dig_iq_hs_ch_name)
		iqConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(iqConnector, repcap.IqConnector)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce:IQ:OUTPut:DIGital:BBMM{iqConnector_cmd_val}:CHANnel{channelNull_cmd_val}:NAME {param}')

	def get(self, iqConnector=repcap.IqConnector.Default, channelNull=repcap.ChannelNull.Default) -> str:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:BBMM<CH>:CHANnel<ST0>:NAME \n
		Snippet: value: str = driver.source.iq.output.digital.bbmm.channel.name.get(iqConnector = repcap.IqConnector.Default, channelNull = repcap.ChannelNull.Default) \n
		Sets the channel name. \n
			:param iqConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bbmm')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: dig_iq_hs_ch_name: string"""
		iqConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(iqConnector, repcap.IqConnector)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce:IQ:OUTPut:DIGital:BBMM{iqConnector_cmd_val}:CHANnel{channelNull_cmd_val}:NAME?')
		return trim_str_response(response)
