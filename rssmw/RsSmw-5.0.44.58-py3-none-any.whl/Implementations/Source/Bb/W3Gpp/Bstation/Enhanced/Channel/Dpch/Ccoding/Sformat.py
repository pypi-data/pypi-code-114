from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sformat:
	"""Sformat commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sformat", core, parent)

	def set(self, sformat: int, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation:ENHanced:CHANnel<CH0>:DPCH:CCODing:SFORmat \n
		Snippet: driver.source.bb.w3Gpp.bstation.enhanced.channel.dpch.ccoding.sformat.set(sformat = 1, channelNull = repcap.ChannelNull.Default) \n
		The command sets the slot format for the selected enhanced DPCH of base station 1. The slot format is fixed for
		channel-coded measurement channels conforming to the standard - 'Reference Measurement Channel'. Changing the slot format
		automatically activates User coding (W3GP:BST:ENH:CHAN<11...13>:DPCH:CCOD:TYPE USER) . The slot format also fixes the
		symbol rate, bits per frame, pilot length and TFCI state parameters. When a channel coding type conforming to the
		standard is selected ([:SOURce<hw>]:BB:W3GPp:BSTation:ENHanced:CHANnel<ch0>:DPCH:CCODing:TYPE) and channel coding is
		activated, the slot format is ([:SOURce<hw>]:BB:W3GPp:BSTation:ENHanced:CHANnel<ch0>:DPCH:CCODing:STATe) automatically
		set to the associated value. Changing the slot format automatically activates User coding (W3GP:BST:ENH:CHAN<11...
		13>:DPCH:CCOD:TYPE USER) . The command sets the symbol rate (W3GP:BST:ENH:CHAN:DPCH:CCOD:SRAT) , the bits per frame
		(W3GP:BST:ENH:CHAN:DPCH:CCOD:BPFR) , the pilot length (W3GP:BST1:CHAN:DPCC:PLEN) , and the TFCI state
		(W3GP:BST1:CHAN:DPCC:TFCI STAT) to the associated values. \n
			:param sformat: integer Range: 0 to dynamic
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.decimal_value_to_str(sformat)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation:ENHanced:CHANnel{channelNull_cmd_val}:DPCH:CCODing:SFORmat {param}')

	def get(self, channelNull=repcap.ChannelNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation:ENHanced:CHANnel<CH0>:DPCH:CCODing:SFORmat \n
		Snippet: value: int = driver.source.bb.w3Gpp.bstation.enhanced.channel.dpch.ccoding.sformat.get(channelNull = repcap.ChannelNull.Default) \n
		The command sets the slot format for the selected enhanced DPCH of base station 1. The slot format is fixed for
		channel-coded measurement channels conforming to the standard - 'Reference Measurement Channel'. Changing the slot format
		automatically activates User coding (W3GP:BST:ENH:CHAN<11...13>:DPCH:CCOD:TYPE USER) . The slot format also fixes the
		symbol rate, bits per frame, pilot length and TFCI state parameters. When a channel coding type conforming to the
		standard is selected ([:SOURce<hw>]:BB:W3GPp:BSTation:ENHanced:CHANnel<ch0>:DPCH:CCODing:TYPE) and channel coding is
		activated, the slot format is ([:SOURce<hw>]:BB:W3GPp:BSTation:ENHanced:CHANnel<ch0>:DPCH:CCODing:STATe) automatically
		set to the associated value. Changing the slot format automatically activates User coding (W3GP:BST:ENH:CHAN<11...
		13>:DPCH:CCOD:TYPE USER) . The command sets the symbol rate (W3GP:BST:ENH:CHAN:DPCH:CCOD:SRAT) , the bits per frame
		(W3GP:BST:ENH:CHAN:DPCH:CCOD:BPFR) , the pilot length (W3GP:BST1:CHAN:DPCC:PLEN) , and the TFCI state
		(W3GP:BST1:CHAN:DPCC:TFCI STAT) to the associated values. \n
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: sformat: integer Range: 0 to dynamic"""
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation:ENHanced:CHANnel{channelNull_cmd_val}:DPCH:CCODing:SFORmat?')
		return Conversions.str_to_int(response)
