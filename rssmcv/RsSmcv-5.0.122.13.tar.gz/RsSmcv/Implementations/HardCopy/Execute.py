from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Execute:
	"""Execute commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("execute", core, parent)

	def set(self) -> None:
		"""SCPI: HCOPy:[EXECute] \n
		Snippet: driver.hardCopy.execute.set() \n
		Generates a hard copy of the current display. The output destination is a file. \n
		"""
		self._core.io.write(f'HCOPy:EXECute')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: HCOPy:[EXECute] \n
		Snippet: driver.hardCopy.execute.set_with_opc() \n
		Generates a hard copy of the current display. The output destination is a file. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmcv.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'HCOPy:EXECute', opc_timeout_ms)
