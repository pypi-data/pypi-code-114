from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class External:
	"""External commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("external", core, parent)

	def set(self, external: float, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation:ENHanced:CHANnel<CH0>:DPCH:DPControl:STEP:[EXTernal] \n
		Snippet: driver.source.bb.w3Gpp.bstation.enhanced.channel.dpch.dpControl.step.external.set(external = 1.0, channelNull = repcap.ChannelNull.Default) \n
		This command sets step width by which – with Dynamic Power Control being switched on - the channel power of the selected
		enhanced channel is increased or decreased. \n
			:param external: float Range: 0.5 to 6, Unit: dB
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.decimal_value_to_str(external)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation:ENHanced:CHANnel{channelNull_cmd_val}:DPCH:DPControl:STEP:EXTernal {param}')

	def get(self, channelNull=repcap.ChannelNull.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation:ENHanced:CHANnel<CH0>:DPCH:DPControl:STEP:[EXTernal] \n
		Snippet: value: float = driver.source.bb.w3Gpp.bstation.enhanced.channel.dpch.dpControl.step.external.get(channelNull = repcap.ChannelNull.Default) \n
		This command sets step width by which – with Dynamic Power Control being switched on - the channel power of the selected
		enhanced channel is increased or decreased. \n
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: external: float Range: 0.5 to 6, Unit: dB"""
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation:ENHanced:CHANnel{channelNull_cmd_val}:DPCH:DPControl:STEP:EXTernal?')
		return Conversions.str_to_float(response)
