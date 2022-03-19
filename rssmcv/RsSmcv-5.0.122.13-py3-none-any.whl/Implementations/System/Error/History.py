from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class History:
	"""History commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("history", core, parent)

	def clear(self) -> None:
		"""SCPI: SYSTem:ERRor:HISTory:CLEar \n
		Snippet: driver.system.error.history.clear() \n
		Clears the error history. \n
		"""
		self._core.io.write(f'SYSTem:ERRor:HISTory:CLEar')

	def clear_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: SYSTem:ERRor:HISTory:CLEar \n
		Snippet: driver.system.error.history.clear_with_opc() \n
		Clears the error history. \n
		Same as clear, but waits for the operation to complete before continuing further. Use the RsSmcv.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SYSTem:ERRor:HISTory:CLEar', opc_timeout_ms)

	def get_value(self) -> str:
		"""SCPI: SYSTem:ERRor:HISTory \n
		Snippet: value: str = driver.system.error.history.get_value() \n
		No command help available \n
			:return: error_history: No help available
		"""
		response = self._core.io.query_str('SYSTem:ERRor:HISTory?')
		return trim_str_response(response)
