from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Level:
	"""Level commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)

	def set(self, bbout_hs_level: float, iqConnector=repcap.IqConnector.Default, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:BBMM<CH>:CHANnel<ST0>:POWer:LEVel \n
		Snippet: driver.source.iq.output.digital.bbmm.channel.power.level.set(bbout_hs_level = 1.0, iqConnector = repcap.IqConnector.Default, channelNull = repcap.ChannelNull.Default) \n
		Enters the RMS level of the output signal. \n
			:param bbout_hs_level: float Range: -80 to 0
			:param iqConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bbmm')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.decimal_value_to_str(bbout_hs_level)
		iqConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(iqConnector, repcap.IqConnector)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce:IQ:OUTPut:DIGital:BBMM{iqConnector_cmd_val}:CHANnel{channelNull_cmd_val}:POWer:LEVel {param}')

	def get(self, iqConnector=repcap.IqConnector.Default, channelNull=repcap.ChannelNull.Default) -> float:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:BBMM<CH>:CHANnel<ST0>:POWer:LEVel \n
		Snippet: value: float = driver.source.iq.output.digital.bbmm.channel.power.level.get(iqConnector = repcap.IqConnector.Default, channelNull = repcap.ChannelNull.Default) \n
		Enters the RMS level of the output signal. \n
			:param iqConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bbmm')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: bbout_hs_level: No help available"""
		iqConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(iqConnector, repcap.IqConnector)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce:IQ:OUTPut:DIGital:BBMM{iqConnector_cmd_val}:CHANnel{channelNull_cmd_val}:POWer:LEVel?')
		return Conversions.str_to_float(response)
