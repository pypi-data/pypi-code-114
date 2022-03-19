from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SymbolRate:
	"""SymbolRate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbolRate", core, parent)

	def set(self, srate: enums.SymbRate, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:SRATe \n
		Snippet: driver.source.bb.w3Gpp.bstation.channel.symbolRate.set(srate = enums.SymbRate.D120k, baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default) \n
		The command sets the symbol rate of the selected channel. The value range depends on the selected channel and the
		selected slot format. The slot format determines the symbol rate (and thus the range of values for the channelization
		code) , the TFCI state and the pilot length. If the value of any one of the four parameters is changed, all the other
		parameters are adapted as necessary. In the case of enhanced channels with active channel coding, the selected channel
		coding also affects the slot format and thus the remaining parameters. If these parameters are changed, the channel
		coding type is set to user. \n
			:param srate: D7K5| D15K| D30K| D60K| D120k| D240k| D480k| D960k
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.enum_scalar_to_str(srate, enums.SymbRate)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:SRATe {param}')

	# noinspection PyTypeChecker
	def get(self, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default) -> enums.SymbRate:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:SRATe \n
		Snippet: value: enums.SymbRate = driver.source.bb.w3Gpp.bstation.channel.symbolRate.get(baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default) \n
		The command sets the symbol rate of the selected channel. The value range depends on the selected channel and the
		selected slot format. The slot format determines the symbol rate (and thus the range of values for the channelization
		code) , the TFCI state and the pilot length. If the value of any one of the four parameters is changed, all the other
		parameters are adapted as necessary. In the case of enhanced channels with active channel coding, the selected channel
		coding also affects the slot format and thus the remaining parameters. If these parameters are changed, the channel
		coding type is set to user. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: srate: D7K5| D15K| D30K| D60K| D120k| D240k| D480k| D960k"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:SRATe?')
		return Conversions.str_to_scalar_enum(response, enums.SymbRate)
