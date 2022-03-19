from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ttiedch:
	"""Ttiedch commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ttiedch", core, parent)

	def set(self, ttiedch: enums.HsUpaDchTti, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:[HSUPa]:EAGCh:TTIEdch \n
		Snippet: driver.source.bb.w3Gpp.bstation.channel.hsupa.eagch.ttiedch.set(ttiedch = enums.HsUpaDchTti._10ms, baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default) \n
		Sets the processing duration. \n
			:param ttiedch: 2ms| 10ms
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.enum_scalar_to_str(ttiedch, enums.HsUpaDchTti)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:HSUPa:EAGCh:TTIEdch {param}')

	# noinspection PyTypeChecker
	def get(self, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default) -> enums.HsUpaDchTti:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:[HSUPa]:EAGCh:TTIEdch \n
		Snippet: value: enums.HsUpaDchTti = driver.source.bb.w3Gpp.bstation.channel.hsupa.eagch.ttiedch.get(baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default) \n
		Sets the processing duration. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: ttiedch: 2ms| 10ms"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:HSUPa:EAGCh:TTIEdch?')
		return Conversions.str_to_scalar_enum(response, enums.HsUpaDchTti)
