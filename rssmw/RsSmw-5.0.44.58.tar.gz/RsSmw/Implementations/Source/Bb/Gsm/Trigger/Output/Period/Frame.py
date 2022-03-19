from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frame:
	"""Frame commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frame", core, parent)

	def set(self, frame: int, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GSM:TRIGger:OUTPut<CH>:PERiod:[FRAMe] \n
		Snippet: driver.source.bb.gsm.trigger.output.period.frame.set(frame = 1, output = repcap.Output.Default) \n
		Sets the repetition rate for the frame clock at the marker outputs. \n
			:param frame: integer Range: 1 to 67108863
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.decimal_value_to_str(frame)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:GSM:TRIGger:OUTPut{output_cmd_val}:PERiod:FRAMe {param}')

	def get(self, output=repcap.Output.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:GSM:TRIGger:OUTPut<CH>:PERiod:[FRAMe] \n
		Snippet: value: int = driver.source.bb.gsm.trigger.output.period.frame.get(output = repcap.Output.Default) \n
		Sets the repetition rate for the frame clock at the marker outputs. \n
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: frame: integer Range: 1 to 67108863"""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GSM:TRIGger:OUTPut{output_cmd_val}:PERiod:FRAMe?')
		return Conversions.str_to_int(response)
