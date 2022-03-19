from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Post:
	"""Post commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("post", core, parent)

	def set(self, post_time: int, sequencer=repcap.Sequencer.Default, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:TRIGger:[SEQuencer<ST>]:OUTPut<CH>:POST \n
		Snippet: driver.source.bb.esequencer.trigger.sequencer.output.post.set(post_time = 1, sequencer = repcap.Sequencer.Default, output = repcap.Output.Default) \n
		Sets pre-marker time for PDW format variant 2. \n
			:param post_time: integer Range: 0 to 24000
			:param sequencer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sequencer')
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.decimal_value_to_str(post_time)
		sequencer_cmd_val = self._cmd_group.get_repcap_cmd_value(sequencer, repcap.Sequencer)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:ESEQuencer:TRIGger:SEQuencer{sequencer_cmd_val}:OUTPut{output_cmd_val}:POST {param}')

	def get(self, sequencer=repcap.Sequencer.Default, output=repcap.Output.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:TRIGger:[SEQuencer<ST>]:OUTPut<CH>:POST \n
		Snippet: value: int = driver.source.bb.esequencer.trigger.sequencer.output.post.get(sequencer = repcap.Sequencer.Default, output = repcap.Output.Default) \n
		Sets pre-marker time for PDW format variant 2. \n
			:param sequencer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sequencer')
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: post_time: No help available"""
		sequencer_cmd_val = self._cmd_group.get_repcap_cmd_value(sequencer, repcap.Sequencer)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ESEQuencer:TRIGger:SEQuencer{sequencer_cmd_val}:OUTPut{output_cmd_val}:POST?')
		return Conversions.str_to_int(response)
