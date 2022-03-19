from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Period:
	"""Period commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("period", core, parent)

	def set(self, period: int, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:XMRadio:TERRestrial:TRIGger:OUTPut<CH>:PERiod \n
		Snippet: driver.source.bb.xmRadio.terrestrial.trigger.output.period.set(period = 1, output = repcap.Output.Default) \n
		No command help available \n
			:param period: No help available
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.decimal_value_to_str(period)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:XMRadio:TERRestrial:TRIGger:OUTPut{output_cmd_val}:PERiod {param}')

	def get(self, output=repcap.Output.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:XMRadio:TERRestrial:TRIGger:OUTPut<CH>:PERiod \n
		Snippet: value: int = driver.source.bb.xmRadio.terrestrial.trigger.output.period.get(output = repcap.Output.Default) \n
		No command help available \n
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: period: No help available"""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:XMRadio:TERRestrial:TRIGger:OUTPut{output_cmd_val}:PERiod?')
		return Conversions.str_to_int(response)
