from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TtInterval:
	"""TtInterval commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ttInterval", core, parent)

	def set(self, tt_interval: enums.TchTranTimInt, channelNull=repcap.ChannelNull.Default, transportChannelNull=repcap.TransportChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation:ENHanced:CHANnel<CH0>:DPCH:TCHannel<DI0>:TTINterval \n
		Snippet: driver.source.bb.w3Gpp.bstation.enhanced.channel.dpch.tchannel.ttInterval.set(tt_interval = enums.TchTranTimInt._10MS, channelNull = repcap.ChannelNull.Default, transportChannelNull = repcap.TransportChannelNull.Default) \n
		Sets the number of frames into which a TCH is divided. This setting also defines the interleaver depth. \n
			:param tt_interval: 10MS| 20MS| 40MS
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:param transportChannelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Tchannel')
		"""
		param = Conversions.enum_scalar_to_str(tt_interval, enums.TchTranTimInt)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		transportChannelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(transportChannelNull, repcap.TransportChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation:ENHanced:CHANnel{channelNull_cmd_val}:DPCH:TCHannel{transportChannelNull_cmd_val}:TTINterval {param}')

	# noinspection PyTypeChecker
	def get(self, channelNull=repcap.ChannelNull.Default, transportChannelNull=repcap.TransportChannelNull.Default) -> enums.TchTranTimInt:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation:ENHanced:CHANnel<CH0>:DPCH:TCHannel<DI0>:TTINterval \n
		Snippet: value: enums.TchTranTimInt = driver.source.bb.w3Gpp.bstation.enhanced.channel.dpch.tchannel.ttInterval.get(channelNull = repcap.ChannelNull.Default, transportChannelNull = repcap.TransportChannelNull.Default) \n
		Sets the number of frames into which a TCH is divided. This setting also defines the interleaver depth. \n
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:param transportChannelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Tchannel')
			:return: tt_interval: 10MS| 20MS| 40MS"""
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		transportChannelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(transportChannelNull, repcap.TransportChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation:ENHanced:CHANnel{channelNull_cmd_val}:DPCH:TCHannel{transportChannelNull_cmd_val}:TTINterval?')
		return Conversions.str_to_scalar_enum(response, enums.TchTranTimInt)
