from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Foffset:
	"""Foffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("foffset", core, parent)

	def set(self, mark_fall_offs: int, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:TRIGger:OUTPut<CH>:FOFFset \n
		Snippet: driver.source.bb.ofdm.trigger.output.foffset.set(mark_fall_offs = 1, output = repcap.Output.Default) \n
		Shifts the rising or falling ramp of the marker by the selected number of samples. \n
			:param mark_fall_offs: integer Range: -640000 to 640000
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.decimal_value_to_str(mark_fall_offs)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:TRIGger:OUTPut{output_cmd_val}:FOFFset {param}')

	def get(self, output=repcap.Output.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:OFDM:TRIGger:OUTPut<CH>:FOFFset \n
		Snippet: value: int = driver.source.bb.ofdm.trigger.output.foffset.get(output = repcap.Output.Default) \n
		Shifts the rising or falling ramp of the marker by the selected number of samples. \n
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: mark_fall_offs: integer Range: -640000 to 640000"""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:OFDM:TRIGger:OUTPut{output_cmd_val}:FOFFset?')
		return Conversions.str_to_int(response)
