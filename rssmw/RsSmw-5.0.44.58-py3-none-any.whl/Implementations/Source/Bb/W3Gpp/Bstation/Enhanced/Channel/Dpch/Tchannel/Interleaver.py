from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Interleaver:
	"""Interleaver commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("interleaver", core, parent)

	def set(self, interleaver: bool, channelNull=repcap.ChannelNull.Default, transportChannelNull=repcap.TransportChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation:ENHanced:CHANnel<CH0>:DPCH:TCHannel<DI0>:INTerleaver \n
		Snippet: driver.source.bb.w3Gpp.bstation.enhanced.channel.dpch.tchannel.interleaver.set(interleaver = False, channelNull = repcap.ChannelNull.Default, transportChannelNull = repcap.TransportChannelNull.Default) \n
		The command activates or deactivates channel coding interleaver state 1 for the selected channel. Interleaver state 1 can
		be activated and deactivated for each transport channel individually. The channel is selected via the suffix at TCHannel.
		Interleaver state 2 can only be activated or deactivated for all the transport channels together
		([:SOURce<hw>]:BB:W3GPp:BSTation:ENHanced:CHANnel<ch0>:DPCH:INTerleaver2) . Note: The interleaver states do not cause the
		symbol rate to change. \n
			:param interleaver: ON| OFF
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:param transportChannelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Tchannel')
		"""
		param = Conversions.bool_to_str(interleaver)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		transportChannelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(transportChannelNull, repcap.TransportChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation:ENHanced:CHANnel{channelNull_cmd_val}:DPCH:TCHannel{transportChannelNull_cmd_val}:INTerleaver {param}')

	def get(self, channelNull=repcap.ChannelNull.Default, transportChannelNull=repcap.TransportChannelNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation:ENHanced:CHANnel<CH0>:DPCH:TCHannel<DI0>:INTerleaver \n
		Snippet: value: bool = driver.source.bb.w3Gpp.bstation.enhanced.channel.dpch.tchannel.interleaver.get(channelNull = repcap.ChannelNull.Default, transportChannelNull = repcap.TransportChannelNull.Default) \n
		The command activates or deactivates channel coding interleaver state 1 for the selected channel. Interleaver state 1 can
		be activated and deactivated for each transport channel individually. The channel is selected via the suffix at TCHannel.
		Interleaver state 2 can only be activated or deactivated for all the transport channels together
		([:SOURce<hw>]:BB:W3GPp:BSTation:ENHanced:CHANnel<ch0>:DPCH:INTerleaver2) . Note: The interleaver states do not cause the
		symbol rate to change. \n
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:param transportChannelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Tchannel')
			:return: interleaver: ON| OFF"""
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		transportChannelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(transportChannelNull, repcap.TransportChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation:ENHanced:CHANnel{channelNull_cmd_val}:DPCH:TCHannel{transportChannelNull_cmd_val}:INTerleaver?')
		return Conversions.str_to_bool(response)
