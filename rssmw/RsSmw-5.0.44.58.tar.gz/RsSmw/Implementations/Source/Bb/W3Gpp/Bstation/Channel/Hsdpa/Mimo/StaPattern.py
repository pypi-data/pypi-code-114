from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Utilities import trim_str_response
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StaPattern:
	"""StaPattern commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("staPattern", core, parent)

	def set(self, sta_pattern: str, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:HSDPa:MIMO:STAPattern \n
		Snippet: driver.source.bb.w3Gpp.bstation.channel.hsdpa.mimo.staPattern.set(sta_pattern = '1', baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default) \n
		Enables/disables a temporal deactivation of Stream 2 per TTI in form of sending pattern. The stream 2 sending pattern is
		a sequence of max 16 values of '1' (enables Stream 2 for that TTI) and '-' (disabled Stream 2 for that TTI) . \n
			:param sta_pattern: string
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.value_to_quoted_str(sta_pattern)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:HSDPa:MIMO:STAPattern {param}')

	def get(self, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:HSDPa:MIMO:STAPattern \n
		Snippet: value: str = driver.source.bb.w3Gpp.bstation.channel.hsdpa.mimo.staPattern.get(baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default) \n
		Enables/disables a temporal deactivation of Stream 2 per TTI in form of sending pattern. The stream 2 sending pattern is
		a sequence of max 16 values of '1' (enables Stream 2 for that TTI) and '-' (disabled Stream 2 for that TTI) . \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: sta_pattern: string"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:HSDPa:MIMO:STAPattern?')
		return trim_str_response(response)
