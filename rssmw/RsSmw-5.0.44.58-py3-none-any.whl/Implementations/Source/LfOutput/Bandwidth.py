from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bandwidth:
	"""Bandwidth commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bandwidth", core, parent)

	# noinspection PyTypeChecker
	def get(self, lfOutput=repcap.LfOutput.Default) -> enums.LfBwidth:
		"""SCPI: [SOURce]:LFOutput<CH>:BANDwidth \n
		Snippet: value: enums.LfBwidth = driver.source.lfOutput.bandwidth.get(lfOutput = repcap.LfOutput.Default) \n
		Queries the bandwidth of the external LF signal. \n
			:param lfOutput: optional repeated capability selector. Default value: Nr1 (settable in the interface 'LfOutput')
			:return: bandwidth: BW0M2| BW10m"""
		lfOutput_cmd_val = self._cmd_group.get_repcap_cmd_value(lfOutput, repcap.LfOutput)
		response = self._core.io.query_str(f'SOURce:LFOutput{lfOutput_cmd_val}:BANDwidth?')
		return Conversions.str_to_scalar_enum(response, enums.LfBwidth)
