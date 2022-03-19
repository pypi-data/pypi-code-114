from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.HsMode, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:HSDPa:MODE \n
		Snippet: driver.source.bb.w3Gpp.bstation.channel.hsdpa.mode.set(mode = enums.HsMode.CONTinuous, baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default) \n
		The command selects the HSDPA mode. \n
			:param mode: CONTinuous| PSF0| PSF1| PSF2| PSF3| PSF4| HSET CONTinuous The high speed channel is generated continuously. This mode is defined in test model 5. PSFx The high speed channel is generated in packet mode. The start of the channel is set by selecting the subframe in which the first packet is sent. HSET The high speed channels are preset according to TS 25.1401 Annex A.7, H-Set.
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.HsMode)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:HSDPa:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default) -> enums.HsMode:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:HSDPa:MODE \n
		Snippet: value: enums.HsMode = driver.source.bb.w3Gpp.bstation.channel.hsdpa.mode.get(baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default) \n
		The command selects the HSDPA mode. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: mode: CONTinuous| PSF0| PSF1| PSF2| PSF3| PSF4| HSET CONTinuous The high speed channel is generated continuously. This mode is defined in test model 5. PSFx The high speed channel is generated in packet mode. The start of the channel is set by selecting the subframe in which the first packet is sent. HSET The high speed channels are preset according to TS 25.1401 Annex A.7, H-Set."""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:HSDPa:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.HsMode)
