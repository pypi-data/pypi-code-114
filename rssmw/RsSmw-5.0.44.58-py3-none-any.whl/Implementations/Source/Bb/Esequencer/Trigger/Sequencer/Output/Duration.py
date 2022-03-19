from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Duration:
	"""Duration commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("duration", core, parent)

	def set(self, duration: int, sequencer=repcap.Sequencer.Default, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:TRIGger:[SEQuencer<ST>]:OUTPut<CH>:DURation \n
		Snippet: driver.source.bb.esequencer.trigger.sequencer.output.duration.set(duration = 1, sequencer = repcap.Sequencer.Default, output = repcap.Output.Default) \n
		Sets the duration of the restart marker signal, or the signal defined in the sequence list. \n
			:param duration: integer Range: 1 to 65536
			:param sequencer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sequencer')
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.decimal_value_to_str(duration)
		sequencer_cmd_val = self._cmd_group.get_repcap_cmd_value(sequencer, repcap.Sequencer)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:ESEQuencer:TRIGger:SEQuencer{sequencer_cmd_val}:OUTPut{output_cmd_val}:DURation {param}')

	def get(self, sequencer=repcap.Sequencer.Default, output=repcap.Output.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:TRIGger:[SEQuencer<ST>]:OUTPut<CH>:DURation \n
		Snippet: value: int = driver.source.bb.esequencer.trigger.sequencer.output.duration.get(sequencer = repcap.Sequencer.Default, output = repcap.Output.Default) \n
		Sets the duration of the restart marker signal, or the signal defined in the sequence list. \n
			:param sequencer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sequencer')
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: duration: integer Range: 1 to 65536"""
		sequencer_cmd_val = self._cmd_group.get_repcap_cmd_value(sequencer, repcap.Sequencer)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ESEQuencer:TRIGger:SEQuencer{sequencer_cmd_val}:OUTPut{output_cmd_val}:DURation?')
		return Conversions.str_to_int(response)
