from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rms:
	"""Rms commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rms", core, parent)

	def get(self, channelNull=repcap.ChannelNull.Default) -> float:
		"""SCPI: [SOURce<HW>]:BBIN:CHANnel<CH0>:POWer:RMS \n
		Snippet: value: float = driver.source.bbin.channel.power.rms.get(channelNull = repcap.ChannelNull.Default) \n
		Queries the estimated RMS level. \n
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: bbin_iq_hs_ch_po_rms: float Range: -100 to 10"""
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BBIN:CHANnel{channelNull_cmd_val}:POWer:RMS?')
		return Conversions.str_to_float(response)
