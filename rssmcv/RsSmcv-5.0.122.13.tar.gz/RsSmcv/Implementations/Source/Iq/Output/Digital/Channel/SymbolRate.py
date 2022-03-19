from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SymbolRate:
	"""SymbolRate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbolRate", core, parent)

	def set(self, dig_iq_hs_srat_chan: float, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:CHANnel<ST0>:SRATe \n
		Snippet: driver.source.iq.output.digital.channel.symbolRate.set(dig_iq_hs_srat_chan = 1.0, channelNull = repcap.ChannelNull.Default) \n
		Sets the sample rate of the channel of the HS digital I/Q output signal. \n
			:param dig_iq_hs_srat_chan: float Range: 400 to depends on options The maximum value depends on the connected receiving device. For more information, see data sheet.
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.decimal_value_to_str(dig_iq_hs_srat_chan)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce:IQ:OUTPut:DIGital:CHANnel{channelNull_cmd_val}:SRATe {param}')

	def get(self, channelNull=repcap.ChannelNull.Default) -> float:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:CHANnel<ST0>:SRATe \n
		Snippet: value: float = driver.source.iq.output.digital.channel.symbolRate.get(channelNull = repcap.ChannelNull.Default) \n
		Sets the sample rate of the channel of the HS digital I/Q output signal. \n
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: dig_iq_hs_srat_chan: float Range: 400 to depends on options The maximum value depends on the connected receiving device. For more information, see data sheet."""
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce:IQ:OUTPut:DIGital:CHANnel{channelNull_cmd_val}:SRATe?')
		return Conversions.str_to_float(response)
