from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pattern:
	"""Pattern commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pattern", core, parent)

	def set(self, pattern: List[str], output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:TRIGger:OUTPut<CH>:PATTern \n
		Snippet: driver.source.bb.wlnn.trigger.output.pattern.set(pattern = ['raw1', 'raw2', 'raw3'], output = repcap.Output.Default) \n
		Defines the bit pattern used to generate the marker signal if [:SOURce<hw>]:BB:WLNN:TRIGger:OUTPut<ch>:MODEis set to
		PATTern. \n
			:param pattern: 64 bits 0 = marker off, 1 = marker on
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.list_to_csv_str(pattern)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:TRIGger:OUTPut{output_cmd_val}:PATTern {param}')

	def get(self, output=repcap.Output.Default) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:WLNN:TRIGger:OUTPut<CH>:PATTern \n
		Snippet: value: List[str] = driver.source.bb.wlnn.trigger.output.pattern.get(output = repcap.Output.Default) \n
		Defines the bit pattern used to generate the marker signal if [:SOURce<hw>]:BB:WLNN:TRIGger:OUTPut<ch>:MODEis set to
		PATTern. \n
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: pattern: 64 bits 0 = marker off, 1 = marker on"""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:TRIGger:OUTPut{output_cmd_val}:PATTern?')
		return Conversions.str_to_str_list(response)
