from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, type_py: enums.ChanTypeDn, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:TYPE \n
		Snippet: driver.source.bb.w3Gpp.bstation.channel.typePy.set(type_py = enums.ChanTypeDn.AICH, baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default) \n
		Sets the channel type. \n
			:param type_py: PCPich| SCPich| PSCH| SSCH| PCCPch| SCCPch| PICH| APAich| AICH| PDSCh| DPCCh| DPCH| HSSCch| HSQPsk| HSQam| HS64Qam| HSMimo| EAGCh| ERGCh| EHICh| FDPCh| HS16Qam The channels types of CHANnel0 to CHANnel8 are predefined. For the remaining channels, you can select a channel type from the relevant standard channels and the high-speed channels
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.ChanTypeDn)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default) -> enums.ChanTypeDn:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:TYPE \n
		Snippet: value: enums.ChanTypeDn = driver.source.bb.w3Gpp.bstation.channel.typePy.get(baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default) \n
		Sets the channel type. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: type_py: PCPich| SCPich| PSCH| SSCH| PCCPch| SCCPch| PICH| APAich| AICH| PDSCh| DPCCh| DPCH| HSSCch| HSQPsk| HSQam| HS64Qam| HSMimo| EAGCh| ERGCh| EHICh| FDPCh| HS16Qam The channels types of CHANnel0 to CHANnel8 are predefined. For the remaining channels, you can select a channel type from the relevant standard channels and the high-speed channels"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.ChanTypeDn)
