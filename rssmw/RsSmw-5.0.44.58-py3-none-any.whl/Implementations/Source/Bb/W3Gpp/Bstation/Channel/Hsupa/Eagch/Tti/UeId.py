from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UeId:
	"""UeId commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ueId", core, parent)

	def set(self, ue_id: int, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default, transmTimeIntervalNull=repcap.TransmTimeIntervalNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:[HSUPa]:EAGCh:TTI<DI0>:UEID \n
		Snippet: driver.source.bb.w3Gpp.bstation.channel.hsupa.eagch.tti.ueId.set(ue_id = 1, baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default, transmTimeIntervalNull = repcap.TransmTimeIntervalNull.Default) \n
		Sets the UE Id for the selected TTI. \n
			:param ue_id: integer Range: 0 to 65535
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:param transmTimeIntervalNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Tti')
		"""
		param = Conversions.decimal_value_to_str(ue_id)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		transmTimeIntervalNull_cmd_val = self._cmd_group.get_repcap_cmd_value(transmTimeIntervalNull, repcap.TransmTimeIntervalNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:HSUPa:EAGCh:TTI{transmTimeIntervalNull_cmd_val}:UEID {param}')

	def get(self, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default, transmTimeIntervalNull=repcap.TransmTimeIntervalNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:[HSUPa]:EAGCh:TTI<DI0>:UEID \n
		Snippet: value: int = driver.source.bb.w3Gpp.bstation.channel.hsupa.eagch.tti.ueId.get(baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default, transmTimeIntervalNull = repcap.TransmTimeIntervalNull.Default) \n
		Sets the UE Id for the selected TTI. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:param transmTimeIntervalNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Tti')
			:return: ue_id: integer Range: 0 to 65535"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		transmTimeIntervalNull_cmd_val = self._cmd_group.get_repcap_cmd_value(transmTimeIntervalNull, repcap.TransmTimeIntervalNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:HSUPa:EAGCh:TTI{transmTimeIntervalNull_cmd_val}:UEID?')
		return Conversions.str_to_int(response)
