from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pre:
	"""Pre commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pre", core, parent)

	def set(self, pre_time: int, sequencer=repcap.Sequencer.Default, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:TRIGger:[SEQuencer<ST>]:OUTPut<CH>:PRE \n
		Snippet: driver.source.bb.esequencer.trigger.sequencer.output.pre.set(pre_time = 1, sequencer = repcap.Sequencer.Default, output = repcap.Output.Default) \n
		Sets pre-marker time for PDW format variant 2. \n
			:param pre_time: integer Range: 0 to 24000
			:param sequencer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sequencer')
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.decimal_value_to_str(pre_time)
		sequencer_cmd_val = self._cmd_group.get_repcap_cmd_value(sequencer, repcap.Sequencer)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:ESEQuencer:TRIGger:SEQuencer{sequencer_cmd_val}:OUTPut{output_cmd_val}:PRE {param}')

	def get(self, sequencer=repcap.Sequencer.Default, output=repcap.Output.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:TRIGger:[SEQuencer<ST>]:OUTPut<CH>:PRE \n
		Snippet: value: int = driver.source.bb.esequencer.trigger.sequencer.output.pre.get(sequencer = repcap.Sequencer.Default, output = repcap.Output.Default) \n
		Sets pre-marker time for PDW format variant 2. \n
			:param sequencer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sequencer')
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: pre_time: integer Range: 0 to 24000"""
		sequencer_cmd_val = self._cmd_group.get_repcap_cmd_value(sequencer, repcap.Sequencer)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ESEQuencer:TRIGger:SEQuencer{sequencer_cmd_val}:OUTPut{output_cmd_val}:PRE?')
		return Conversions.str_to_int(response)
