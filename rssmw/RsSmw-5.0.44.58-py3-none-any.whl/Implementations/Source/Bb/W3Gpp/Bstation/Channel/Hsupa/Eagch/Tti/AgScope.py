from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AgScope:
	"""AgScope commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("agScope", core, parent)

	def set(self, ag_scope: enums.HsUpaAgchScope, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default, transmTimeIntervalNull=repcap.TransmTimeIntervalNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:[HSUPa]:EAGCh:TTI<DI0>:AGSCope \n
		Snippet: driver.source.bb.w3Gpp.bstation.channel.hsupa.eagch.tti.agScope.set(ag_scope = enums.HsUpaAgchScope.ALL, baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default, transmTimeIntervalNull = repcap.TransmTimeIntervalNull.Default) \n
		Sets the scope of the selected grant. According to the TS 25.321, the impact of each grant on the UE depends on this
		parameter. For E-DCH TTI = 10ms, the absolute grant scope is always ALL (All HARQ Processes) . \n
			:param ag_scope: ALL| PER
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:param transmTimeIntervalNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Tti')
		"""
		param = Conversions.enum_scalar_to_str(ag_scope, enums.HsUpaAgchScope)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		transmTimeIntervalNull_cmd_val = self._cmd_group.get_repcap_cmd_value(transmTimeIntervalNull, repcap.TransmTimeIntervalNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:HSUPa:EAGCh:TTI{transmTimeIntervalNull_cmd_val}:AGSCope {param}')

	# noinspection PyTypeChecker
	def get(self, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default, transmTimeIntervalNull=repcap.TransmTimeIntervalNull.Default) -> enums.HsUpaAgchScope:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:[HSUPa]:EAGCh:TTI<DI0>:AGSCope \n
		Snippet: value: enums.HsUpaAgchScope = driver.source.bb.w3Gpp.bstation.channel.hsupa.eagch.tti.agScope.get(baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default, transmTimeIntervalNull = repcap.TransmTimeIntervalNull.Default) \n
		Sets the scope of the selected grant. According to the TS 25.321, the impact of each grant on the UE depends on this
		parameter. For E-DCH TTI = 10ms, the absolute grant scope is always ALL (All HARQ Processes) . \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:param transmTimeIntervalNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Tti')
			:return: ag_scope: ALL| PER"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		transmTimeIntervalNull_cmd_val = self._cmd_group.get_repcap_cmd_value(transmTimeIntervalNull, repcap.TransmTimeIntervalNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:HSUPa:EAGCh:TTI{transmTimeIntervalNull_cmd_val}:AGSCope?')
		return Conversions.str_to_scalar_enum(response, enums.HsUpaAgchScope)
