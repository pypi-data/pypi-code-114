from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class S64Qam:
	"""S64Qam commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("s64Qam", core, parent)

	def set(self, s_64_qam: bool, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:HSDPa:HSET:S64Qam \n
		Snippet: driver.source.bb.w3Gpp.bstation.channel.hsdpa.hset.s64Qam.set(s_64_qam = False, baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default) \n
		Enables/disables UE support of 64QAM. This command is enabled only for HS-SCCH Type 1 (normal operation) and 16QAM
		modulation. In case this parameter is disabled, i.e. the UE does not support 64QAM, the xccs,7 bit is used for
		channelization information. \n
			:param s_64_qam: ON| OFF
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.bool_to_str(s_64_qam)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:HSDPa:HSET:S64Qam {param}')

	def get(self, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:HSDPa:HSET:S64Qam \n
		Snippet: value: bool = driver.source.bb.w3Gpp.bstation.channel.hsdpa.hset.s64Qam.get(baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default) \n
		Enables/disables UE support of 64QAM. This command is enabled only for HS-SCCH Type 1 (normal operation) and 16QAM
		modulation. In case this parameter is disabled, i.e. the UE does not support 64QAM, the xccs,7 bit is used for
		channelization information. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: s_64_qam: ON| OFF"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:HSDPa:HSET:S64Qam?')
		return Conversions.str_to_bool(response)
