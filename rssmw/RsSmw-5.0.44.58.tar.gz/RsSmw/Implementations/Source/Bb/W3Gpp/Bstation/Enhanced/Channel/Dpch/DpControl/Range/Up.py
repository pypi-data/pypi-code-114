from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Up:
	"""Up commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("up", core, parent)

	def set(self, up: float, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:ENHanced:CHANnel<CH0>:DPCH:DPControl:RANGe:UP \n
		Snippet: driver.source.bb.w3Gpp.bstation.enhanced.channel.dpch.dpControl.range.up.set(up = 1.0, baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default) \n
		The command selects the dynamic range for ranging down the channel power. \n
			:param up: float Range: 0 to 60, Unit: dB
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.decimal_value_to_str(up)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:ENHanced:CHANnel{channelNull_cmd_val}:DPCH:DPControl:RANGe:UP {param}')

	def get(self, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:ENHanced:CHANnel<CH0>:DPCH:DPControl:RANGe:UP \n
		Snippet: value: float = driver.source.bb.w3Gpp.bstation.enhanced.channel.dpch.dpControl.range.up.get(baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default) \n
		The command selects the dynamic range for ranging down the channel power. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: up: No help available"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:ENHanced:CHANnel{channelNull_cmd_val}:DPCH:DPControl:RANGe:UP?')
		return Conversions.str_to_float(response)
