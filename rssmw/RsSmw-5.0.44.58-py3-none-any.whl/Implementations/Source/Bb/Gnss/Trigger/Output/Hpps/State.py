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

	def set(self, high_prec_pps_stat: bool, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:TRIGger:OUTPut<CH>:HPPS:STATe \n
		Snippet: driver.source.bb.gnss.trigger.output.hpps.state.set(high_prec_pps_stat = False, output = repcap.Output.Default) \n
		Enables generation of a high-precision PPS marker signal. \n
			:param high_prec_pps_stat: 1| ON| 0| OFF
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.bool_to_str(high_prec_pps_stat)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:TRIGger:OUTPut{output_cmd_val}:HPPS:STATe {param}')

	def get(self, output=repcap.Output.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:TRIGger:OUTPut<CH>:HPPS:STATe \n
		Snippet: value: bool = driver.source.bb.gnss.trigger.output.hpps.state.get(output = repcap.Output.Default) \n
		Enables generation of a high-precision PPS marker signal. \n
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: high_prec_pps_stat: 1| ON| 0| OFF"""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:TRIGger:OUTPut{output_cmd_val}:HPPS:STATe?')
		return Conversions.str_to_bool(response)
