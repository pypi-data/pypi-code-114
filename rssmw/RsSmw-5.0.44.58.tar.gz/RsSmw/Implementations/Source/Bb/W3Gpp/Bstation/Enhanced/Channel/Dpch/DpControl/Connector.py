from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Connector:
	"""Connector commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("connector", core, parent)

	def set(self, connector: enums.FeedbackConnector, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation:ENHanced:CHANnel<CH0>:DPCH:DPControl:CONNector \n
		Snippet: driver.source.bb.w3Gpp.bstation.enhanced.channel.dpch.dpControl.connector.set(connector = enums.FeedbackConnector.GLOBal, channelNull = repcap.ChannelNull.Default) \n
		Determines the input connector at that the instrument expects the external control signal. \n
			:param connector: LOCal| GLOBal
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.enum_scalar_to_str(connector, enums.FeedbackConnector)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation:ENHanced:CHANnel{channelNull_cmd_val}:DPCH:DPControl:CONNector {param}')

	# noinspection PyTypeChecker
	def get(self, channelNull=repcap.ChannelNull.Default) -> enums.FeedbackConnector:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation:ENHanced:CHANnel<CH0>:DPCH:DPControl:CONNector \n
		Snippet: value: enums.FeedbackConnector = driver.source.bb.w3Gpp.bstation.enhanced.channel.dpch.dpControl.connector.get(channelNull = repcap.ChannelNull.Default) \n
		Determines the input connector at that the instrument expects the external control signal. \n
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: connector: LOCal| GLOBal"""
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation:ENHanced:CHANnel{channelNull_cmd_val}:DPCH:DPControl:CONNector?')
		return Conversions.str_to_scalar_enum(response, enums.FeedbackConnector)
