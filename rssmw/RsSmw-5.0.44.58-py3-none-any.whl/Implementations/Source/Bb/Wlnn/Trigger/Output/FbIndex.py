from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FbIndex:
	"""FbIndex commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fbIndex", core, parent)

	def set(self, fb_index: int, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:TRIGger:OUTPut<CH>:FBINdex \n
		Snippet: driver.source.bb.wlnn.trigger.output.fbIndex.set(fb_index = 1, output = repcap.Output.Default) \n
		Sets the frame block index. For this/these frame block(s) , a marker signal is generated. The maximum value depends on
		the number of the currently active frame blocks (max = 100) . \n
			:param fb_index: integer Range: 0 to 100
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.decimal_value_to_str(fb_index)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:TRIGger:OUTPut{output_cmd_val}:FBINdex {param}')

	def get(self, output=repcap.Output.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:WLNN:TRIGger:OUTPut<CH>:FBINdex \n
		Snippet: value: int = driver.source.bb.wlnn.trigger.output.fbIndex.get(output = repcap.Output.Default) \n
		Sets the frame block index. For this/these frame block(s) , a marker signal is generated. The maximum value depends on
		the number of the currently active frame blocks (max = 100) . \n
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: fb_index: integer Range: 0 to 100"""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:TRIGger:OUTPut{output_cmd_val}:FBINdex?')
		return Conversions.str_to_int(response)
