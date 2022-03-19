from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Usb:
	"""Usb commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("usb", core, parent)

	def set(self) -> None:
		"""SCPI: SLISt:CLEar:USB \n
		Snippet: driver.slist.clear.usb.set() \n
		Removes all R&S NRP power sensors connected over USB from the list. \n
		"""
		self._core.io.write(f'SLISt:CLEar:USB')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: SLISt:CLEar:USB \n
		Snippet: driver.slist.clear.usb.set_with_opc() \n
		Removes all R&S NRP power sensors connected over USB from the list. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SLISt:CLEar:USB', opc_timeout_ms)
