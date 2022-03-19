from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Invert:
	"""Invert commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("invert", core, parent)

	def set(self, invert: bool, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TRIGger:OUTPut<CH>:INVert \n
		Snippet: driver.source.bb.nr5G.trigger.output.invert.set(invert = False, output = repcap.Output.Default) \n
		Turns inversion of the marker signal on and off. \n
			:param invert: 1| ON| 0| OFF 1 | ON Marker is on a falling edge. 0 | OFF Marker is on a rising edge.
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.bool_to_str(invert)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TRIGger:OUTPut{output_cmd_val}:INVert {param}')

	def get(self, output=repcap.Output.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TRIGger:OUTPut<CH>:INVert \n
		Snippet: value: bool = driver.source.bb.nr5G.trigger.output.invert.get(output = repcap.Output.Default) \n
		Turns inversion of the marker signal on and off. \n
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: invert: 1| ON| 0| OFF 1 | ON Marker is on a falling edge. 0 | OFF Marker is on a rising edge."""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:TRIGger:OUTPut{output_cmd_val}:INVert?')
		return Conversions.str_to_bool(response)
