from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Plength:
	"""Plength commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("plength", core, parent)

	def set(self, plength: enums.PilLen, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:DPCCh:PLENgth \n
		Snippet: driver.source.bb.w3Gpp.bstation.channel.dpcch.plength.set(plength = enums.PilLen.BIT0, baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default) \n
		Sets the length of the pilot fields. The range of values for this parameter depends on the channel type and the symbol
		rate. The slot format determines the symbol rate (and thus the range of values for the channelization code) , the TFCI
		state and the pilot length. If the value of any one of the four parameters is changed, all the other parameters are
		adapted as necessary. In the case of enhanced channels with active channel coding, the selected channel coding also
		affects the slot format and thus the remaining parameters. If these parameters are changed, the channel coding type is
		set to user. \n
			:param plength: BIT2| BIT4| BIT8| BIT16| BIT0
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.enum_scalar_to_str(plength, enums.PilLen)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:DPCCh:PLENgth {param}')

	# noinspection PyTypeChecker
	def get(self, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default) -> enums.PilLen:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:DPCCh:PLENgth \n
		Snippet: value: enums.PilLen = driver.source.bb.w3Gpp.bstation.channel.dpcch.plength.get(baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default) \n
		Sets the length of the pilot fields. The range of values for this parameter depends on the channel type and the symbol
		rate. The slot format determines the symbol rate (and thus the range of values for the channelization code) , the TFCI
		state and the pilot length. If the value of any one of the four parameters is changed, all the other parameters are
		adapted as necessary. In the case of enhanced channels with active channel coding, the selected channel coding also
		affects the slot format and thus the remaining parameters. If these parameters are changed, the channel coding type is
		set to user. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: plength: BIT2| BIT4| BIT8| BIT16| BIT0"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:DPCCh:PLENgth?')
		return Conversions.str_to_scalar_enum(response, enums.PilLen)
