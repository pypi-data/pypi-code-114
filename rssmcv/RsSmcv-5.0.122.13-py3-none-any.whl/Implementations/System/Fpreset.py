from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fpreset:
	"""Fpreset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fpreset", core, parent)

	def set(self) -> None:
		"""SCPI: SYSTem:FPReset \n
		Snippet: driver.system.fpreset.set() \n
		Triggers an instrument reset to the original state of delivery. \n
		"""
		self._core.io.write(f'SYSTem:FPReset')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: SYSTem:FPReset \n
		Snippet: driver.system.fpreset.set_with_opc() \n
		Triggers an instrument reset to the original state of delivery. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmcv.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SYSTem:FPReset', opc_timeout_ms)
