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

	def set(self, mode: enums.Cdma2KmarkMode, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:TRIGger:OUTPut<CH>:MODE \n
		Snippet: driver.source.bb.c2K.trigger.output.mode.set(mode = enums.Cdma2KmarkMode.CSPeriod, output = repcap.Output.Default) \n
		Defines the signal for the selected marker output. \n
			:param mode: PCGRoup| RFRame| SCFRame| SFRame| ESECond| CSPeriod| RATio| USER Marker signal that marks: PCGRoup The start of each power control group (every 1.25 ms) . RFRame Every 20 ms (traffic channel clock) . SCFRame The start of each sync channel frame (every 26.6 ms) . SFRame Every 80 ms (super frame clock) . ESECond Every 2 s (even second mark) . CSPeriod The start of each arbitrary waveform sequence RATio Off / On times USER The beginning of every user-defined period
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.Cdma2KmarkMode)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:TRIGger:OUTPut{output_cmd_val}:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, output=repcap.Output.Default) -> enums.Cdma2KmarkMode:
		"""SCPI: [SOURce<HW>]:BB:C2K:TRIGger:OUTPut<CH>:MODE \n
		Snippet: value: enums.Cdma2KmarkMode = driver.source.bb.c2K.trigger.output.mode.get(output = repcap.Output.Default) \n
		Defines the signal for the selected marker output. \n
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: mode: PCGRoup| RFRame| SCFRame| SFRame| ESECond| CSPeriod| RATio| USER Marker signal that marks: PCGRoup The start of each power control group (every 1.25 ms) . RFRame Every 20 ms (traffic channel clock) . SCFRame The start of each sync channel frame (every 26.6 ms) . SFRame Every 80 ms (super frame clock) . ESECond Every 2 s (even second mark) . CSPeriod The start of each arbitrary waveform sequence RATio Off / On times USER The beginning of every user-defined period"""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:C2K:TRIGger:OUTPut{output_cmd_val}:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.Cdma2KmarkMode)
