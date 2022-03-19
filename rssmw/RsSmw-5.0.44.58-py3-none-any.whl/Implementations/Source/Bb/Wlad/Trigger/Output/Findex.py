from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Findex:
	"""Findex commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("findex", core, parent)

	def set(self, findex: int, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:TRIGger:OUTPut<CH>:FINDex \n
		Snippet: driver.source.bb.wlad.trigger.output.findex.set(findex = 1, output = repcap.Output.Default) \n
		Sets the frame index, the frame to be marked in the frame block. \n
			:param findex: integer Range: 1 to 53687
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.decimal_value_to_str(findex)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:TRIGger:OUTPut{output_cmd_val}:FINDex {param}')

	def get(self, output=repcap.Output.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:WLAD:TRIGger:OUTPut<CH>:FINDex \n
		Snippet: value: int = driver.source.bb.wlad.trigger.output.findex.get(output = repcap.Output.Default) \n
		Sets the frame index, the frame to be marked in the frame block. \n
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: findex: integer Range: 1 to 53687"""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLAD:TRIGger:OUTPut{output_cmd_val}:FINDex?')
		return Conversions.str_to_int(response)
