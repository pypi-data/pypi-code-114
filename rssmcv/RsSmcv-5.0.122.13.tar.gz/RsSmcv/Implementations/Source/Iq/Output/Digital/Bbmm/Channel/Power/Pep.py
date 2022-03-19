from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pep:
	"""Pep commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pep", core, parent)

	def set(self, bbout_pep_hs: float, iqConnector=repcap.IqConnector.Default, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:BBMM<CH>:CHANnel<ST0>:POWer:PEP \n
		Snippet: driver.source.iq.output.digital.bbmm.channel.power.pep.set(bbout_pep_hs = 1.0, iqConnector = repcap.IqConnector.Default, channelNull = repcap.ChannelNull.Default) \n
		Sets the peak level of the channel of the HS digital I/Q output signal. The level is relative to full scale of 0.5 V (in
		terms of dB full scale) . \n
			:param bbout_pep_hs: float Range: -60 to 0
			:param iqConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bbmm')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.decimal_value_to_str(bbout_pep_hs)
		iqConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(iqConnector, repcap.IqConnector)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce:IQ:OUTPut:DIGital:BBMM{iqConnector_cmd_val}:CHANnel{channelNull_cmd_val}:POWer:PEP {param}')

	def get(self, iqConnector=repcap.IqConnector.Default, channelNull=repcap.ChannelNull.Default) -> float:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:BBMM<CH>:CHANnel<ST0>:POWer:PEP \n
		Snippet: value: float = driver.source.iq.output.digital.bbmm.channel.power.pep.get(iqConnector = repcap.IqConnector.Default, channelNull = repcap.ChannelNull.Default) \n
		Sets the peak level of the channel of the HS digital I/Q output signal. The level is relative to full scale of 0.5 V (in
		terms of dB full scale) . \n
			:param iqConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bbmm')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: bbout_pep_hs: float Range: -60 to 0"""
		iqConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(iqConnector, repcap.IqConnector)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce:IQ:OUTPut:DIGital:BBMM{iqConnector_cmd_val}:CHANnel{channelNull_cmd_val}:POWer:PEP?')
		return Conversions.str_to_float(response)
