from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AgvIndex:
	"""AgvIndex commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("agvIndex", core, parent)

	def set(self, agv_index: int, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default, transmTimeIntervalNull=repcap.TransmTimeIntervalNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:[HSUPa]:EAGCh:TTI<DI0>:AGVIndex \n
		Snippet: driver.source.bb.w3Gpp.bstation.channel.hsupa.eagch.tti.agvIndex.set(agv_index = 1, baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default, transmTimeIntervalNull = repcap.TransmTimeIntervalNull.Default) \n
		Sets the Index for the selected TTI. According to the TS 25.212 (4.10.1A.1) , there is a cross-reference between the
		grant's index and the grant value. \n
			:param agv_index: integer Range: 0 to 31
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:param transmTimeIntervalNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Tti')
		"""
		param = Conversions.decimal_value_to_str(agv_index)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		transmTimeIntervalNull_cmd_val = self._cmd_group.get_repcap_cmd_value(transmTimeIntervalNull, repcap.TransmTimeIntervalNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:HSUPa:EAGCh:TTI{transmTimeIntervalNull_cmd_val}:AGVIndex {param}')

	def get(self, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default, transmTimeIntervalNull=repcap.TransmTimeIntervalNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:[HSUPa]:EAGCh:TTI<DI0>:AGVIndex \n
		Snippet: value: int = driver.source.bb.w3Gpp.bstation.channel.hsupa.eagch.tti.agvIndex.get(baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default, transmTimeIntervalNull = repcap.TransmTimeIntervalNull.Default) \n
		Sets the Index for the selected TTI. According to the TS 25.212 (4.10.1A.1) , there is a cross-reference between the
		grant's index and the grant value. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:param transmTimeIntervalNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Tti')
			:return: agv_index: integer Range: 0 to 31"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		transmTimeIntervalNull_cmd_val = self._cmd_group.get_repcap_cmd_value(transmTimeIntervalNull, repcap.TransmTimeIntervalNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:HSUPa:EAGCh:TTI{transmTimeIntervalNull_cmd_val}:AGVIndex?')
		return Conversions.str_to_int(response)
