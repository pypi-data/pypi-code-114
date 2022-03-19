from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.ExtSeqMarkMode, sequencer=repcap.Sequencer.Default, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:TRIGger:[SEQuencer<ST>]:OUTPut<CH>:MODE \n
		Snippet: driver.source.bb.esequencer.trigger.sequencer.output.mode.set(mode = enums.ExtSeqMarkMode.ADW, sequencer = repcap.Sequencer.Default, output = repcap.Output.Default) \n
		Defines the signal for the selected marker output. \n
			:param mode: UNCHanged| STARt| ENTRy| PULSe| PDW UNCHanged Provides the marker signal defined in the waveform. ENTRy Generates a marker signal when enabled in the loaded list file. The [:SOURcehw]:BB:ESEQuencer:TRIGger[:SEQuencerst]:OUTPutch:DURation determines how long the marker signal is high. STARt Generates a marker signal at each sequence start. The [:SOURcehw]:BB:ESEQuencer:TRIGger[:SEQuencerst]:OUTPutch:DURation defines the length of the marker signal. PULSe Creates a marker signal with the same width as the pulse width. PDW Option: R&S SMW-K502: uses the marker signals as defined in the R&S Pulse Sequencer. Option: R&S SMW-K503: creates marker signals according to the marker bit field inside the PDW header.
			:param sequencer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sequencer')
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.ExtSeqMarkMode)
		sequencer_cmd_val = self._cmd_group.get_repcap_cmd_value(sequencer, repcap.Sequencer)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:ESEQuencer:TRIGger:SEQuencer{sequencer_cmd_val}:OUTPut{output_cmd_val}:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, sequencer=repcap.Sequencer.Default, output=repcap.Output.Default) -> enums.ExtSeqMarkMode:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:TRIGger:[SEQuencer<ST>]:OUTPut<CH>:MODE \n
		Snippet: value: enums.ExtSeqMarkMode = driver.source.bb.esequencer.trigger.sequencer.output.mode.get(sequencer = repcap.Sequencer.Default, output = repcap.Output.Default) \n
		Defines the signal for the selected marker output. \n
			:param sequencer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sequencer')
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: mode: UNCHanged| STARt| ENTRy| PULSe| PDW UNCHanged Provides the marker signal defined in the waveform. ENTRy Generates a marker signal when enabled in the loaded list file. The [:SOURcehw]:BB:ESEQuencer:TRIGger[:SEQuencerst]:OUTPutch:DURation determines how long the marker signal is high. STARt Generates a marker signal at each sequence start. The [:SOURcehw]:BB:ESEQuencer:TRIGger[:SEQuencerst]:OUTPutch:DURation defines the length of the marker signal. PULSe Creates a marker signal with the same width as the pulse width. PDW Option: R&S SMW-K502: uses the marker signals as defined in the R&S Pulse Sequencer. Option: R&S SMW-K503: creates marker signals according to the marker bit field inside the PDW header."""
		sequencer_cmd_val = self._cmd_group.get_repcap_cmd_value(sequencer, repcap.Sequencer)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ESEQuencer:TRIGger:SEQuencer{sequencer_cmd_val}:OUTPut{output_cmd_val}:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.ExtSeqMarkMode)
