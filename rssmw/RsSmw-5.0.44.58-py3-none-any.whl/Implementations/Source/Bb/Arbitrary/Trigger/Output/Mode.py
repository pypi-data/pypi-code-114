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

	def set(self, mode: enums.TriggerMarkModeA, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:TRIGger:OUTPut<CH>:MODE \n
		Snippet: driver.source.bb.arbitrary.trigger.output.mode.set(mode = enums.TriggerMarkModeA.PATTern, output = repcap.Output.Default) \n
		Defines the signal for the selected marker output. For detailed description of the regular marker modes, refer to 'Marker
		modes'. \n
			:param mode: UNCHanged| RESTart| PULSe| PATTern| RATio UNCHanged A marker signal as defined in the waveform file (tag 'marker mode x') is generated.
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.TriggerMarkModeA)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:TRIGger:OUTPut{output_cmd_val}:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, output=repcap.Output.Default) -> enums.TriggerMarkModeA:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:TRIGger:OUTPut<CH>:MODE \n
		Snippet: value: enums.TriggerMarkModeA = driver.source.bb.arbitrary.trigger.output.mode.get(output = repcap.Output.Default) \n
		Defines the signal for the selected marker output. For detailed description of the regular marker modes, refer to 'Marker
		modes'. \n
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: mode: UNCHanged| RESTart| PULSe| PATTern| RATio UNCHanged A marker signal as defined in the waveform file (tag 'marker mode x') is generated."""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ARBitrary:TRIGger:OUTPut{output_cmd_val}:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.TriggerMarkModeA)
