from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cfactor:
	"""Cfactor commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cfactor", core, parent)

	def set(self, bbin_iq_hs_ch_cr_fac: float, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BBIN:CHANnel<CH0>:POWer:CFACtor \n
		Snippet: driver.source.bbin.channel.power.cfactor.set(bbin_iq_hs_ch_cr_fac = 1.0, channelNull = repcap.ChannelNull.Default) \n
		Sets the crest factor of the individual channels. \n
			:param bbin_iq_hs_ch_cr_fac: float Range: 0 to 30
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.decimal_value_to_str(bbin_iq_hs_ch_cr_fac)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BBIN:CHANnel{channelNull_cmd_val}:POWer:CFACtor {param}')

	def get(self, channelNull=repcap.ChannelNull.Default) -> float:
		"""SCPI: [SOURce<HW>]:BBIN:CHANnel<CH0>:POWer:CFACtor \n
		Snippet: value: float = driver.source.bbin.channel.power.cfactor.get(channelNull = repcap.ChannelNull.Default) \n
		Sets the crest factor of the individual channels. \n
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: bbin_iq_hs_ch_cr_fac: float Range: 0 to 30"""
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BBIN:CHANnel{channelNull_cmd_val}:POWer:CFACtor?')
		return Conversions.str_to_float(response)
