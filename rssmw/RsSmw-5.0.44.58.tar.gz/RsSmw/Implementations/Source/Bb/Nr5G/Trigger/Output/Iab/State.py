from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, iab_state: bool, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TRIGger:OUTPut<CH>:IAB:STATe \n
		Snippet: driver.source.bb.nr5G.trigger.output.iab.state.set(iab_state = False, output = repcap.Output.Default) \n
		Turns usage of the IAB frame format on and off. \n
			:param iab_state: 1| ON| 0| OFF
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.bool_to_str(iab_state)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TRIGger:OUTPut{output_cmd_val}:IAB:STATe {param}')

	def get(self, output=repcap.Output.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TRIGger:OUTPut<CH>:IAB:STATe \n
		Snippet: value: bool = driver.source.bb.nr5G.trigger.output.iab.state.get(output = repcap.Output.Default) \n
		Turns usage of the IAB frame format on and off. \n
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: iab_state: No help available"""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:TRIGger:OUTPut{output_cmd_val}:IAB:STATe?')
		return Conversions.str_to_bool(response)
