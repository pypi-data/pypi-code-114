from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DinSec:
	"""DinSec commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dinSec", core, parent)

	def get(self, output=repcap.Output.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TRIGger:OUTPut<CH>:DINSec \n
		Snippet: value: float = driver.source.bb.eutra.trigger.output.dinSec.get(output = repcap.Output.Default) \n
		Queries the marker delay in microseconds.
		You can define a marker delay in samples with [:SOURce<hw>]:BB:EUTRa:TRIGger:OUTPut<ch>:DELay. \n
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: delay_in_seconds: float Range: 0 to 16777215"""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:TRIGger:OUTPut{output_cmd_val}:DINSec?')
		return Conversions.str_to_float(response)
