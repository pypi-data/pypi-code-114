from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Offset:
	"""Offset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	def set(self, offset: float, lfOutput=repcap.LfOutput.Default) -> None:
		"""SCPI: [SOURce]:LFOutput<CH>:OFFSet \n
		Snippet: driver.source.lfOutput.offset.set(offset = 1.0, lfOutput = repcap.LfOutput.Default) \n
		Sets a DC offset at the selected LF Output. \n
			:param offset: float Range: -3.6 to 3.6, Unit: V
			:param lfOutput: optional repeated capability selector. Default value: Nr1 (settable in the interface 'LfOutput')
		"""
		param = Conversions.decimal_value_to_str(offset)
		lfOutput_cmd_val = self._cmd_group.get_repcap_cmd_value(lfOutput, repcap.LfOutput)
		self._core.io.write(f'SOURce:LFOutput{lfOutput_cmd_val}:OFFSet {param}')

	def get(self, lfOutput=repcap.LfOutput.Default) -> float:
		"""SCPI: [SOURce]:LFOutput<CH>:OFFSet \n
		Snippet: value: float = driver.source.lfOutput.offset.get(lfOutput = repcap.LfOutput.Default) \n
		Sets a DC offset at the selected LF Output. \n
			:param lfOutput: optional repeated capability selector. Default value: Nr1 (settable in the interface 'LfOutput')
			:return: offset: float Range: -3.6 to 3.6, Unit: V"""
		lfOutput_cmd_val = self._cmd_group.get_repcap_cmd_value(lfOutput, repcap.LfOutput)
		response = self._core.io.query_str(f'SOURce:LFOutput{lfOutput_cmd_val}:OFFSet?')
		return Conversions.str_to_float(response)
