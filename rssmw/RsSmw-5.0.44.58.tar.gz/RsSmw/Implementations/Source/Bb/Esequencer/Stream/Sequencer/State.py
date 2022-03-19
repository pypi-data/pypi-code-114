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

	def set(self, sequencer_state: bool, twoStreams=repcap.TwoStreams.Default, sequencer=repcap.Sequencer.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:STReam<DI>:SEQuencer<ST>:STATe \n
		Snippet: driver.source.bb.esequencer.stream.sequencer.state.set(sequencer_state = False, twoStreams = repcap.TwoStreams.Default, sequencer = repcap.Sequencer.Default) \n
		Assigns a sequencer to the selected streams. \n
			:param sequencer_state: 1| ON| 0| OFF
			:param twoStreams: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stream')
			:param sequencer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sequencer')
		"""
		param = Conversions.bool_to_str(sequencer_state)
		twoStreams_cmd_val = self._cmd_group.get_repcap_cmd_value(twoStreams, repcap.TwoStreams)
		sequencer_cmd_val = self._cmd_group.get_repcap_cmd_value(sequencer, repcap.Sequencer)
		self._core.io.write(f'SOURce<HwInstance>:BB:ESEQuencer:STReam{twoStreams_cmd_val}:SEQuencer{sequencer_cmd_val}:STATe {param}')

	def get(self, twoStreams=repcap.TwoStreams.Default, sequencer=repcap.Sequencer.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:STReam<DI>:SEQuencer<ST>:STATe \n
		Snippet: value: bool = driver.source.bb.esequencer.stream.sequencer.state.get(twoStreams = repcap.TwoStreams.Default, sequencer = repcap.Sequencer.Default) \n
		Assigns a sequencer to the selected streams. \n
			:param twoStreams: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stream')
			:param sequencer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sequencer')
			:return: sequencer_state: 1| ON| 0| OFF"""
		twoStreams_cmd_val = self._cmd_group.get_repcap_cmd_value(twoStreams, repcap.TwoStreams)
		sequencer_cmd_val = self._cmd_group.get_repcap_cmd_value(sequencer, repcap.Sequencer)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ESEQuencer:STReam{twoStreams_cmd_val}:SEQuencer{sequencer_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
