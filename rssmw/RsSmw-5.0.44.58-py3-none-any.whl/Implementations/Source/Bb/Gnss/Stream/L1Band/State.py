from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, stream=repcap.Stream.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:STReam<ST>:L1Band:[STATe] \n
		Snippet: driver.source.bb.gnss.stream.l1Band.state.set(state = False, stream = repcap.Stream.Default) \n
		Activates L1, L2 or L5 bands within the GNSS stream. Use the command, e.g. to specify, which bands are active and
		inactive per stream. See also [:SOURce<hw>]:BB:GNSS:STReam<st>:RFBand. \n
			:param state: 1| ON| 0| OFF
			:param stream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stream')
		"""
		param = Conversions.bool_to_str(state)
		stream_cmd_val = self._cmd_group.get_repcap_cmd_value(stream, repcap.Stream)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:STReam{stream_cmd_val}:L1Band:STATe {param}')

	def get(self, stream=repcap.Stream.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:STReam<ST>:L1Band:[STATe] \n
		Snippet: value: bool = driver.source.bb.gnss.stream.l1Band.state.get(stream = repcap.Stream.Default) \n
		Activates L1, L2 or L5 bands within the GNSS stream. Use the command, e.g. to specify, which bands are active and
		inactive per stream. See also [:SOURce<hw>]:BB:GNSS:STReam<st>:RFBand. \n
			:param stream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stream')
			:return: state: 1| ON| 0| OFF"""
		stream_cmd_val = self._cmd_group.get_repcap_cmd_value(stream, repcap.Stream)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:STReam{stream_cmd_val}:L1Band:STATe?')
		return Conversions.str_to_bool(response)
