from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ...........Internal.Utilities import trim_str_response
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dselect:
	"""Dselect commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dselect", core, parent)

	def set(self, dselect: str, channelNull=repcap.ChannelNull.Default, transportChannelNull=repcap.TransportChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation:ENHanced:CHANnel<CH0>:DPCH:TCHannel<DI0>:DATA:DSELect \n
		Snippet: driver.source.bb.w3Gpp.bstation.enhanced.channel.dpch.tchannel.data.dselect.set(dselect = '1', channelNull = repcap.ChannelNull.Default, transportChannelNull = repcap.TransportChannelNull.Default) \n
		The command selects the data list for enhanced channels for the DLISt selection. The files are stored with the fixed file
		extensions *.dm_iqd in a directory of the user's choice. The directory applicable to the commands is defined with the
		command MMEMory:CDIR. To access the files in this directory, you only have to give the file name, without the path and
		the file extension. \n
			:param dselect: string
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:param transportChannelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Tchannel')
		"""
		param = Conversions.value_to_quoted_str(dselect)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		transportChannelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(transportChannelNull, repcap.TransportChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation:ENHanced:CHANnel{channelNull_cmd_val}:DPCH:TCHannel{transportChannelNull_cmd_val}:DATA:DSELect {param}')

	def get(self, channelNull=repcap.ChannelNull.Default, transportChannelNull=repcap.TransportChannelNull.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation:ENHanced:CHANnel<CH0>:DPCH:TCHannel<DI0>:DATA:DSELect \n
		Snippet: value: str = driver.source.bb.w3Gpp.bstation.enhanced.channel.dpch.tchannel.data.dselect.get(channelNull = repcap.ChannelNull.Default, transportChannelNull = repcap.TransportChannelNull.Default) \n
		The command selects the data list for enhanced channels for the DLISt selection. The files are stored with the fixed file
		extensions *.dm_iqd in a directory of the user's choice. The directory applicable to the commands is defined with the
		command MMEMory:CDIR. To access the files in this directory, you only have to give the file name, without the path and
		the file extension. \n
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:param transportChannelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Tchannel')
			:return: dselect: string"""
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		transportChannelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(transportChannelNull, repcap.TransportChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation:ENHanced:CHANnel{channelNull_cmd_val}:DPCH:TCHannel{transportChannelNull_cmd_val}:DATA:DSELect?')
		return trim_str_response(response)
