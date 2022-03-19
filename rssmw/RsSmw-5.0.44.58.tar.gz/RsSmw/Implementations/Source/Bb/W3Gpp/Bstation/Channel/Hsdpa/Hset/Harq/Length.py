from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Length:
	"""Length commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("length", core, parent)

	def set(self, length: int, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:HSDPa:HSET:HARQ:LENGth \n
		Snippet: driver.source.bb.w3Gpp.bstation.channel.hsdpa.hset.harq.length.set(length = 1, baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default) \n
		Sets the number of HARQ processes. This value determines the distribution of the payload in the subframes. \n
			:param length: integer Range: 1 to 6
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.decimal_value_to_str(length)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:HSDPa:HSET:HARQ:LENGth {param}')

	def get(self, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:HSDPa:HSET:HARQ:LENGth \n
		Snippet: value: int = driver.source.bb.w3Gpp.bstation.channel.hsdpa.hset.harq.length.get(baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default) \n
		Sets the number of HARQ processes. This value determines the distribution of the payload in the subframes. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: length: integer Range: 1 to 6"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:HSDPa:HSET:HARQ:LENGth?')
		return Conversions.str_to_int(response)
