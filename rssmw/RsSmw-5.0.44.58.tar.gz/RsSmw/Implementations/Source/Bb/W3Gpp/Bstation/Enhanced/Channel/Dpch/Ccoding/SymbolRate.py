from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SymbolRate:
	"""SymbolRate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbolRate", core, parent)

	# noinspection PyTypeChecker
	def get(self, channelNull=repcap.ChannelNull.Default) -> enums.SymbRate:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation:ENHanced:CHANnel<CH0>:DPCH:CCODing:SRATe \n
		Snippet: value: enums.SymbRate = driver.source.bb.w3Gpp.bstation.enhanced.channel.dpch.ccoding.symbolRate.get(channelNull = repcap.ChannelNull.Default) \n
		The command queries the symbol rate.
		The symbol rate depends on the selected slot format
		([:SOURce<hw>]:BB:W3GPp:BSTation:ENHanced:CHANnel<ch0>:DPCH:CCODing:SFORmat) , and if the slot format changes, this
		changes automatically as well. \n
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: srate: D7K5| D15K| D30K| D60K| D120k| D240k| D480k| D960k| D1920k| D2880k| D3840k| D4800k| D5760k| D2X1920K| D2X960K2X1920K"""
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation:ENHanced:CHANnel{channelNull_cmd_val}:DPCH:CCODing:SRATe?')
		return Conversions.str_to_scalar_enum(response, enums.SymbRate)
