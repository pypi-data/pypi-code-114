from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NulSlots:
	"""NulSlots commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nulSlots", core, parent)

	def set(self, num_ul_slots: int, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TRIGger:OUTPut<CH>:NULSlots \n
		Snippet: driver.source.bb.nr5G.trigger.output.nulSlots.set(num_ul_slots = 1, output = repcap.Output.Default) \n
		Sets the number of UL slots in a UL/DL pattern containing a marker. \n
			:param num_ul_slots: integer Range: 0 to 10
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.decimal_value_to_str(num_ul_slots)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TRIGger:OUTPut{output_cmd_val}:NULSlots {param}')

	def get(self, output=repcap.Output.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TRIGger:OUTPut<CH>:NULSlots \n
		Snippet: value: int = driver.source.bb.nr5G.trigger.output.nulSlots.get(output = repcap.Output.Default) \n
		Sets the number of UL slots in a UL/DL pattern containing a marker. \n
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: num_ul_slots: integer Range: 0 to 10"""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:TRIGger:OUTPut{output_cmd_val}:NULSlots?')
		return Conversions.str_to_int(response)
