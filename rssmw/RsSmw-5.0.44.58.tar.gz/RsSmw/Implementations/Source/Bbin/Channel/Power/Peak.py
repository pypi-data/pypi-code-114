from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Peak:
	"""Peak commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("peak", core, parent)

	def set(self, bbin_hs_ch_po_peak: float, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BBIN:CHANnel<CH0>:POWer:PEAK \n
		Snippet: driver.source.bbin.channel.power.peak.set(bbin_hs_ch_po_peak = 1.0, channelNull = repcap.ChannelNull.Default) \n
		Sets the peak level per channel. \n
			:param bbin_hs_ch_po_peak: float Range: -60 to 3.02
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.decimal_value_to_str(bbin_hs_ch_po_peak)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BBIN:CHANnel{channelNull_cmd_val}:POWer:PEAK {param}')

	def get(self, channelNull=repcap.ChannelNull.Default) -> float:
		"""SCPI: [SOURce<HW>]:BBIN:CHANnel<CH0>:POWer:PEAK \n
		Snippet: value: float = driver.source.bbin.channel.power.peak.get(channelNull = repcap.ChannelNull.Default) \n
		Sets the peak level per channel. \n
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: bbin_hs_ch_po_peak: float Range: -60 to 3.02"""
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BBIN:CHANnel{channelNull_cmd_val}:POWer:PEAK?')
		return Conversions.str_to_float(response)
