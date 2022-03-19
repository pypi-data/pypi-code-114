from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sformat:
	"""Sformat commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sformat", core, parent)

	def set(self, sformat: int, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:SFORmat \n
		Snippet: driver.source.bb.w3Gpp.bstation.channel.sformat.set(sformat = 1, baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default) \n
		The command sets the slot format of the selected channel. The value range depends on the selected channel.
		The slot format determines the symbol rate (and thus the range of values for the channelization code) , the TFCI state
		and the pilot length. If the value of any one of the four parameters is changed, all the other parameters are adapted as
		necessary. In the case of enhanced channels with active channel coding, the selected channel coding also affects the slot
		format and thus the remaining parameters. If these parameters are changed, the channel coding type is set to user. \n
			:param sformat: integer Range: 0 to dynamic
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.decimal_value_to_str(sformat)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:SFORmat {param}')

	def get(self, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:SFORmat \n
		Snippet: value: int = driver.source.bb.w3Gpp.bstation.channel.sformat.get(baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default) \n
		The command sets the slot format of the selected channel. The value range depends on the selected channel.
		The slot format determines the symbol rate (and thus the range of values for the channelization code) , the TFCI state
		and the pilot length. If the value of any one of the four parameters is changed, all the other parameters are adapted as
		necessary. In the case of enhanced channels with active channel coding, the selected channel coding also affects the slot
		format and thus the remaining parameters. If these parameters are changed, the channel coding type is set to user. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: sformat: integer Range: 0 to dynamic"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:SFORmat?')
		return Conversions.str_to_int(response)
