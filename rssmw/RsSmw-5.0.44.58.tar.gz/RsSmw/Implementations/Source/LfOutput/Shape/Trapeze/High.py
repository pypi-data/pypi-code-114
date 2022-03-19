from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class High:
	"""High commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("high", core, parent)

	def set(self, high: float, lfOutput=repcap.LfOutput.Default) -> None:
		"""SCPI: [SOURce<HW>]:LFOutput<CH>:SHAPe:TRAPeze:HIGH \n
		Snippet: driver.source.lfOutput.shape.trapeze.high.set(high = 1.0, lfOutput = repcap.LfOutput.Default) \n
		Sets the high time for the trapezoid signal of the LF generator. \n
			:param high: float Range: 1E-6 to 100
			:param lfOutput: optional repeated capability selector. Default value: Nr1 (settable in the interface 'LfOutput')
		"""
		param = Conversions.decimal_value_to_str(high)
		lfOutput_cmd_val = self._cmd_group.get_repcap_cmd_value(lfOutput, repcap.LfOutput)
		self._core.io.write(f'SOURce<HwInstance>:LFOutput{lfOutput_cmd_val}:SHAPe:TRAPeze:HIGH {param}')

	def get(self, lfOutput=repcap.LfOutput.Default) -> float:
		"""SCPI: [SOURce<HW>]:LFOutput<CH>:SHAPe:TRAPeze:HIGH \n
		Snippet: value: float = driver.source.lfOutput.shape.trapeze.high.get(lfOutput = repcap.LfOutput.Default) \n
		Sets the high time for the trapezoid signal of the LF generator. \n
			:param lfOutput: optional repeated capability selector. Default value: Nr1 (settable in the interface 'LfOutput')
			:return: high: float Range: 1E-6 to 100"""
		lfOutput_cmd_val = self._cmd_group.get_repcap_cmd_value(lfOutput, repcap.LfOutput)
		response = self._core.io.query_str(f'SOURce<HwInstance>:LFOutput{lfOutput_cmd_val}:SHAPe:TRAPeze:HIGH?')
		return Conversions.str_to_float(response)
