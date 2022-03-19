from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	def set(self, power: float, mobileStation=repcap.MobileStation.Default, channel=repcap.Channel.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:MSTation<ST>:CHANnel<CH>:POWer \n
		Snippet: driver.source.bb.c2K.mstation.channel.power.set(power = 1.0, mobileStation = repcap.MobileStation.Default, channel = repcap.Channel.Default) \n
		Sets the channel power relative to the powers of the other channels. This setting also determines the starting power of
		the channel for Misuse Output Power Control. With the command [:SOURce<hw>]:BB:C2K:POWer:ADJust, the power of all the
		activated channels is adapted so that the total power corresponds to 0 dB. This does not change the power ratio among the
		individual channels. For the traffic channels, this value is specific for the selected radio configuration. \n
			:param power: float Range: -80 to 0
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Channel')
		"""
		param = Conversions.decimal_value_to_str(power)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:MSTation{mobileStation_cmd_val}:CHANnel{channel_cmd_val}:POWer {param}')

	def get(self, mobileStation=repcap.MobileStation.Default, channel=repcap.Channel.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:C2K:MSTation<ST>:CHANnel<CH>:POWer \n
		Snippet: value: float = driver.source.bb.c2K.mstation.channel.power.get(mobileStation = repcap.MobileStation.Default, channel = repcap.Channel.Default) \n
		Sets the channel power relative to the powers of the other channels. This setting also determines the starting power of
		the channel for Misuse Output Power Control. With the command [:SOURce<hw>]:BB:C2K:POWer:ADJust, the power of all the
		activated channels is adapted so that the total power corresponds to 0 dB. This does not change the power ratio among the
		individual channels. For the traffic channels, this value is specific for the selected radio configuration. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Channel')
			:return: power: float Range: -80 to 0"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:C2K:MSTation{mobileStation_cmd_val}:CHANnel{channel_cmd_val}:POWer?')
		return Conversions.str_to_float(response)
