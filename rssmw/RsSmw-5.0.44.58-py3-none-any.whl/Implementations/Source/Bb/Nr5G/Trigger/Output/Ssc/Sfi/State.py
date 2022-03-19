from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, use_spec_slot_idx: bool, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TRIGger:OUTPut<CH>:SSC:SFI:STATe \n
		Snippet: driver.source.bb.nr5G.trigger.output.ssc.sfi.state.set(use_spec_slot_idx = False, output = repcap.Output.Default) \n
		Turns usage of the special slot format on and off. If on, select a special frame as defined by 3GPP with
		[:SOURce<hw>]:BB:NR5G:TRIGger:OUTPut<ch>:SSC:SLFMt.
			INTRO_CMD_HELP: If off, select the number of symbols with \n
			- Downlink: [:SOURce<hw>]:BB:NR5G:TRIGger:OUTPut<ch>:SSC:NDLSymbols
			- Uplink: [:SOURce<hw>]:BB:NR5G:TRIGger:OUTPut<ch>:SSC:NULSymbols \n
			:param use_spec_slot_idx: 1| ON| 0| OFF
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.bool_to_str(use_spec_slot_idx)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TRIGger:OUTPut{output_cmd_val}:SSC:SFI:STATe {param}')

	def get(self, output=repcap.Output.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TRIGger:OUTPut<CH>:SSC:SFI:STATe \n
		Snippet: value: bool = driver.source.bb.nr5G.trigger.output.ssc.sfi.state.get(output = repcap.Output.Default) \n
		Turns usage of the special slot format on and off. If on, select a special frame as defined by 3GPP with
		[:SOURce<hw>]:BB:NR5G:TRIGger:OUTPut<ch>:SSC:SLFMt.
			INTRO_CMD_HELP: If off, select the number of symbols with \n
			- Downlink: [:SOURce<hw>]:BB:NR5G:TRIGger:OUTPut<ch>:SSC:NDLSymbols
			- Uplink: [:SOURce<hw>]:BB:NR5G:TRIGger:OUTPut<ch>:SSC:NULSymbols \n
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: use_spec_slot_idx: No help available"""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:TRIGger:OUTPut{output_cmd_val}:SSC:SFI:STATe?')
		return Conversions.str_to_bool(response)
