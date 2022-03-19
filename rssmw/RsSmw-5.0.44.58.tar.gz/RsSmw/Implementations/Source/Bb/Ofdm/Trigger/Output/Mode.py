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

	def set(self, mark_mode: enums.MarkMode, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:TRIGger:OUTPut<CH>:MODE \n
		Snippet: driver.source.bb.ofdm.trigger.output.mode.set(mark_mode = enums.MarkMode.RESTart, output = repcap.Output.Default) \n
		Defines the signal for the selected marker output. \n
			:param mark_mode: RESTart
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.enum_scalar_to_str(mark_mode, enums.MarkMode)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:TRIGger:OUTPut{output_cmd_val}:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, output=repcap.Output.Default) -> enums.MarkMode:
		"""SCPI: [SOURce<HW>]:BB:OFDM:TRIGger:OUTPut<CH>:MODE \n
		Snippet: value: enums.MarkMode = driver.source.bb.ofdm.trigger.output.mode.get(output = repcap.Output.Default) \n
		Defines the signal for the selected marker output. \n
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: mark_mode: RESTart"""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:OFDM:TRIGger:OUTPut{output_cmd_val}:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.MarkMode)
