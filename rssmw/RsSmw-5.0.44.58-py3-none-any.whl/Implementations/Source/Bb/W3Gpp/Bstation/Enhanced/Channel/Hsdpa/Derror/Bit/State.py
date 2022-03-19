from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation:[ENHanced]:CHANnel<CH0>:HSDPa:DERRor:BIT:STATe \n
		Snippet: driver.source.bb.w3Gpp.bstation.enhanced.channel.hsdpa.derror.bit.state.set(state = False, channelNull = repcap.ChannelNull.Default) \n
		The command activates bit error generation or deactivates it. Bit errors are inserted into the data stream of the coupled
		HS-PDSCHs. It is possible to select the layer in which the errors are inserted (physical or transport layer) . When the
		data source is read out, individual bits are deliberately inverted at random points in the data bit stream at the
		specified error rate in order to simulate an invalid signal. \n
			:param state: ON| OFF
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.bool_to_str(state)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation:ENHanced:CHANnel{channelNull_cmd_val}:HSDPa:DERRor:BIT:STATe {param}')

	def get(self, channelNull=repcap.ChannelNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation:[ENHanced]:CHANnel<CH0>:HSDPa:DERRor:BIT:STATe \n
		Snippet: value: bool = driver.source.bb.w3Gpp.bstation.enhanced.channel.hsdpa.derror.bit.state.get(channelNull = repcap.ChannelNull.Default) \n
		The command activates bit error generation or deactivates it. Bit errors are inserted into the data stream of the coupled
		HS-PDSCHs. It is possible to select the layer in which the errors are inserted (physical or transport layer) . When the
		data source is read out, individual bits are deliberately inverted at random points in the data bit stream at the
		specified error rate in order to simulate an invalid signal. \n
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: state: ON| OFF"""
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation:ENHanced:CHANnel{channelNull_cmd_val}:HSDPa:DERRor:BIT:STATe?')
		return Conversions.str_to_bool(response)
