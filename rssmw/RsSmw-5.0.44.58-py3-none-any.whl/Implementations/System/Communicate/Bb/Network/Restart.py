from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Restart:
	"""Restart commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("restart", core, parent)

	def set(self) -> None:
		"""SCPI: SYSTem:COMMunicate:BB<HW>:NETWork:RESTart \n
		Snippet: driver.system.communicate.bb.network.restart.set() \n
		Restarts the network. \n
		"""
		self._core.io.write(f'SYSTem:COMMunicate:BB<HwInstance>:NETWork:RESTart')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: SYSTem:COMMunicate:BB<HW>:NETWork:RESTart \n
		Snippet: driver.system.communicate.bb.network.restart.set_with_opc() \n
		Restarts the network. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SYSTem:COMMunicate:BB<HwInstance>:NETWork:RESTart', opc_timeout_ms)
