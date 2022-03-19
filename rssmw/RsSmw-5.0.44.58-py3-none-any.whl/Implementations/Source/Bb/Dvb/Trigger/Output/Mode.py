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

	def set(self, mode: enums.DvbMarkMode, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:TRIGger:OUTPut<CH>:MODE \n
		Snippet: driver.source.bb.dvb.trigger.output.mode.set(mode = enums.DvbMarkMode.FRAMe, output = repcap.Output.Default) \n
		Defines the signal for the selected marker output. \n
			:param mode: RESTart| SFRame| SFRAMe| FRAMe| PULSe| PATTern| RATio RESTart Marks the start of every sequence length loop. Restart mode is available only for ETI data source. SFRame Marks the start of every super-frame period. FRAMe Marks the start of every frame. PULSe Generated continuously according to the frequency and frequency divider. PATTern A marker signal according to a bit pattern RATio A regular marker signal that is defined by an on/off ratio
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.DvbMarkMode)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:TRIGger:OUTPut{output_cmd_val}:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, output=repcap.Output.Default) -> enums.DvbMarkMode:
		"""SCPI: [SOURce<HW>]:BB:DVB:TRIGger:OUTPut<CH>:MODE \n
		Snippet: value: enums.DvbMarkMode = driver.source.bb.dvb.trigger.output.mode.get(output = repcap.Output.Default) \n
		Defines the signal for the selected marker output. \n
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: mode: RESTart| SFRame| SFRAMe| FRAMe| PULSe| PATTern| RATio RESTart Marks the start of every sequence length loop. Restart mode is available only for ETI data source. SFRame Marks the start of every super-frame period. FRAMe Marks the start of every frame. PULSe Generated continuously according to the frequency and frequency divider. PATTern A marker signal according to a bit pattern RATio A regular marker signal that is defined by an on/off ratio"""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:DVB:TRIGger:OUTPut{output_cmd_val}:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.DvbMarkMode)
