from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, lfOutput=repcap.LfOutput.Default) -> None:
		"""SCPI: [SOURce]:LFOutput<CH>:[STATe] \n
		Snippet: driver.source.lfOutput.state.set(state = False, lfOutput = repcap.LfOutput.Default) \n
		Activates LF signal output. \n
			:param state: 1| ON| 0| OFF
			:param lfOutput: optional repeated capability selector. Default value: Nr1 (settable in the interface 'LfOutput')
		"""
		param = Conversions.bool_to_str(state)
		lfOutput_cmd_val = self._cmd_group.get_repcap_cmd_value(lfOutput, repcap.LfOutput)
		self._core.io.write(f'SOURce:LFOutput{lfOutput_cmd_val}:STATe {param}')

	def get(self, lfOutput=repcap.LfOutput.Default) -> bool:
		"""SCPI: [SOURce]:LFOutput<CH>:[STATe] \n
		Snippet: value: bool = driver.source.lfOutput.state.get(lfOutput = repcap.LfOutput.Default) \n
		Activates LF signal output. \n
			:param lfOutput: optional repeated capability selector. Default value: Nr1 (settable in the interface 'LfOutput')
			:return: state: 1| ON| 0| OFF"""
		lfOutput_cmd_val = self._cmd_group.get_repcap_cmd_value(lfOutput, repcap.LfOutput)
		response = self._core.io.query_str(f'SOURce:LFOutput{lfOutput_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
