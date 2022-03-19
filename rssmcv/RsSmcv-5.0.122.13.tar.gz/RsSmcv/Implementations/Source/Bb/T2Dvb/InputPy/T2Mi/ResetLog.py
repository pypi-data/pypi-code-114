from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ResetLog:
	"""ResetLog commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("resetLog", core, parent)

	def set(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:INPut:T2MI:RESetlog \n
		Snippet: driver.source.bb.t2Dvb.inputPy.t2Mi.resetLog.set() \n
		Resets the log file. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:INPut:T2MI:RESetlog')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:INPut:T2MI:RESetlog \n
		Snippet: driver.source.bb.t2Dvb.inputPy.t2Mi.resetLog.set_with_opc() \n
		Resets the log file. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmcv.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:T2DVb:INPut:T2MI:RESetlog', opc_timeout_ms)
