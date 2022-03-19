from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tpower:
	"""Tpower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tpower", core, parent)

	def set(self, tpower: float, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:HSDPa:HSET:TPOWer \n
		Snippet: driver.source.bb.w3Gpp.bstation.channel.hsdpa.hset.tpower.set(tpower = 1.0, baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default) \n
		Sets the total power of the HS-PDSCH channels in the H-Set. The individual power levels of the HS-PDSCHs are calculated
		automatically and can be queried with the command [:SOURce<hw>]:BB:W3GPp:BSTation<st>:CHANnel<ch0>:POWer. \n
			:param tpower: float The min/max values depend on the number of HS-PDSCH channelization codes ([:SOURcehw]:BB:W3GPp:BSTationst:CHANnelch0:HSDPa:HSET:CLENgth) and are calculated as follow: min = -80 dB + 10*log10(NumberOfHS-PDSCHChannelizationCodes) max = 0 dB + 10*log10(NumberOfHS-PDSCHChannelizationCodes) Range: dynamic to dynamic
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.decimal_value_to_str(tpower)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:HSDPa:HSET:TPOWer {param}')

	def get(self, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:HSDPa:HSET:TPOWer \n
		Snippet: value: float = driver.source.bb.w3Gpp.bstation.channel.hsdpa.hset.tpower.get(baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default) \n
		Sets the total power of the HS-PDSCH channels in the H-Set. The individual power levels of the HS-PDSCHs are calculated
		automatically and can be queried with the command [:SOURce<hw>]:BB:W3GPp:BSTation<st>:CHANnel<ch0>:POWer. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: tpower: float The min/max values depend on the number of HS-PDSCH channelization codes ([:SOURcehw]:BB:W3GPp:BSTationst:CHANnelch0:HSDPa:HSET:CLENgth) and are calculated as follow: min = -80 dB + 10*log10(NumberOfHS-PDSCHChannelizationCodes) max = 0 dB + 10*log10(NumberOfHS-PDSCHChannelizationCodes) Range: dynamic to dynamic"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:HSDPa:HSET:TPOWer?')
		return Conversions.str_to_float(response)
