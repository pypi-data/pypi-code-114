from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.PowContMode, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation:ENHanced:CHANnel<CH0>:DPCH:DPControl:MODE \n
		Snippet: driver.source.bb.w3Gpp.bstation.enhanced.channel.dpch.dpControl.mode.set(mode = enums.PowContMode.EXTernal, channelNull = repcap.ChannelNull.Default) \n
		Selects the control signal source for Dynamic Power Control. \n
			:param mode: TPC| MANual | EXTernal
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.PowContMode)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation:ENHanced:CHANnel{channelNull_cmd_val}:DPCH:DPControl:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, channelNull=repcap.ChannelNull.Default) -> enums.PowContMode:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation:ENHanced:CHANnel<CH0>:DPCH:DPControl:MODE \n
		Snippet: value: enums.PowContMode = driver.source.bb.w3Gpp.bstation.enhanced.channel.dpch.dpControl.mode.get(channelNull = repcap.ChannelNull.Default) \n
		Selects the control signal source for Dynamic Power Control. \n
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: mode: TPC| MANual | EXTernal"""
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation:ENHanced:CHANnel{channelNull_cmd_val}:DPCH:DPControl:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.PowContMode)
