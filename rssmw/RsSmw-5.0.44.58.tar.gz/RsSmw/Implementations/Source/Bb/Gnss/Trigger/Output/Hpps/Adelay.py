from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Adelay:
	"""Adelay commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("adelay", core, parent)

	def set(self, additional_delay: float, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:TRIGger:OUTPut<CH>:HPPS:ADELay \n
		Snippet: driver.source.bb.gnss.trigger.output.hpps.adelay.set(additional_delay = 1.0, output = repcap.Output.Default) \n
		Sets an additional delay for the high-precision PPS marker signal. \n
			:param additional_delay: float Range: 0 to 10E-6
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.decimal_value_to_str(additional_delay)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:TRIGger:OUTPut{output_cmd_val}:HPPS:ADELay {param}')

	def get(self, output=repcap.Output.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:TRIGger:OUTPut<CH>:HPPS:ADELay \n
		Snippet: value: float = driver.source.bb.gnss.trigger.output.hpps.adelay.get(output = repcap.Output.Default) \n
		Sets an additional delay for the high-precision PPS marker signal. \n
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: additional_delay: float Range: 0 to 10E-6"""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:TRIGger:OUTPut{output_cmd_val}:HPPS:ADELay?')
		return Conversions.str_to_float(response)
