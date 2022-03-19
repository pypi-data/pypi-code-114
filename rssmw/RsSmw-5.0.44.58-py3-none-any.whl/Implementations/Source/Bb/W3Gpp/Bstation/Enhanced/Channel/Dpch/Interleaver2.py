from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Interleaver2:
	"""Interleaver2 commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("interleaver2", core, parent)

	def set(self, interleaver_2: bool, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation:ENHanced:CHANnel<CH0>:DPCH:INTerleaver2 \n
		Snippet: driver.source.bb.w3Gpp.bstation.enhanced.channel.dpch.interleaver2.set(interleaver_2 = False, channelNull = repcap.ChannelNull.Default) \n
		The command activates or deactivates channel coding interleaver state 2 for the selected channel. Interleaver state 2 is
		activated or deactivated for all the transport channels together. Interleaver state 1 can be activated and deactivated
		for each transport channel individually (command
		[:SOURce<hw>]:BB:W3GPp:BSTation:ENHanced:CHANnel<ch0>:DPCH:TCHannel<di0>:INTerleaver) . Note: The interleaver states do
		not cause the symbol rate to change. \n
			:param interleaver_2: ON| OFF
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.bool_to_str(interleaver_2)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation:ENHanced:CHANnel{channelNull_cmd_val}:DPCH:INTerleaver2 {param}')

	def get(self, channelNull=repcap.ChannelNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation:ENHanced:CHANnel<CH0>:DPCH:INTerleaver2 \n
		Snippet: value: bool = driver.source.bb.w3Gpp.bstation.enhanced.channel.dpch.interleaver2.get(channelNull = repcap.ChannelNull.Default) \n
		The command activates or deactivates channel coding interleaver state 2 for the selected channel. Interleaver state 2 is
		activated or deactivated for all the transport channels together. Interleaver state 1 can be activated and deactivated
		for each transport channel individually (command
		[:SOURce<hw>]:BB:W3GPp:BSTation:ENHanced:CHANnel<ch0>:DPCH:TCHannel<di0>:INTerleaver) . Note: The interleaver states do
		not cause the symbol rate to change. \n
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: interleaver_2: ON| OFF"""
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation:ENHanced:CHANnel{channelNull_cmd_val}:DPCH:INTerleaver2?')
		return Conversions.str_to_bool(response)
