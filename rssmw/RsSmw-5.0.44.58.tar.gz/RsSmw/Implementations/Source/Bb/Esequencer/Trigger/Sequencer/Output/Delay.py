from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Delay:
	"""Delay commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("delay", core, parent)

	def set(self, delay: float, sequencer=repcap.Sequencer.Default, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:TRIGger:[SEQuencer<ST>]:OUTPut<CH>:DELay \n
		Snippet: driver.source.bb.esequencer.trigger.sequencer.output.delay.set(delay = 1.0, sequencer = repcap.Sequencer.Default, output = repcap.Output.Default) \n
		Defines the delay between the signal on the marker outputs and the start of the signals. \n
			:param delay: float Range: 0 (R&S SMWK501/-K502/-K503/-K504) /6 (R&S SMW-K315) to 16777215
			:param sequencer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sequencer')
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.decimal_value_to_str(delay)
		sequencer_cmd_val = self._cmd_group.get_repcap_cmd_value(sequencer, repcap.Sequencer)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:ESEQuencer:TRIGger:SEQuencer{sequencer_cmd_val}:OUTPut{output_cmd_val}:DELay {param}')

	def get(self, sequencer=repcap.Sequencer.Default, output=repcap.Output.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:TRIGger:[SEQuencer<ST>]:OUTPut<CH>:DELay \n
		Snippet: value: float = driver.source.bb.esequencer.trigger.sequencer.output.delay.get(sequencer = repcap.Sequencer.Default, output = repcap.Output.Default) \n
		Defines the delay between the signal on the marker outputs and the start of the signals. \n
			:param sequencer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sequencer')
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: delay: float Range: 0 (R&S SMWK501/-K502/-K503/-K504) /6 (R&S SMW-K315) to 16777215"""
		sequencer_cmd_val = self._cmd_group.get_repcap_cmd_value(sequencer, repcap.Sequencer)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ESEQuencer:TRIGger:SEQuencer{sequencer_cmd_val}:OUTPut{output_cmd_val}:DELay?')
		return Conversions.str_to_float(response)
