from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Offset:
	"""Offset commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def set(self, offset: float, channel=repcap.Channel.Default) -> None:
		"""SCPI: SENSe<CH>:[POWer]:OFFSet \n
		Snippet: driver.sense.power.offset.set(offset = 1.0, channel = repcap.Channel.Default) \n
		Sets a level offset which is added to the measured level value after activation with command method RsSmw.Sense.Power.
		Offset.State.set. The level offset allows, e.g. to consider an attenuator in the signal path. \n
			:param offset: float Range: -100.0 to 100.0, Unit: dB
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sense')
		"""
		param = Conversions.decimal_value_to_str(offset)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		self._core.io.write(f'SENSe{channel_cmd_val}:POWer:OFFSet {param}')

	def get(self, channel=repcap.Channel.Default) -> float:
		"""SCPI: SENSe<CH>:[POWer]:OFFSet \n
		Snippet: value: float = driver.sense.power.offset.get(channel = repcap.Channel.Default) \n
		Sets a level offset which is added to the measured level value after activation with command method RsSmw.Sense.Power.
		Offset.State.set. The level offset allows, e.g. to consider an attenuator in the signal path. \n
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sense')
			:return: offset: float Range: -100.0 to 100.0, Unit: dB"""
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		response = self._core.io.query_str(f'SENSe{channel_cmd_val}:POWer:OFFSet?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Offset':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Offset(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
