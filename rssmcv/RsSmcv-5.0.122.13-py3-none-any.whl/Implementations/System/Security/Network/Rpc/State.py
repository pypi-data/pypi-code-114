from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, sec_pass_word: str, rpc_state: bool) -> None:
		"""SCPI: SYSTem:SECurity:NETWork:RPC:[STATe] \n
		Snippet: driver.system.security.network.rpc.state.set(sec_pass_word = '1', rpc_state = False) \n
		No command help available \n
			:param sec_pass_word: No help available
			:param rpc_state: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('sec_pass_word', sec_pass_word, DataType.String), ArgSingle('rpc_state', rpc_state, DataType.Boolean))
		self._core.io.write(f'SYSTem:SECurity:NETWork:RPC:STATe {param}'.rstrip())

	def get(self) -> bool:
		"""SCPI: SYSTem:SECurity:NETWork:RPC:[STATe] \n
		Snippet: value: bool = driver.system.security.network.rpc.state.get() \n
		No command help available \n
			:return: rpc_state: No help available"""
		response = self._core.io.query_str(f'SYSTem:SECurity:NETWork:RPC:STATe?')
		return Conversions.str_to_bool(response)
