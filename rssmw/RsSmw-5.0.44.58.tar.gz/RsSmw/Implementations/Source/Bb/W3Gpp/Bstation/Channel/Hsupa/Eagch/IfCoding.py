from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IfCoding:
	"""IfCoding commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ifCoding", core, parent)

	def set(self, if_coding: bool, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:[HSUPa]:EAGCh:IFCoding \n
		Snippet: driver.source.bb.w3Gpp.bstation.channel.hsupa.eagch.ifCoding.set(if_coding = False, baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default) \n
		Enables/disables the information coding. \n
			:param if_coding: 1| ON| 0| OFF 0|OFF corresponds to a standard operation; no coding is performed and the data is sent uncoded. 1|ON you can configure the way the data is coded
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.bool_to_str(if_coding)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:HSUPa:EAGCh:IFCoding {param}')

	def get(self, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:[HSUPa]:EAGCh:IFCoding \n
		Snippet: value: bool = driver.source.bb.w3Gpp.bstation.channel.hsupa.eagch.ifCoding.get(baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default) \n
		Enables/disables the information coding. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: if_coding: 1| ON| 0| OFF 0|OFF corresponds to a standard operation; no coding is performed and the data is sent uncoded. 1|ON you can configure the way the data is coded"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:HSUPa:EAGCh:IFCoding?')
		return Conversions.str_to_bool(response)
