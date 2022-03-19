from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SymbolRate:
	"""SymbolRate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbolRate", core, parent)

	def set(self, dig_iq_hs_srat_chan: float, iqConnector=repcap.IqConnector.Default, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:BBMM<CH>:CHANnel<ST0>:SRATe \n
		Snippet: driver.source.iq.output.digital.bbmm.channel.symbolRate.set(dig_iq_hs_srat_chan = 1.0, iqConnector = repcap.IqConnector.Default, channelNull = repcap.ChannelNull.Default) \n
		Sets the sample rate per channel. \n
			:param dig_iq_hs_srat_chan: float Range: 400 to max* *) max = 250E6 ('System Config Mode = Advanced') / max = 1250E6 ('System Config Mode = Standard') See also 'Supported digital interfaces depending on the system configuration'.
			:param iqConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bbmm')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.decimal_value_to_str(dig_iq_hs_srat_chan)
		iqConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(iqConnector, repcap.IqConnector)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce:IQ:OUTPut:DIGital:BBMM{iqConnector_cmd_val}:CHANnel{channelNull_cmd_val}:SRATe {param}')

	def get(self, iqConnector=repcap.IqConnector.Default, channelNull=repcap.ChannelNull.Default) -> float:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:BBMM<CH>:CHANnel<ST0>:SRATe \n
		Snippet: value: float = driver.source.iq.output.digital.bbmm.channel.symbolRate.get(iqConnector = repcap.IqConnector.Default, channelNull = repcap.ChannelNull.Default) \n
		Sets the sample rate per channel. \n
			:param iqConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bbmm')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: dig_iq_hs_srat_chan: float Range: 400 to max* *) max = 250E6 ('System Config Mode = Advanced') / max = 1250E6 ('System Config Mode = Standard') See also 'Supported digital interfaces depending on the system configuration'."""
		iqConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(iqConnector, repcap.IqConnector)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce:IQ:OUTPut:DIGital:BBMM{iqConnector_cmd_val}:CHANnel{channelNull_cmd_val}:SRATe?')
		return Conversions.str_to_float(response)
