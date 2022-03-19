from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	def set(self, frequency: float, channel=repcap.Channel.Default) -> None:
		"""SCPI: SENSe<CH>:[POWer]:FREQuency \n
		Snippet: driver.sense.power.frequency.set(frequency = 1.0, channel = repcap.Channel.Default) \n
		Sets the RF frequency of the signal, if signal source 'USER' is selected (method RsSmcv.Sense.Power.Source.set) . \n
			:param frequency: float
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sense')
		"""
		param = Conversions.decimal_value_to_str(frequency)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		self._core.io.write(f'SENSe{channel_cmd_val}:POWer:FREQuency {param}')

	def get(self, channel=repcap.Channel.Default) -> float:
		"""SCPI: SENSe<CH>:[POWer]:FREQuency \n
		Snippet: value: float = driver.sense.power.frequency.get(channel = repcap.Channel.Default) \n
		Sets the RF frequency of the signal, if signal source 'USER' is selected (method RsSmcv.Sense.Power.Source.set) . \n
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sense')
			:return: frequency: float"""
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		response = self._core.io.query_str(f'SENSe{channel_cmd_val}:POWer:FREQuency?')
		return Conversions.str_to_float(response)
