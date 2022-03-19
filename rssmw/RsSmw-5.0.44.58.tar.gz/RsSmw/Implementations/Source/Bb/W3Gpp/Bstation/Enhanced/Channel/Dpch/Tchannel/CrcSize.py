from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CrcSize:
	"""CrcSize commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("crcSize", core, parent)

	def set(self, crc_size: enums.TchCrc, channelNull=repcap.ChannelNull.Default, transportChannelNull=repcap.TransportChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation:ENHanced:CHANnel<CH0>:DPCH:TCHannel<DI0>:CRCSize \n
		Snippet: driver.source.bb.w3Gpp.bstation.enhanced.channel.dpch.tchannel.crcSize.set(crc_size = enums.TchCrc._12, channelNull = repcap.ChannelNull.Default, transportChannelNull = repcap.TransportChannelNull.Default) \n
		The command defines the CRC length for the selected transport channel. It is also possible to deactivate checksum
		determination. \n
			:param crc_size: NONE| 8| 12| 16| 24
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:param transportChannelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Tchannel')
		"""
		param = Conversions.enum_scalar_to_str(crc_size, enums.TchCrc)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		transportChannelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(transportChannelNull, repcap.TransportChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation:ENHanced:CHANnel{channelNull_cmd_val}:DPCH:TCHannel{transportChannelNull_cmd_val}:CRCSize {param}')

	# noinspection PyTypeChecker
	def get(self, channelNull=repcap.ChannelNull.Default, transportChannelNull=repcap.TransportChannelNull.Default) -> enums.TchCrc:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation:ENHanced:CHANnel<CH0>:DPCH:TCHannel<DI0>:CRCSize \n
		Snippet: value: enums.TchCrc = driver.source.bb.w3Gpp.bstation.enhanced.channel.dpch.tchannel.crcSize.get(channelNull = repcap.ChannelNull.Default, transportChannelNull = repcap.TransportChannelNull.Default) \n
		The command defines the CRC length for the selected transport channel. It is also possible to deactivate checksum
		determination. \n
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:param transportChannelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Tchannel')
			:return: crc_size: NONE| 8| 12| 16| 24"""
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		transportChannelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(transportChannelNull, repcap.TransportChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation:ENHanced:CHANnel{channelNull_cmd_val}:DPCH:TCHannel{transportChannelNull_cmd_val}:CRCSize?')
		return Conversions.str_to_scalar_enum(response, enums.TchCrc)
