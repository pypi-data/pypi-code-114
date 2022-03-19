from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ReShift:
	"""ReShift commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("reShift", core, parent)

	def set(self, shift: int, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:TRIGger:OUTPut<CH>:RESHift \n
		Snippet: driver.source.bb.wlnn.trigger.output.reShift.set(shift = 1, output = repcap.Output.Default) \n
		Shifts the rising edge of the marker the specified number of samples. Negative values result in a shift back of the
		marker edge. \n
			:param shift: integer Range: -1000 to 1000
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.decimal_value_to_str(shift)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:TRIGger:OUTPut{output_cmd_val}:RESHift {param}')

	def get(self, output=repcap.Output.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:WLNN:TRIGger:OUTPut<CH>:RESHift \n
		Snippet: value: int = driver.source.bb.wlnn.trigger.output.reShift.get(output = repcap.Output.Default) \n
		Shifts the rising edge of the marker the specified number of samples. Negative values result in a shift back of the
		marker edge. \n
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: shift: integer Range: -1000 to 1000"""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:TRIGger:OUTPut{output_cmd_val}:RESHift?')
		return Conversions.str_to_int(response)
