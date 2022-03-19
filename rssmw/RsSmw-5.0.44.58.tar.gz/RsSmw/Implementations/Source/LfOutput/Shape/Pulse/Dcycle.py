from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dcycle:
	"""Dcycle commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dcycle", core, parent)

	def set(self, dcycle: float, lfOutput=repcap.LfOutput.Default) -> None:
		"""SCPI: [SOURce<HW>]:LFOutput<CH>:SHAPe:PULSe:DCYCle \n
		Snippet: driver.source.lfOutput.shape.pulse.dcycle.set(dcycle = 1.0, lfOutput = repcap.LfOutput.Default) \n
		Sets the duty cycle for the shape pulse. \n
			:param dcycle: float Range: 1E-6 to 100, Unit: PCT
			:param lfOutput: optional repeated capability selector. Default value: Nr1 (settable in the interface 'LfOutput')
		"""
		param = Conversions.decimal_value_to_str(dcycle)
		lfOutput_cmd_val = self._cmd_group.get_repcap_cmd_value(lfOutput, repcap.LfOutput)
		self._core.io.write(f'SOURce<HwInstance>:LFOutput{lfOutput_cmd_val}:SHAPe:PULSe:DCYCle {param}')

	def get(self, lfOutput=repcap.LfOutput.Default) -> float:
		"""SCPI: [SOURce<HW>]:LFOutput<CH>:SHAPe:PULSe:DCYCle \n
		Snippet: value: float = driver.source.lfOutput.shape.pulse.dcycle.get(lfOutput = repcap.LfOutput.Default) \n
		Sets the duty cycle for the shape pulse. \n
			:param lfOutput: optional repeated capability selector. Default value: Nr1 (settable in the interface 'LfOutput')
			:return: dcycle: float Range: 1E-6 to 100, Unit: PCT"""
		lfOutput_cmd_val = self._cmd_group.get_repcap_cmd_value(lfOutput, repcap.LfOutput)
		response = self._core.io.query_str(f'SOURce<HwInstance>:LFOutput{lfOutput_cmd_val}:SHAPe:PULSe:DCYCle?')
		return Conversions.str_to_float(response)
