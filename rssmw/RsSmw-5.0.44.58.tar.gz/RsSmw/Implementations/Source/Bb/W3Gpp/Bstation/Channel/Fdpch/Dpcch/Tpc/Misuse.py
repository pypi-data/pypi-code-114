from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Misuse:
	"""Misuse commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("misuse", core, parent)

	def set(self, misuse: bool, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:FDPCh:DPCCh:TPC:MISuse \n
		Snippet: driver.source.bb.w3Gpp.bstation.channel.fdpch.dpcch.tpc.misuse.set(misuse = False, baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default) \n
		The command activates 'mis-' use of the TPC field (Transmit Power Control) of the selected channel for controlling the
		channel powers of these channels of the specified base station.
		The bit pattern (see command [:SOURce<hw>]:BB:W3GPp:BSTation<st>:CHANnel<ch0>:FDPCh:DPCCh:TPC:DATA:PATTern) of the TPC
		field of each channel is used to control the channel power. A '1' leads to an increase of channel powers, a '0' to a
		reduction of channel powers. Channel power is limited to the range 0 dB to -60 dB. The step width of the change is
		defined with the command [:SOURce<hw>]:BB:W3GPp:BSTation<st>:CHANnel<ch0>:FDPCh:DPCCh:TPC:PSTep. \n
			:param misuse: ON| OFF
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.bool_to_str(misuse)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:FDPCh:DPCCh:TPC:MISuse {param}')

	def get(self, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:FDPCh:DPCCh:TPC:MISuse \n
		Snippet: value: bool = driver.source.bb.w3Gpp.bstation.channel.fdpch.dpcch.tpc.misuse.get(baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default) \n
		The command activates 'mis-' use of the TPC field (Transmit Power Control) of the selected channel for controlling the
		channel powers of these channels of the specified base station.
		The bit pattern (see command [:SOURce<hw>]:BB:W3GPp:BSTation<st>:CHANnel<ch0>:FDPCh:DPCCh:TPC:DATA:PATTern) of the TPC
		field of each channel is used to control the channel power. A '1' leads to an increase of channel powers, a '0' to a
		reduction of channel powers. Channel power is limited to the range 0 dB to -60 dB. The step width of the change is
		defined with the command [:SOURce<hw>]:BB:W3GPp:BSTation<st>:CHANnel<ch0>:FDPCh:DPCCh:TPC:PSTep. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: misuse: ON| OFF"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:FDPCh:DPCCh:TPC:MISuse?')
		return Conversions.str_to_bool(response)
