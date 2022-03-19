from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Output:
	"""Output commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("output", core, parent)

	def set(self, output: bool, external=repcap.External.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:TRIGger:[EXTernal<CH>]:SYNChronize:OUTPut \n
		Snippet: driver.source.bb.tetra.trigger.external.synchronize.output.set(output = False, external = repcap.External.Default) \n
		Enables signal output synchronous to the trigger event. \n
			:param output: 1| ON| 0| OFF
			:param external: optional repeated capability selector. Default value: Nr1 (settable in the interface 'External')
		"""
		param = Conversions.bool_to_str(output)
		external_cmd_val = self._cmd_group.get_repcap_cmd_value(external, repcap.External)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:TRIGger:EXTernal{external_cmd_val}:SYNChronize:OUTPut {param}')

	def get(self, external=repcap.External.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:TETRa:TRIGger:[EXTernal<CH>]:SYNChronize:OUTPut \n
		Snippet: value: bool = driver.source.bb.tetra.trigger.external.synchronize.output.get(external = repcap.External.Default) \n
		Enables signal output synchronous to the trigger event. \n
			:param external: optional repeated capability selector. Default value: Nr1 (settable in the interface 'External')
			:return: output: 1| ON| 0| OFF"""
		external_cmd_val = self._cmd_group.get_repcap_cmd_value(external, repcap.External)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TETRa:TRIGger:EXTernal{external_cmd_val}:SYNChronize:OUTPut?')
		return Conversions.str_to_bool(response)
