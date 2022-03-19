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

	def set(self, mode: enums.TetraMarkMode, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:TRIGger:OUTPut<CH>:MODE \n
		Snippet: driver.source.bb.tetra.trigger.output.mode.set(mode = enums.TetraMarkMode.FSTart, output = repcap.Output.Default) \n
		Defines the signal for the selected marker output. \n
			:param mode: RESTart| SSTart| FSTart| MFSTart| HFSTart| PULSe| PATTern| RATio RESTart A marker signal is generated at the start of each ARB sequence. SSTart A marker signal is generated at the start of each slot. FSTart A marker signal is generated at the start of each frame. MFSTart A marker signal is generated at the start of each multiframe. HFSTart A marker signal is generated at the start of each hyperframe. PULSe A regular marker signal is generated. The pulse frequency is defined by entering a divider. The frequency is derived by dividing the sample rate by the divider. PATTern A marker signal that is defined by a bit pattern is generated. The pattern has a maximum length of 64 bits and is defined with the command [:SOURcehw]:BB:TETRa:TRIGger:OUTPutch:PATTern. RATio A marker signal corresponding to the Time Off / Time On specifications in the commands [:SOURcehw]:BB:TETRa:TRIGger:OUTPutch:ONTime and [:SOURcehw]:BB:TETRa:TRIGger:OUTPutch:OFFTime is generated.
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.TetraMarkMode)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:TRIGger:OUTPut{output_cmd_val}:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, output=repcap.Output.Default) -> enums.TetraMarkMode:
		"""SCPI: [SOURce<HW>]:BB:TETRa:TRIGger:OUTPut<CH>:MODE \n
		Snippet: value: enums.TetraMarkMode = driver.source.bb.tetra.trigger.output.mode.get(output = repcap.Output.Default) \n
		Defines the signal for the selected marker output. \n
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: mode: RESTart| SSTart| FSTart| MFSTart| HFSTart| PULSe| PATTern| RATio RESTart A marker signal is generated at the start of each ARB sequence. SSTart A marker signal is generated at the start of each slot. FSTart A marker signal is generated at the start of each frame. MFSTart A marker signal is generated at the start of each multiframe. HFSTart A marker signal is generated at the start of each hyperframe. PULSe A regular marker signal is generated. The pulse frequency is defined by entering a divider. The frequency is derived by dividing the sample rate by the divider. PATTern A marker signal that is defined by a bit pattern is generated. The pattern has a maximum length of 64 bits and is defined with the command [:SOURcehw]:BB:TETRa:TRIGger:OUTPutch:PATTern. RATio A marker signal corresponding to the Time Off / Time On specifications in the commands [:SOURcehw]:BB:TETRa:TRIGger:OUTPutch:ONTime and [:SOURcehw]:BB:TETRa:TRIGger:OUTPutch:OFFTime is generated."""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TETRa:TRIGger:OUTPut{output_cmd_val}:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.TetraMarkMode)
