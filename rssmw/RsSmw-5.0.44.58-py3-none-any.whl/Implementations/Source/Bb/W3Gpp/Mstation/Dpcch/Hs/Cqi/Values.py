from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Values:
	"""Values commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("values", core, parent)

	def set(self, values: int, mobileStation=repcap.MobileStation.Default, channelQualId=repcap.ChannelQualId.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:CQI<CH>:[VALues] \n
		Snippet: driver.source.bb.w3Gpp.mstation.dpcch.hs.cqi.values.set(values = 1, mobileStation = repcap.MobileStation.Default, channelQualId = repcap.ChannelQualId.Default) \n
		Sets the values of the CQI sequence.
		The length of the CQI sequence is defined with command [:SOURce<hw>]:BB:W3GPp:MSTation<st>:DPCCh:HS:CQI:PLENgth.
		The pattern is generated cyclically. \n
			:param values: integer Value -1 means that no CQI is sent (DTX - Discontinuous Transmission) . Range: -1 to 30
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:param channelQualId: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cqi')
		"""
		param = Conversions.decimal_value_to_str(values)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		channelQualId_cmd_val = self._cmd_group.get_repcap_cmd_value(channelQualId, repcap.ChannelQualId)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:CQI{channelQualId_cmd_val}:VALues {param}')

	def get(self, mobileStation=repcap.MobileStation.Default, channelQualId=repcap.ChannelQualId.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:CQI<CH>:[VALues] \n
		Snippet: value: int = driver.source.bb.w3Gpp.mstation.dpcch.hs.cqi.values.get(mobileStation = repcap.MobileStation.Default, channelQualId = repcap.ChannelQualId.Default) \n
		Sets the values of the CQI sequence.
		The length of the CQI sequence is defined with command [:SOURce<hw>]:BB:W3GPp:MSTation<st>:DPCCh:HS:CQI:PLENgth.
		The pattern is generated cyclically. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:param channelQualId: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cqi')
			:return: values: integer Value -1 means that no CQI is sent (DTX - Discontinuous Transmission) . Range: -1 to 30"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		channelQualId_cmd_val = self._cmd_group.get_repcap_cmd_value(channelQualId, repcap.ChannelQualId)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:CQI{channelQualId_cmd_val}:VALues?')
		return Conversions.str_to_int(response)
