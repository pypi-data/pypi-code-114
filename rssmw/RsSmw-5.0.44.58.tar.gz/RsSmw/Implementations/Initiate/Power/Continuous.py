from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Continuous:
	"""Continuous commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("continuous", core, parent)

	def set(self, continuous: bool, channel=repcap.Channel.Default) -> None:
		"""SCPI: INITiate<HW>:[POWer]:CONTinuous \n
		Snippet: driver.initiate.power.continuous.set(continuous = False, channel = repcap.Channel.Default) \n
		Switches the local state of the continuous power measurement by R&S NRP power sensors on and off. Switching off local
		state enhances the measurement performance during remote control. The remote measurement is triggered with method RsSmw.
		Read.Power.get_) . This command also returns the measurement results. The local state is not affected, measurement
		results can be retrieved with local state on or off. \n
			:param continuous: 0| 1| OFF| ON
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Initiate')
		"""
		param = Conversions.bool_to_str(continuous)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		self._core.io.write(f'INITiate{channel_cmd_val}:POWer:CONTinuous {param}')

	def get(self, channel=repcap.Channel.Default) -> bool:
		"""SCPI: INITiate<HW>:[POWer]:CONTinuous \n
		Snippet: value: bool = driver.initiate.power.continuous.get(channel = repcap.Channel.Default) \n
		Switches the local state of the continuous power measurement by R&S NRP power sensors on and off. Switching off local
		state enhances the measurement performance during remote control. The remote measurement is triggered with method RsSmw.
		Read.Power.get_) . This command also returns the measurement results. The local state is not affected, measurement
		results can be retrieved with local state on or off. \n
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Initiate')
			:return: continuous: 0| 1| OFF| ON"""
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		response = self._core.io.query_str(f'INITiate{channel_cmd_val}:POWer:CONTinuous?')
		return Conversions.str_to_bool(response)
