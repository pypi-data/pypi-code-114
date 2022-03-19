from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Read:
	"""Read commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("read", core, parent)

	def set(self, read: enums.TpcReadMode, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:FDPCh:DPCCh:TPC:READ \n
		Snippet: driver.source.bb.w3Gpp.bstation.channel.fdpch.dpcch.tpc.read.set(read = enums.TpcReadMode.CONTinuous, baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default) \n
		The command sets the read out mode for the bit pattern of the TPC field. \n
			:param read: CONTinuous| S0A| S1A| S01A| S10A CONTinuous The bit pattern is used cyclically. S0A The bit pattern is used once, then the TPC sequence continues with 0 bits. S1A The bit pattern is used once, then the TPC sequence continues with 1 bit. S01A The bit pattern is used once and then the TPC sequence is continued with 0 bits and 1 bit alternately (in multiples, depending on by the symbol rate, for example, 00001111) . S10A The bit pattern is used once and then the TPC sequence is continued with 1 bit and 0 bits alternately (in multiples, depending on by the symbol rate, for example, 11110000) .
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.enum_scalar_to_str(read, enums.TpcReadMode)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:FDPCh:DPCCh:TPC:READ {param}')

	# noinspection PyTypeChecker
	def get(self, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default) -> enums.TpcReadMode:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:FDPCh:DPCCh:TPC:READ \n
		Snippet: value: enums.TpcReadMode = driver.source.bb.w3Gpp.bstation.channel.fdpch.dpcch.tpc.read.get(baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default) \n
		The command sets the read out mode for the bit pattern of the TPC field. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: read: CONTinuous| S0A| S1A| S01A| S10A CONTinuous The bit pattern is used cyclically. S0A The bit pattern is used once, then the TPC sequence continues with 0 bits. S1A The bit pattern is used once, then the TPC sequence continues with 1 bit. S01A The bit pattern is used once and then the TPC sequence is continued with 0 bits and 1 bit alternately (in multiples, depending on by the symbol rate, for example, 00001111) . S10A The bit pattern is used once and then the TPC sequence is continued with 1 bit and 0 bits alternately (in multiples, depending on by the symbol rate, for example, 11110000) ."""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:FDPCh:DPCCh:TPC:READ?')
		return Conversions.str_to_scalar_enum(response, enums.TpcReadMode)
