from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SfIndex:
	"""SfIndex commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sfIndex", core, parent)

	def set(self, super_frame_index: int, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:TRIGger:OUTPut<CH>:SFINdex \n
		Snippet: driver.source.bb.dvb.trigger.output.sfIndex.set(super_frame_index = 1, output = repcap.Output.Default) \n
		No command help available \n
			:param super_frame_index: No help available
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.decimal_value_to_str(super_frame_index)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:TRIGger:OUTPut{output_cmd_val}:SFINdex {param}')

	def get(self, output=repcap.Output.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVB:TRIGger:OUTPut<CH>:SFINdex \n
		Snippet: value: int = driver.source.bb.dvb.trigger.output.sfIndex.get(output = repcap.Output.Default) \n
		No command help available \n
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: super_frame_index: No help available"""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:DVB:TRIGger:OUTPut{output_cmd_val}:SFINdex?')
		return Conversions.str_to_int(response)
