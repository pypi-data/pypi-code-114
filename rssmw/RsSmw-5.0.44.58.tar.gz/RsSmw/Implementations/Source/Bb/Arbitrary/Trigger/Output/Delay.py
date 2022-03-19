from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Delay:
	"""Delay commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("delay", core, parent)

	def set(self, delay: float, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:TRIGger:OUTPut<CH>:DELay \n
		Snippet: driver.source.bb.arbitrary.trigger.output.delay.set(delay = 1.0, output = repcap.Output.Default) \n
		Defines the delay between the signal on the marker outputs and the start of the signals. \n
			:param delay: integer Range: 0 to depends on other values, Unit: Symbol
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.decimal_value_to_str(delay)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:TRIGger:OUTPut{output_cmd_val}:DELay {param}')

	def get(self, output=repcap.Output.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:TRIGger:OUTPut<CH>:DELay \n
		Snippet: value: float = driver.source.bb.arbitrary.trigger.output.delay.get(output = repcap.Output.Default) \n
		Defines the delay between the signal on the marker outputs and the start of the signals. \n
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: delay: integer Range: 0 to depends on other values, Unit: Symbol"""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ARBitrary:TRIGger:OUTPut{output_cmd_val}:DELay?')
		return Conversions.str_to_float(response)
