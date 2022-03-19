from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, channel=repcap.Channel.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:DTTest:TABLe:SHORt:SET<CH>:STATe \n
		Snippet: driver.source.bb.btooth.dtTest.table.short.set.state.set(state = False, channel = repcap.Channel.Default) \n
		Activates the corresponding parameter set in the short table. If a set deactivated, its parameters are skipped in the
		sequence. Instead, the next active set is used. For EDR packets, each set applies to 20 packets. \n
			:param state: 1| ON| 0| OFF
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Set')
		"""
		param = Conversions.bool_to_str(state)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:DTTest:TABLe:SHORt:SET{channel_cmd_val}:STATe {param}')

	def get(self, channel=repcap.Channel.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:DTTest:TABLe:SHORt:SET<CH>:STATe \n
		Snippet: value: bool = driver.source.bb.btooth.dtTest.table.short.set.state.get(channel = repcap.Channel.Default) \n
		Activates the corresponding parameter set in the short table. If a set deactivated, its parameters are skipped in the
		sequence. Instead, the next active set is used. For EDR packets, each set applies to 20 packets. \n
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Set')
			:return: state: 1| ON| 0| OFF"""
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:BTOoth:DTTest:TABLe:SHORt:SET{channel_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
