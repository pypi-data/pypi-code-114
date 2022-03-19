from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, sequencer=repcap.Sequencer.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:SEQuencer<ST>:STATe \n
		Snippet: driver.source.bb.esequencer.sequencer.state.set(state = False, sequencer = repcap.Sequencer.Default) \n
		Enables the sequencer. \n
			:param state: 1| ON| 0| OFF
			:param sequencer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sequencer')
		"""
		param = Conversions.bool_to_str(state)
		sequencer_cmd_val = self._cmd_group.get_repcap_cmd_value(sequencer, repcap.Sequencer)
		self._core.io.write(f'SOURce<HwInstance>:BB:ESEQuencer:SEQuencer{sequencer_cmd_val}:STATe {param}')

	def get(self, sequencer=repcap.Sequencer.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:SEQuencer<ST>:STATe \n
		Snippet: value: bool = driver.source.bb.esequencer.sequencer.state.get(sequencer = repcap.Sequencer.Default) \n
		Enables the sequencer. \n
			:param sequencer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sequencer')
			:return: state: 1| ON| 0| OFF"""
		sequencer_cmd_val = self._cmd_group.get_repcap_cmd_value(sequencer, repcap.Sequencer)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ESEQuencer:SEQuencer{sequencer_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
