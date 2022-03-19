from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.BtoMarkMode, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:TRIGger:OUTPut<CH>:MODE \n
		Snippet: driver.source.bb.btooth.trigger.output.mode.set(mode = enums.BtoMarkMode.ACTive, output = repcap.Output.Default) \n
		Defines the signal for the selected marker output. \n
			:param mode: RESTart| STARt| ACTive| PULSe| PATTern| RATio | IACTive RESTart A marker signal is generated at the start of each signal sequence. STARt A marker signal is generated at the start of each event/frame. ACTive The marker masks the active part of the event/frame. At the start of each burst, the marker signal changes to high. It changes back to low after the end of each burst. PULSe A regular marker signal is generated. The clock frequency is defined by entering a divider. The frequency is derived by dividing the symbol rate by the divider. The input box for divider opens when 'Pulse' is selected, and the resulting pulse frequency is displayed below. PATTern A marker signal that is defined by a bit pattern is generated. The pattern has a maximum length of 32 bits and is defined in an input field which opens when pattern is selected. RATio A regular marker signal corresponding to the'Time Off' / 'Time On' specifications in the commands SOURce1:BB:BTO:TRIGger:OUTPut:OFFTime and SOURce1:BB:BTO:TRIGger:OUTPut:ONTime is generated. IACTive The marker masks the inactive part of the event/frame. At the start of each burst, the marker signal changes to low. It changes back to high after the end of each burst.
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.BtoMarkMode)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:TRIGger:OUTPut{output_cmd_val}:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, output=repcap.Output.Default) -> enums.BtoMarkMode:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:TRIGger:OUTPut<CH>:MODE \n
		Snippet: value: enums.BtoMarkMode = driver.source.bb.btooth.trigger.output.mode.get(output = repcap.Output.Default) \n
		Defines the signal for the selected marker output. \n
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: mode: RESTart| STARt| ACTive| PULSe| PATTern| RATio | IACTive RESTart A marker signal is generated at the start of each signal sequence. STARt A marker signal is generated at the start of each event/frame. ACTive The marker masks the active part of the event/frame. At the start of each burst, the marker signal changes to high. It changes back to low after the end of each burst. PULSe A regular marker signal is generated. The clock frequency is defined by entering a divider. The frequency is derived by dividing the symbol rate by the divider. The input box for divider opens when 'Pulse' is selected, and the resulting pulse frequency is displayed below. PATTern A marker signal that is defined by a bit pattern is generated. The pattern has a maximum length of 32 bits and is defined in an input field which opens when pattern is selected. RATio A regular marker signal corresponding to the'Time Off' / 'Time On' specifications in the commands SOURce1:BB:BTO:TRIGger:OUTPut:OFFTime and SOURce1:BB:BTO:TRIGger:OUTPut:ONTime is generated. IACTive The marker masks the inactive part of the event/frame. At the start of each burst, the marker signal changes to low. It changes back to high after the end of each burst."""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:BTOoth:TRIGger:OUTPut{output_cmd_val}:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.BtoMarkMode)
