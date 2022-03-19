from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NdlSymbols:
	"""NdlSymbols commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ndlSymbols", core, parent)

	def set(self, spec_slot_dl_sym: int, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TRIGger:OUTPut<CH>:SSC:NDLSymbols \n
		Snippet: driver.source.bb.nr5G.trigger.output.ssc.ndlSymbols.set(spec_slot_dl_sym = 1, output = repcap.Output.Default) \n
		Defines the number of uplink symbols in a special slot that contains a marker.
			INTRO_CMD_HELP: Prerequisites to define the number of downlink symbols: \n
			- Enter uplink mode ([:SOURce<hw>]:BB:NR5G:LINK) .
			- Turn off usage of special slot format ([:SOURce<hw>]:BB:NR5G:TRIGger:OUTPut<ch>:SSC:SFI:STATe) .
		Otherwise, the command is a query only. \n
			:param spec_slot_dl_sym: integer Range: 0 to 14
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.decimal_value_to_str(spec_slot_dl_sym)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TRIGger:OUTPut{output_cmd_val}:SSC:NDLSymbols {param}')

	def get(self, output=repcap.Output.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TRIGger:OUTPut<CH>:SSC:NDLSymbols \n
		Snippet: value: int = driver.source.bb.nr5G.trigger.output.ssc.ndlSymbols.get(output = repcap.Output.Default) \n
		Defines the number of uplink symbols in a special slot that contains a marker.
			INTRO_CMD_HELP: Prerequisites to define the number of downlink symbols: \n
			- Enter uplink mode ([:SOURce<hw>]:BB:NR5G:LINK) .
			- Turn off usage of special slot format ([:SOURce<hw>]:BB:NR5G:TRIGger:OUTPut<ch>:SSC:SFI:STATe) .
		Otherwise, the command is a query only. \n
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: spec_slot_dl_sym: No help available"""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:TRIGger:OUTPut{output_cmd_val}:SSC:NDLSymbols?')
		return Conversions.str_to_int(response)
