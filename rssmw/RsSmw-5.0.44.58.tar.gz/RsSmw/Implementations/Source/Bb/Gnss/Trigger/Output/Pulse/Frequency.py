from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	def get(self, output=repcap.Output.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:TRIGger:OUTPut<CH>:PULSe:FREQuency \n
		Snippet: value: float = driver.source.bb.gnss.trigger.output.pulse.frequency.get(output = repcap.Output.Default) \n
		Queries the pulse frequency of the pulsed marker signal. The pulse frequency is derived by dividing the symbol rate by
		the divider. \n
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: frequency: float"""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:TRIGger:OUTPut{output_cmd_val}:PULSe:FREQuency?')
		return Conversions.str_to_float(response)
