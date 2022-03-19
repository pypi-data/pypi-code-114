from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Lan:
	"""Lan commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lan", core, parent)

	def set(self) -> None:
		"""SCPI: SLISt:CLEar:LAN \n
		Snippet: driver.slist.clear.lan.set() \n
		Removes all R&S NRP power sensors connected in the LAN from the list. \n
		"""
		self._core.io.write(f'SLISt:CLEar:LAN')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: SLISt:CLEar:LAN \n
		Snippet: driver.slist.clear.lan.set_with_opc() \n
		Removes all R&S NRP power sensors connected in the LAN from the list. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SLISt:CLEar:LAN', opc_timeout_ms)
